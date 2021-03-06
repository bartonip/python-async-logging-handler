from logging import FileHandler
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from log4mongo.handlers import MongoHandler
from threading import Thread
from queue import Queue


class AsyncHandlerMixin(object):
    def __init__(self, *args, **kwargs):
        super(AsyncHandlerMixin, self).__init__(*args, **kwargs)
        self.__queue = Queue()
        self.__thread = Thread(target=self.__loop)
        self.__thread.daemon = True
        self.__thread.start()

    def emit(self, record):
        self.__queue.put(record)

    def __loop(self):
        while True:
            record = self.__queue.get()
            try:
                super(AsyncHandlerMixin, self).emit(record)
            except:
                pass


class AsyncFileHandler(AsyncHandlerMixin, FileHandler):
    pass


class AsyncRotatingFileHandler(AsyncHandlerMixin, RotatingFileHandler):
    pass


class AsyncTimedRotatingFileHandler(AsyncHandlerMixin, TimedRotatingFileHandler):
    pass

class AsyncMongoHandler(AsyncHandlerMixin, MongoHandler):
    pass