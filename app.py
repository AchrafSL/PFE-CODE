from flask import Flask, render_template,redirect,request,jsonify,session
import mysql.connector
from flask_mail import Mail, Message
from datetime import timedelta # no need to download the lib
from datetime import datetime  #    
 


# Mail ,Flask are the actual libraries

# Gmail lets you send up to 500 emails per day using The Gmail SMTP server

app = Flask(__name__)

#Setup the session setting :
app.secret_key= "PFE_UIT_ACHRAF_CABREL"
#Data permanent time : 
# Session will be exipred automaticaly after 24h :
app.permanent_session_lifetime = timedelta(hours=24)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'damsostream.login@gmail.com'
app.config['MAIL_PASSWORD'] = 'oxdeudalmxpohfpt'
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









# LogIn and Signup part | ______________________________________________________________________________


# Signup ---------------------------------------------------------------------------------
@app.route('/Signup', methods=["GET","POST"])
def Signup():
    return render_template("Signup.html")

#Email-Exist-Error-Handler(Send a msg to the USER without reloading the page)
@app.route('/CheckEmail', methods=["POST"])
def CheckEmail():
    if request.method == "POST":
        # Need to check if the user already has an account (can't use the same email)
        email = request.json['email']
        email = email.lower()

        sql = "SELECT Email FROM USER WHERE email = %s"
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

    #The email should be case insensitive :
    email = email.lower()
    
    date = datetime.now()
    #No need to check the data because it's already checked by the route /CheckEmail
    sql = "INSERT INTO USER (FirstName, LastName, Email, Password,Date_Joined) VALUES (%s, %s, %s, %s, %s)"
    data = (firstname, lastname, email, password,date)
    mycursor.execute(sql, data)
    myconnection.commit()  # Save

    # generate a token with the operation code 50 for Email verification
    token = generate_verification_token(email, firstname,lastname, password,50)
    send_verification_email(email, token)

    return redirect(f'/Verify?email={email}')



#Verify the email : (so we can Eliminate invalid or spam emails from our list) -------------------

@app.route('/Verify',methods=["GET"])
def Verify():

    email = request.args.get('email')
    return render_template("Login.html",email = email) 

#I didnt find a simple algorithm so i made a simple one myself:
# I think i can generalise this token generator for also forgotPWD 
# the method is to add Operation arguments and it will be added to the sum like
# EmailVerification have a code for example(55) and forgotPWD (66) and will be added 

def generate_verification_token(email, firstname, lastname, password,operation):
    # Convert email to a number ord('A') -> code ascii (65)
    email_num = sum([ord(char) for char in email])
    # Convert password,firstname and lastname to numbers | create a list of ascii codes of the string
     # and sum the codes
    firstname_num = sum([ord(char) for char in firstname])
    lastname_num = sum([ord(char) for char in lastname])
    password_num = sum([ord(char) for char in password])
    token_num = int(( (email_num + firstname_num + lastname_num + password_num) * operation ) / 2)
    return token_num

#First we need to send the usr an email with the verification link
# For that we need to use Flask-Mail library for sending emails from our Flask application
def send_verification_email(email, token):
    msg = Message('Verify Your Email',sender='damsostream.login@gmail.com', recipients=[email])
    verification_link = f'http://127.0.0.1:5000/verify_email?token={token}&email={email}'
    #msg.body = f'Please click the following link to verify your email: {verification_link}'
    msg.html = render_template('Email_template.html',msg = 'email', verification_link=verification_link)
    mail.send(msg)


# Route for verifying-email | Operation code is :50
@app.route('/verify_email', methods=['GET'])
def verify_email():
    token = int(request.args.get('token')) 
    email = request.args.get('email')
    email = email.lower()
    #search for the usr  and generate the token and compare it with the token :
    sql = "SELECT Password,FirstName,LastName FROM USER WHERE email = %s"
    data = (email,)
    mycursor.execute(sql, data)
    results = mycursor.fetchall()
    Password = results[0][0]
    FirstName = results[0][1]
    LastName = results[0][2]

    # Verify the token by comparing it with the generated token for the email
    # because i dont want to save the token it will just take space

    new_token = generate_verification_token(email, FirstName, LastName, Password,50)
    if token == new_token:
        #now check if the email is verified or not
        sql = "SELECT status from USER WHERE Email = %s"
        data = (email,)
        mycursor.execute(sql, data)
        results = mycursor.fetchall()
        status = results[0][0]

        #if it's not verified | verify and go the done page
        if status != 'verified':
            # Change the USER status in the db :
            sql = "UPDATE USER SET status = 'verified' WHERE Email = %s"
            data = (email,)
            mycursor.execute(sql, data)
            myconnection.commit()  # Save
            return  redirect('/Verified_email')
        
        #if it's verified go to it's already verified page
        else:
            return  redirect('/Already_Verified_email')
        
    else:
        #return 'Invalid token'
        return render_template('Signup.html',verif = 1,invalidToken = 1)


