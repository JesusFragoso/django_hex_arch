import os

bind = os.environ.get("BIND_SERVER")
workers = os.environ.get("WORKERS")
timeout = os.environ.get("SERVER_TIMEOUT")
keepalive = os.environ.get("KEEP_ALIVE_SERVER")
reload = os.environ.get("RELOAD_SERVER")