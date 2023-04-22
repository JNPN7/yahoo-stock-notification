from yahoo_notifier.notifier import notify, hourly_subscribers

from flask import Flask, redirect, render_template, request, jsonify, Response
from routes.web import blueprint
from time import sleep
import asyncio
import threading


if __name__ == '__main__':  # Running the app
    t1 = threading.Thread(target=notify, name="notify")
    t1.start()

    app = Flask(__name__)

    # Registering blueprints
    app.register_blueprint(blueprint)
    app.run(host='127.0.0.1', port=5000, debug=True)

    # while True:
    #     sleep(35)
    #     hourly_subscribers["hahaha@gmail.com"] = {
    #         'email': "ids.major.project@gmail.com",
    #         'stock_sym': "META",
    #         'interval': 1,
    #         'current': 1,
    #         'threshold': 100,
    #     }
    #     sleep(35)
    #     hourly_subscribers["new@gmail.com"] = {
    #         'email': "ids.major.project@gmail.com",
    #         'stock_sym': "AAPL",
    #         'interval': 1,
    #         'current': 1,
    #         'threshold': 100,
    #     }