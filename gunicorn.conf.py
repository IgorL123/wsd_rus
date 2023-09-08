import multiprocessing

bind = "0.0.0.0:5000"
workers = 1
threads = 1
errorlog = "app/logs/gunicorn.log"
preload_app = True
