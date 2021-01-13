from logging.config import dictConfig

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


from config import LOGGING_CONFIG


dictConfig(LOGGING_CONFIG)


app = Flask(__name__)
app.config.from_object('config.DevConfig')

db = SQLAlchemy(app)



@app.route('/')
def index():
    app.logger.info('info')
    app.logger.warning('warning')
    app.logger.debug('debug')
    app.logger.error('error')
    return ''


if __name__ == '__main__':
    app.run(port=9999, threaded=True)
