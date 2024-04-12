from flask import Flask, render_template,redirect,request,jsonify
import mysql.connector
from flask_mail import Mail, Message
# Mail ,Flask are the actual libraries

# Gmail lets you send up to 500 emails per day using The Gmail SMTP server

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'damsostream.login@gmail.com'
app.config['MAIL_PASSWORD'] = 'DamsoStream@01'
app.config['MAIL_DEFAULT_SENDER'] = 'damsostream.login@gmail.com'
mail = Mail(app)

''' Considerations
When using the Gmail SMTP server:
The sending limit is 2,000 messages per day. Learn more about email sending limits.
Spam filters might reject or filter suspicious messages.
The fully qualified domain name of the SMTP service is smtp.gmail.com.
Configuration options include:
Port 25, 465, or 587
SSL and TLS protocols  ||| TLS is more secure than SSL so that means it more slower than ssl
Dynamic IP addresses

Setup steps :
On the device or in the app, for server address, enter smtp.gmail.com.
For Port, enter one of the following numbers:
For SSL, enter 465.
For TLS, enter 587.
For authentication, enter your complete Google Workspace email address
 (for example: your.name@solarmora.com) and password. 
 Make sure to sign in to the account before you use it with the device or app.
'''








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
        results = mycursor.fetchall()

        #Note : jsonify ensure that the message is sent in a format that JavaScript can understand. 
        # It converts the Python dictionary into a JSON object

        if len(results) > 0:        # <=> if results:
            if results[0][0] == email:
                # User already exists
                return jsonify({"usr_exist": "true"})
            else:
                # User doesn't exist
                return jsonify({"usr_exist": "false"})
        else:
            return jsonify({"usr_exist": "false"})

    else:
        # Handle invalid requests
        return jsonify({"error": "Invalid request method"})

        
#EndOf-Email-Exist-Error-Handler

#Insert data comming from the form :
@app.route('/SignUpInput',  methods=["POST"])
def SignUpInput():
    # Extract form data
    email = request.form.get("email")
    password = request.form.get("password")
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")

    #No need to check the data because it's already checked by the route /CheckEmail
    sql = "INSERT INTO Client (FirstName, LastName, Email, Password) VALUES (%s, %s, %s, %s)"
    data = (firstname, lastname, email, password)
    mycursor.execute(sql, data)
    myconnection.commit()  # Save
    return redirect(f'/Verify?email={email}')



#Verify the email : (so we can Eliminate invalid or spam emails from our list)
# /Verify rout below is for this job
@app.route('/Verify',methods=["GET"])
def Verify():
    email = request.args.get('email')
    return render_template("Login.html",email = email) 
#First we need to send the usr an email with the verification link
# For that we need to use Flask-Mail library for sending emails from our Flask application







# Login ----------------------------------------------------------------------------------


# Here i need to treat all posibilites and ForgotPwd case also: 

# x = 0 for the default  -----------------------------------------------------------------
@app.route('/Login', methods=["GET","POST"])
def Login():
    return render_template("Login.html",x = 0) 

# x = 1 for ForgotPWD --------------------------------------------------------------------
@app.route('/passwordForgot', methods=["POST"])
def passwordForgot():
    return render_template("Login.html",x = 1)

# x = 2 for Verify ----------------------------------------------------------------------





#Treat data comming from the login form :
    # Check if the user exist in data base else send a msg "Sorry,
    # looks like that’s the wrong email or password."

#Check the login : just like the route /CheckEmail
@app.route('/CheckLogin', methods=["POST"])
def CheckLogin():
    if request.method == "POST":
        email = request.json['email']
        passwd = request.json['passwd']
        sql = "SELECT Email,Password FROM CLIENT WHERE email = %s"
        data = (email,)
        mycursor.execute(sql, data)
        results = mycursor.fetchall()


        if len(results) > 0:        # <=> if results:
            if results[0][0] == email and results[0][1] == passwd:
                # User already exists
                return jsonify({"usr_exist": "true"})
            else:
                # User doesn't exist
                return jsonify({"usr_exist": "false"})
        else:
            return jsonify({"usr_exist": "false"})

    else:
        # Handle invalid requests
        return jsonify({"error": "Invalid request method"})





@app.route('/LoginInput',  methods=["POST"])
def LoginInput():
    #No need to Check the data because it's already checked by the route /CheckLogin
    return redirect('/home')

    











# ----------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
