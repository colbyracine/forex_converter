from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates



app = Flask(__name__)

app.config["SECRET KEY"] = "z1x2c3d6s5a4q7w8e9"
c = CurrencyRates()

@app.route("/")
def get_home_page():
# render homepage
    return render_template("index.html")


@app.route("/forex-converter")
# show forex convereter form
def converter_page():

    return render_template("/forex-converter.html")


@app.route("/handle-form-forex")
#get data from form to convert
def handle_form():
    

    currfrom = request.args.get("currfrom")
    currto = request.args.get("currto")
    amount = request.args.get("amount")

    

    res = c.convert(currfrom, currto, float(amount))
    rate = c.get_rate(currfrom, currto)

    return render_template("/response-forex.html", res=res, currto=currto, currfrom=currfrom, amount=amount, rate=rate)