@app.route('/Verified_email' , methods=["GET"])
def Verified_email():
    return render_template('Signup.html',verif = 0)

@app.route('/Already_Verified_email' , methods=["GET"])
def Already_Verified_email():
    return render_template('Signup.html',verif = 1)






# Login ----------------------------------------------------------------------------------
# Here i need to treat all posibilites and ForgotPwd case also: 

# x = 0 for the default  -----------------------------------------------------------------
@app.route('/Login', methods=["GET","POST"])
def Login():
    return render_template("Login.html",x = 0) 

# x = 1 for ForgotPWD --------------------------------------------------------------------
@app.route('/passwordForgot', methods=["POST","GET"])
def passwordForgot():
    return render_template("Login.html",x = 1,Reset=0)

# x = 2 for Verify ----------------------------------------------------------------------


#Treat data comming from the login form :
    # Check if the user exist in data base else send a msg "Sorry,
    # looks like that’s the wrong email or password."

#Check the login : just like the route /CheckEmail
@app.route('/CheckLogin', methods=["POST"])
def CheckLogin():
    if request.method == "POST":
        email = request.json['email']
        email = email.lower()
        passwd = request.json['passwd']
        sql = "SELECT Email,Password,FirstName,LastName,role,idCli,Date_Joined FROM USER WHERE email = %s"
        data = (email,)
        mycursor.execute(sql, data)
        results = mycursor.fetchall()



        if len(results) > 0:        # <=> if results:
            if results[0][0] == email and results[0][1] == passwd:
                # User already exists

                #Save the data in the session :
                # this session will be permanent for the time we setup in the top :
                session.permanent = False
                session["logged_in"] = True
                session["FirstName"] = results[0][2]
                session["LastName"] = results[0][3]
                session["Email"] = results[0][0]
                session["role"] = results[0][4]
                session["idCli"] = results[0][5]

                default_date = results[0][6]
                new_date = default_date.strftime("%Y-%m-%d %H:%M:%S")

                session["Date_Joined"] = new_date
                #End of session setup

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

    

# ForgotPwd verification part to do not let the usr abuse the system and spam 
# and check if the email exist or not !

# Route for verifying-email | Operation code is :60
# 127.0.0.1 - - [13/Apr/2024 20:10:05] "GET /ResetPassword HTTP/1.1" 405 -
# I always get a "GET" request but i dont know where it's coming from 

#Here is the page that apear after clicking forgotPWD:
@app.route('/ResetPassword',methods=["POST","GET"])
def ResetPassword():
    if request.method == "POST":
        email =  request.form.get("E_mail")
    else:
        email = request.args.get("E_mail")
    email = email.lower()
    #if the email exist send an email to the usr 
    sql = "SELECT Email,Password,firstname,lastname FROM USER WHERE email = %s"
    data = (email,)
    mycursor.execute(sql, data)
    results = mycursor.fetchall()

    if len(results) > 0:
        E_mail = results[0][0]
        password = results[0][1]
        firstname = results[0][2]
        lastname = results[0][3]

        #if it's true then the email exist
        if (email == E_mail):
            # generate token
            token = generate_verification_token(email, firstname, lastname, password,60)
            #then send the email
            send_verification_password(email, token)

            #Page tha says to the usr that the email is sent !
            return render_template('Login.html',x = 1,Reset= 1,email = email)

    #The email doesn't exist the go the doesn't exist page :
    return render_template('Signup.html',verif = 1,Reset = -1)

