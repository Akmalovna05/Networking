"""Gunicorn configuration for the Cloud ERP Platform.

Run with:
    gunicorn cloud_erp_platform.wsgi:application -c gunicorn.conf.py
"""

import multiprocessing
import os

# Bind to a Unix socket shared with Nginx (preferred), or a TCP port.
# Override with the GUNICORN_BIND environment variable if needed.
bind = os.environ.get('GUNICORN_BIND', 'unix:/run/cloud_erp.sock')

# Worker processes: (2 x CPU cores) + 1 is a common starting point.
workers = int(os.environ.get('GUNICORN_WORKERS', multiprocessing.cpu_count() * 2 + 1))
worker_class = os.environ.get('GUNICORN_WORKER_CLASS', 'sync')
threads = int(os.environ.get('GUNICORN_THREADS', '2'))

# Recycle workers periodically to limit memory growth.
max_requests = 1000
max_requests_jitter = 100

# Timeouts (seconds).
timeout = int(os.environ.get('GUNICORN_TIMEOUT', '30'))
graceful_timeout = 30
keepalive = 5

# Logging to stdout/stderr so journald/systemd captures it.
accesslog = '-'
errorlog = '-'
loglevel = os.environ.get('GUNICORN_LOG_LEVEL', 'info')

# Process naming.
proc_name = 'cloud_erp'
