from flask import Flask, render_template,redirect

app = Flask(__name__)

#Home
@app.route('/home', methods=["GET"])
@app.route('/', methods=["GET"])
def home():
    return render_template("Home.html")

# Offers
@app.route('/Offers', methods=["GET"])
def Offers():
    return render_template("Offers.html")

# ContactUS
@app.route('/ContactUS', methods=["GET"])
def ContactUS():
    return render_template("ContactUS.html")

# FeedBacks
@app.route('/FeedBacks', methods=["GET"])
def FeedBacks():
    return render_template("FeedBacks.html")

# AboutUS
@app.route('/AboutUs', methods=["GET"])
def AboutUS():
    return render_template("AboutUs.html")

# Cart
@app.route('/Cart', methods=["GET"])
def Cart():
    return render_template("Cart.html")

# Signup
@app.route('/Signup', methods=["GET"])
def Signup():
    return render_template("Signup.html")

# Login
@app.route('/Login', methods=["GET"])
def Login():
    return render_template("Login.html")



if __name__ == '__main__':
    app.run(debug=True)