#This is the page that apear after the usr recive the link in the email
#it's a form to fill and send it
@app.route('/ResetPassword_Page',methods=["GET"])
def ResetPassword_Page():
    #Verify the token:

    token = int(request.args.get('token')) 
    email = request.args.get('email')
    email = email.lower()

    #search for the usr  and generate the token and compare it with the token :
    sql = "SELECT Password,FirstName,LastName FROM USER WHERE email = %s"
    data = (email,)
    mycursor.execute(sql, data)
    results = mycursor.fetchall()
    Password = results[0][0]
    FirstName = results[0][1]
    LastName = results[0][2]

    # Verify the token by comparing it with the generated token for the email
    # because i dont want to save the token it will just take space

    new_token = generate_verification_token(email, FirstName, LastName, Password,60)
    if token == new_token:
    #if the token match -> load the page where the from exist
    # load the page with a arg = email ;
    # the email will be in an invis input in the form that will be sent with the reset pwd ;
        return render_template('login.html',reset_form = 1,email = email)

    #if the token doesn't match then 
    #return 'token is not valid'
    return render_template('Signup.html',verif = 1,invalidToken = 2)



#Check if the new Password is already the same as the one in the db :
@app.route('/CheckPassword', methods=["POST"])
def CheckPassword():
    if request.method == "POST":
        email = request.json['email']
        password = request.json['passwd']
        sql = "SELECT Password FROM USER WHERE email = %s"
        data = (email,)
        mycursor.execute(sql, data)
        results = mycursor.fetchall()

        #Note : jsonify ensure that the message is sent in a format that JavaScript can understand. 
        # It converts the Python dictionary into a JSON object

        if len(results) > 0:        # <=> if results:
            if results[0][0] == password:
                # password already exists
                return jsonify({"pswd_exist": "true"})
            else:
                # password doesn't exist
                return jsonify({"pswd_exist": "false"})
        else:
            return jsonify({"pswd_exist": "false"})

    else:
        # Handle invalid requests
        return jsonify({"error": "Invalid request method"})



#this route will be triggered from the from sent when the (token == new_token )
@app.route('/ResetPassword_Apply', methods=["POST"])
def ResetPassword_Apply():
    email = request.form.get('Email')
    New_Password = request.form.get('Password')
    # Change the USER password in the db :
    sql = "UPDATE USER SET Password = %s WHERE Email = %s"
    data = (New_Password,email)
    mycursor.execute(sql, data)
    myconnection.commit()  # Save

    #load the done page after changing the mdp
    return render_template('Signup.html',verif = 0,apply = 1)



def send_verification_password(email, token):
    msg = Message('Reset Your Password',sender='damsostream.login@gmail.com', recipients=[email])
    verification_link = f'http://127.0.0.1:5000/ResetPassword_Page?token={token}&email={email}'
    #msg.body = f'Please click the following link to Reset your password: {verification_link}'
    msg.html = render_template('Email_template.html',msg = 'password', verification_link=verification_link)
    mail.send(msg)



#Resend link 
@app.route('/ResendLink', methods=["POST"])
def ResendLink():
    email = request.form.get('EMAIL')
    ResendLink_Type = request.form.get('ResendLink_Type')
    sql = "SELECT Password,FirstName,LastName FROM USER WHERE email = %s"
    data = (email,)
    mycursor.execute(sql, data)
    results = mycursor.fetchall()
    Password = results[0][0]
    FirstName = results[0][1]
    LastName = results[0][2]
    if ResendLink_Type == 'email':
        #operation code is 50 (email verification)
        token = generate_verification_token(email, FirstName, LastName, Password,50)
        #I have to add some restrictions to this button because the usr can spam it 
        send_verification_email(email,token)
        return redirect(f'/Verify?email={email}')
    else:
        token = generate_verification_token(email, FirstName, LastName , Password ,60)
        send_verification_password(email,token)
        return redirect(f'/ResetPassword?E_mail={email}')


##What will happen after the login |-------------------------------------------------------------
@app.route("/USER_Page", methods=["GET"])
def USER_Page():
    if (session.get("logged_in") == True):
        return render_template("USER_Page.html")
    else:
        # if the user is not logged_in he will be redirected to the home page :
        return redirect("/home")    

        

#__________________________________________________________________________________________________







# ----------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
