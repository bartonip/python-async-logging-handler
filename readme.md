**async_logging_handler**

Super-simple extensions for standard Python's ``logging.FileHandler``, ``logging.handlers.RotatingFileHandler`` and ``logging.handlers.TimedRotatingFileHandler``
with asynchronous writing to file (utilizing standard ``Queue.Queue``).

Support for ``MongoHandler`` has also been added.

Useful when using logging in programs, where long-time blocking for logging to file is not allowed.

**Installation**

```bash
pip install git+https://github.com/bartonip/python-async-logging-handler.git
```

**Using**

```python
from async_logging_handler import AsyncFileHandler

# ...

async_handler = AsyncFileHandler(filename)
some_logger.addHandler(async_handler)
```
