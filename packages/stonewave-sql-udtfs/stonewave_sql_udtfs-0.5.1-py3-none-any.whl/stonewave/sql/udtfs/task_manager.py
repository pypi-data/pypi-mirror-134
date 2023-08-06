import multiprocessing as mp
from threading import Semaphore, Lock
from stonewave.sql.udtfs.logger import logger


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class TaskManager(object):
    # ideally the pool_size can be controlled by a config variable
    def __init__(self, pool_size=mp.cpu_count()):
        self._reset(pool_size=pool_size)

    ## add a reset function used in unit test for this singleton object, mock reinitilization of TaskManager
    def _reset(self, pool_size=mp.cpu_count()):
        if hasattr(self, "_pool"):
            self._pool.close()
            self._pool.terminate()
        logger.info("init worker pool", pool_size=pool_size)
        # TODO change max_limit to a configuarable constant
        self.max_limit = 32
        self.max_pool_size = pool_size
        self._pool = mp.Pool(processes=pool_size, maxtasksperchild=1)
        self.workers = Semaphore(pool_size)
        # ensures the semaphore is not replaced while used
        self.workers_mutex = Lock()
        self._pipe_map = {}

    def get_pool(self):
        return self._pool

    def get_map(self):
        return self._pipe_map

    def change_pool_size(self, new_size):
        """Set the Pool to a new size."""
        logger.info("change task manager pool size")
        with self.workers_mutex:
            if new_size > self.max_limit or new_size <= 0:
                logger.error("new pool size not in the range of 0 and cpu count size")
                return False
            current_value = self.workers._value
            diff_value = new_size - self.max_pool_size
            value = current_value + diff_value
            if value < 0:
                logger.error(
                    "pool workers still running, semaphore value can not be negative", changed_semaphore_value=value
                )
                return False
            self.workers = Semaphore(value)
            self.max_pool_size = new_size
            return True
        return False

    def new_task(self, task, args):
        """Start a new task, blocks if queue is full."""
        with self.workers_mutex:
            if not self.workers.acquire(blocking=False):
                return False

        result = self._pool.apply_async(task, args=args, callback=self.task_done)
        return result

    def task_done(self, *args, **kwargs):
        """Called once task is done, releases the queue is blocked."""
        with self.workers_mutex:
            logger.debug("function execution task done")
            self.workers.release()
