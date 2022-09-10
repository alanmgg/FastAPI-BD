from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/home/ubuntu/FastAPI-BD/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/ubuntu/FastAPI-BD/access_log'
errorlog =  '/home/ubuntu/FastAPI-BD/error_log'