from yahoo_notifier.notifier import hourly_subscribers, daily_subscribers, check_if_stock_symbol_exists
from flask import session, redirect, render_template, request, jsonify, Response, flash

subscribers: list = []

def home():
    return render_template('home.html')

def insert():
    hourly_subscribers.append(
        {
        'email': "haha@gmail.com",
        'stocks': "GOOG",
        'interval': 1,
        'current': 1,
        'threshold': 100
        }
    )
    return "OOK1"

def unsubscribe():
    if request.method == 'POST':
        req = request.form
        if req["email"]:
            isSubscriber = False
            if req["email"] in hourly_subscribers:
                isSubscriber = True
                del hourly_subscribers[req["email"]]
            if req["email"] in daily_subscribers:
                isSubscriber = True
                del daily_subscribers[req["email"]]
            if isSubscriber:
                return render_template('successfull.html', message="unsubscribed")

            return render_template("unsubscribe.html", error="You haven't subscribed yet")

        return render_template("unsubscribe.html", error="Enter email")

    return render_template("unsubscribe.html")



def subscribe():
    req = request.form
    if not check_if_stock_symbol_exists(req["stock"]):
        return render_template("home.html", error="Stock symbol doesn't exists")    
    
    try:
        subscriber = {
            "email": req["email"],
            "stock_sym": req["stock"],
            "interval": int(req["time"]),
            "current": 1,
            "threshold": float(req["threshold"])
        }
        if req['time-type'] == "hours":
            hourly_subscribers[req["email"]] = subscriber
        elif req['time-type'] == "days":
            daily_subscribers[req["email"]] = subscriber
        else:
            return render_template("home.html", error="Some error occured try again")    
    except:
        return render_template("home.html", error="Some error occured try again")    
    
    return render_template('successfull.html', message="subscribed")
