#!/usr/bin/env python

import app
import app.audit
import logging
import os
import www
from flask import Flask, jsonify, request
from logging.handlers import SysLogHandler


flaskApp = Flask(__name__)

logHandler = SysLogHandler(address="/dev/log")
formatter = logging.Formatter("trust-service: [%(levelname)s] %(message)s")

logHandler.setFormatter(formatter)
logHandler.setLevel(logging.DEBUG)
flaskApp.logger.addHandler(logHandler)
flaskApp.logger.setLevel(logging.DEBUG)

app.trust_blueprint.finder = app.FileFinder(
    data_path=os.path.join(os.path.dirname(__file__), "tests/system/data"),
    logger=flaskApp.logger,
    audit=app.audit.AuditToSyslog("trust-service-audit"))

flaskApp.register_blueprint(app.trust_blueprint, url_prefix="/service")
flaskApp.register_blueprint(www.docs_blueprint)

flaskApp.logger.info("The application started.")

if __name__ == "__main__":
    flaskApp.run(threaded=True)
