import logging


class FileWrite(logging.Handler):
    def __init__(self, filename):
        logging.Handler.__init__(self)
        self.filename = filename

    def emit(self, record):
        message = self.format(record)
        with open(self.filename, 'a') as file:
            file.write(message + '\n')


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'std_format': {
            'format': '{asctime} - {name} - {levelname} - {message}',
            'style': '{'
        }
    },
    'handlers': {

        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format'
        },
        'file': {
            '()': FileWrite,
            'level': 'DEBUG',
            'filename': 'debug.log',
            'formatter': 'std_format'
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']

            # 'propagate': False
        },

    },
    # 'filters': {},
    # 'root': {},
    # 'incremental': True,
}