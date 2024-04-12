from flask import Flask, render_template,redirect,request,jsonify
import mysql.connector


app = Flask(__name__)

#SetUp the connection between Python and MySql :
# the cursor object to perform db operations:
myconnection = mysql.connector.connect(
    host = "127.0.0.1",     # localhost or 127.0.0.1 ;
    user = "root" ,     #mysql usr name;
    passwd = "Salimi@01" ,      #mysql passwd;
    database="DamsoStreamDB"        # Name of the database you want to connect to
)
mycursor = myconnection.cursor()  

# TO PREVENT SQL INJECTION WHEN THE QUERY VALUES ARE PROVIDED BY THE USER :
# the methode given by mysql.connector to escape the values is %s in sql = ' ........ %s'
# and the values are in data = ....

# COMMANDS : ------------------------------------------------------------------------

# mycursor.execute("Query in SQL") results of this cmd stored in mycursor
# mycursor.execute(sql,data) | sql is a string that contain the sql query 
# mycursor.executemany(sql,data) | if data is a list we use this cmd
# mycursor.rowcount  | mycursor.lastrowid 
# myconnection.commit() if you edit in the data base you need to save changes ;
# mycursor.fetchall() return the rows as lists [(row1),...,(rowN)] and rows may have lot of columns
# mycursor.fetchone() return only the first row 

# ------------------------------------------------------------------------------------




#Home --------------------------------------------------------------------------------------
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


# Cart  ----------------------------------------------------------------------------------
@app.route('/Cart', methods=["GET"])
def Cart():
    return render_template("Cart.html")

# Signup ---------------------------------------------------------------------------------
@app.route('/Signup', methods=["GET"])
def Signup():
    return render_template("Signup.html")

#Email-Exist-Error-Handler(Send a msg to the client without reloading the page)
@app.route('/CheckEmail', methods=["POST"])
def CheckEmail():
    if request.method == "POST":
        # Need to check if the user already has an account (can't use the same email)
        email = request.json['email']
        sql = "SELECT Email FROM CLIENT WHERE email = %s"
        data = (email,)
        mycursor.execute(sql, data)
        results = mycursor.fetchone()

        if results is not None and results[0] == email:
            # User already exists
            return jsonify({"usr_exist": "true"})
        else:
            # User doesn't exist
            return jsonify({"usr_exist": "false"})
        
#EndOf-Email-Exist-Error-Handler

@app.route('/SignUpInput',  methods=["POST"])
def SignUpInput():
    #Insert data because it's already checked using '/CheckEmail' route and Singup.js
    email = request.form.get("email")
    password = request.form.get("password")
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")

    sql1 = "INSERT INTO Client (FirstName, LastName, Email,Password) VALUES (%s,%s,%s,%s)"
    data1 = (firstname,lastname,email,password)
    mycursor.execute(sql1,data1)
    myconnection.commit()  # Save
    return redirect("/Signup")   






# Login ----------------------------------------------------------------------------------


# Here i need to treat all posibilites and ForgotPwd case also: 

# x = 0 for the default  -----------------------------------------------------------------
@app.route('/Login', methods=["GET"])
def Login():
    return render_template("Login.html",x = 0) 

# x = 1 for ForgotPWD --------------------------------------------------------------------
@app.route('/passwordForgot', methods=["POST"])
def passwordForgot():
    return render_template("Login.html",x = 1)

# ----------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
