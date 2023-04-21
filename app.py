from yahoo_notifier.notifier import notify

from flask import Flask, redirect, render_template, request, jsonify, Response
from routes.web import blueprint
from time import sleep
import asyncio
import threading

app = Flask(__name__)

# Registering blueprints

# # Registering custom functions to be used within templates
# app.jinja_env.globals.update(
#     ago=ago,
#     str=str,
# )

# Registering the blueprint
app.register_blueprint(blueprint)

if __name__ == '__main__':  # Running the app
    t1 = threading.Thread(target=notify, name="notify")
    t1.start()
    app.run(host='127.0.0.1', port=5000, debug=True)