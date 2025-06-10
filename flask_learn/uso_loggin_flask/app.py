from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    # app.logger.debug("Msg Debug")
    app.logger.info(f"Entrando al path {request.path}")
    # app.logger.warning("Msg Warning")
    # app.logger.error("Msg Error")
    return "Hello World"
