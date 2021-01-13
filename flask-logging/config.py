class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = None


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://user:password@host/db_name'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://user:password@host/db_name'


LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format':
                '%(asctime)s[%(levelname)s] %(module)s %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'file.handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'app.log',
            'maxBytes': 1024 * 1024,
            'backupCount': 3,
            'level': 'DEBUG',
            'formatter': 'default',
            'encoding': 'utf-8'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi', 'file.handler'],
    }
}
