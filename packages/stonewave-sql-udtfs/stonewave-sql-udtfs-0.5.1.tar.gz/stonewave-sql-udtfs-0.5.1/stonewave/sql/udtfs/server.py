from fastapi import FastAPI, HTTPException
import multiprocessing as mp
from pydantic import BaseModel, Json
from typing import Optional
from stonewave.sql.udtfs.task_manager import TaskManager
import uvicorn
import asyncio
import stonewave.sql.udtfs.function_executor as function_executor
from stonewave.sql.udtfs.logger import logger, get_logger_config
import json

app = FastAPI()


class RequestObj(BaseModel):
    func_name: Optional[str] = None
    method: str
    params: Json

    class Config:
        schema_extra = {"example": {"func_name": "faker", "method": "eval", "params": {}}}


@app.post("/table-functions/execs")
async def create(req: RequestObj):
    try:
        func_name = req.func_name
        parent_conn, child_conn = mp.Pipe()
        task_manager = TaskManager()
        worker_value = task_manager.workers._value
        print(worker_value)
        while True:
            if task_manager.new_task(
                function_executor.execute_worker,
                (
                    func_name,
                    child_conn,
                    worker_value,
                ),
            ):
                break
            else:
                print("waiting at worker value {}".format(worker_value))
                await asyncio.sleep(0.2)

        parent_conn.send(req)
        response = parent_conn.recv()
        res_json = json.loads(response)
        execution_id = res_json.get("execution_id")
        if res_json.get("result") == "finish":
            parent_conn.close()
            logger.info("finish execution in create", execution_id=execution_id, req=str(req))
            return res_json
        queue_map = task_manager.get_map()
        if execution_id is None or queue_map.get(execution_id) is not None:
            raise HTTPException(status_code=500, detail="queue map execution_id not valid")
        logger.info("start execution", execution_id=execution_id, req=str(req), worker=worker_value)
        queue_map[execution_id] = parent_conn
        return res_json
    except HTTPException as e:
        print("error occured {}".format(str(e)))
        raise e
    except Exception as e:
        print("error occured {}".format(str(e)))
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/table-functions/execs/{execution_id}")
async def receive_req(req: RequestObj, execution_id: str):
    try:
        execution_id = execution_id
        task_manager = TaskManager()
        queue_map = task_manager.get_map()
        if execution_id is not None:
            parent_conn = queue_map.get(execution_id)
            if parent_conn is None:
                raise HTTPException(status_code=500, detail="queue map execution_id not valid")
            parent_conn.send(req)
            response = parent_conn.recv()
            res_json = json.loads(response)
            if res_json["result"] == "finish":
                pool_instance = TaskManager()
                queue_map.pop(execution_id)
                parent_conn.close()
                logger.info(
                    "finish execution, remaining number of workers: {}".format(pool_instance.workers._value),
                    execution_id=execution_id,
                    req=str(req),
                )
            return res_json
        else:
            raise HTTPException(status_code=400, detail="no execution_id provided")
    except HTTPException as e:
        print("error occured {}".format(str(e)))
        raise e
    except Exception as e:
        print("error occured {}".format(str(e)))
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/workers/pool-size")
async def repopulate(num_procs: int):
    pool_instance = TaskManager()
    if pool_instance.change_pool_size(num_procs):
        return "succeed"
    else:
        raise HTTPException(status_code=500, detail="repopulate internal error")


@app.get("/status")
async def heartbeat():
    return "success"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9720)
