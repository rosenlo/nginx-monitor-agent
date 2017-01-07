#!/usr/bin/env python
# encoding: utf-8

"""
Author: Rosen
Mail: rosenluov@gmail.com
File: settings.py
Created Time: 12/28/16 11:53
"""

import logging.config
from os import path
from socket import gethostname

BASE_DIR = path.dirname(path.abspath(__file__))
NGINX_FILE = BASE_DIR + '/nginx-config.yaml'
STATSD_FILE = BASE_DIR + '/statsd.yaml'
PID_FILE = '/var/run/nginx-monitor-agent/nginx-monitor-agent.pid'
HOSTNAME = gethostname()
URL = "http://127.0.0.1/req_status"

STDOUT = '/data/log/nginx-monitor-agent/nginx-agent.log'
STDERR = '/data/log/nginx-monitor-agent/nginx-agent.err'

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] [%(name)s] %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 50,
            # If delay is true,
            # then file opening is deferred until the first call to emit().
            'delay': True,
            'filename': STDOUT,
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    }
})

METRICS = {
    'domain': [
        'bytes_in',
        'bytes_out',
        'conn_total',
        'req_total',
        'http_2xx',
        'http_3xx',
        'http_4xx',
        'http_5xx',
        'http_other_status',
        'rt',
        'ups_req',
        'ups_rt',
        'ups_tries',
        'http_200',
        'http_206',
        'http_302',
        'http_304',
        'http_403',
        'http_404',
        'http_416',
        'http_499',
        'http_500',
        'http_502',
        'http_503',
        'http_504',
        'http_508',
        'http_other_detail_status',
        'http_ups_4xx',
        'http_ups_5xx'
    ]
}
