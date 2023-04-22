from yahoo_notifier.notifier import hourly_subscribers, daily_subscribers, check_if_stock_symbol_exists, get_stock_data
from flask import session, redirect, render_template, request, jsonify, Response, flash

subscribers: list = []

def home():
    return render_template('home.html')


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


def getStock(stock_sym: str):
    if stock_sym == None:
        # return render_template('stock.html')
        return render_template('stock.html')
    else:
        print(stock_sym)
        print(check_if_stock_symbol_exists(stock_sym))
        if not check_if_stock_symbol_exists(stock_sym):
            return render_template('stock.html', error="Stock symbol doesn't exists")

        data = get_stock_data(stock_sym)
        return render_template('stock.html', data=data)


def searchStock():
    if request.method == 'POST':
        req = request.form 
        if not req["stock"]:
            return redirect("/stock")
        
        return redirect(f'/stock/{req["stock"]}')
