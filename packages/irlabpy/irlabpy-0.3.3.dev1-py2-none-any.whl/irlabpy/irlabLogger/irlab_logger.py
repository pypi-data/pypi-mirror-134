import os

def get_logger(file_name):
    import logging.config

    os.system('mkdir -p %s' % ("/home/admin/logs/irlab_logger"))

    logging.config.dictConfig({
        'version': 1, # 版本号，强制为1
        'disable_existing_loggers': True, # 是否禁用已经存在的logger对象，默认为True
        'formatters': { # 格式化器，指明了最终输出中日志记录的布局
            'verbose': {
                'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt': "%Y-%m-%d %H:%M:%S"
            }
        },
        'handlers': { # 处理器，将（记录器产生的）日志记录发送至合适的目的地
            'file': {
                'level': 'DEBUG',
                'class': 'cloghandler.ConcurrentRotatingFileHandler', # 日志处理类
                # 当达到10MB时分割日志
                'maxBytes': 1024 * 1024 * 10,
                # 最多保留50份文件
                'backupCount': 50,
                # If delay is true,
                # then file opening is deferred until the first call to emit().
                'delay': False,
                'filename': os.path.join("/home/admin/logs/irlab_logger", file_name),
                'formatter': 'verbose'
            }
        },
        'loggers': { # 记录器：暴露了应用程序代码能直接使用的接口
            'common': {
                'handlers': ['file'],
                'level': 'INFO'
            }
        }
    })

    return logging.getLogger('common')
