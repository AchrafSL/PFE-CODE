from flask import Flask, render_template,redirect,request,jsonify,session,url_for
import mysql.connector
from flask_mail import Mail, Message
from datetime import timedelta,datetime # no need to download the lib
import phonenumbers


# Mail ,Flask are the actual libraries

#Upload files : (Source - flask Documentation:
# https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/)

from werkzeug.utils import secure_filename   

# Avoiding Execution of Malicious Files: Malicious users might upload files with executable extensions
# like .php, .exe, etc., hoping to execute them on your server. By using secure_filename,
# you can rename such files to have non-executable extensions or take other preventive measures to
# ensure they can't be executed inadvertently.

import os

UPLOAD_FOLDER = 'static\\Images\\Users_pfp'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Setup the session setting :
app.secret_key= os.getenv("SECRET_KEY")
#Data permanent time : 
# Session will be exipred automaticaly after 24h :
app.permanent_session_lifetime = timedelta(hours=24)

# Configure Flask-Mail

# Email account used for verification
app.config['MAIL_USERNAME_VERIFICATION'] = os.getenv("MAIL_USERNAME_VERIFICATION")
app.config['MAIL_PASSWORD_VERIFICATION'] = os.getenv("MAIL_PASSWORD_VERIFICATION")
app.config['MAIL_DEFAULT_SENDER_VERIFICATION'] = os.getenv("MAIL_DEFAULT_SENDER_VERIFICATION")

# Email account used for sending contact us messages
app.config['MAIL_USERNAME_CONTACT'] = os.getenv("MAIL_USERNAME_CONTACT")
app.config['MAIL_PASSWORD_CONTACT'] = os.getenv("MAIL_PASSWORD_CONTACT")
app.config['MAIL_DEFAULT_SENDER_CONTACT'] = os.getenv("MAIL_DEFAULT_SENDER_CONTACT")


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_DEFAULT_SENDER")
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
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT")),
)
mycursor = myconnection.cursor()
# TO PREVENT SQL INJECTION WHEN THE QUERY VALUES ARE PROVIDED BY THE user :
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
@app.route('/home', methods=["GET","POST"])
@app.route('/', methods=["GET","POST"])
def home():
    return render_template("Home.html")

# Offers ---------------------------------------------------------------------------------
@app.route('/Offers', methods=["GET","POST"])
def Offers():
    #the number of offers
    mycursor.execute("SELECT COUNT(*) AS OffersNumber FROM offers;")
    results = mycursor.fetchall()

    # Search for an offer :
    word = request.args.get('product')
    if word is not None:
        sql = "SELECT name, Offer_price,idOffer,image_Name FROM offers WHERE name LIKE %s"
        data = ("%" + word + "%",)  
        mycursor.execute(sql, data)
        offer_result = mycursor.fetchall()
    else:
        mycursor.execute("SELECT name, Offer_price,idOffer,image_Name FROM offers;")
        offer_result = mycursor.fetchall()

    offer_data = []
    for row in offer_result:
        offer = {'name': row[0], 'price': row[1],'idOffer':row[2],'image_Name':row[3]}
        offer_data.append(offer) #add the offer to the end of the list offer_data

    # Zip the range and offer data
    offer_data = zip(range(results[0][0]), offer_data)

    return render_template("Offers.html" , OffersNumber = results[0][0] , OfferData = offer_data ,word = word )

#Product_Description --------------------------------------------------------------------------------
@app.route("/Product_Description", methods=["GET"])
def Product_Description():
    id = request.args.get('productId')
    sql = "SELECT * FROM offers where idOffer = %s"
    data = (id,)

    mycursor.execute(sql,data)
    results = mycursor.fetchall()
    offer_data = {'productId': results[0][0], 'description': results[0][1],'image_Name':results[0][2]
                  ,'Offer_price':results[0][3] ,'name': results[0][4]}
                  

    # Load comment data : (show the top 100 only)
    sql = "SELECT idCli, comment_TEXT, Date_written,idComment FROM comment WHERE idOffer = %s ORDER BY Date_written DESC LIMIT 100;"
    data = (id,)
    mycursor.execute(sql,data)
    results = mycursor.fetchall()

    comments_data = []
    for res in results:
        sql = "SELECT LastName, FirstName,pfpName FROM user WHERE idCli = %s;"
        user_data = (res[0],) 
        mycursor.execute(sql, user_data)
        Usr_Data = mycursor.fetchone()

        comment_data = {
            'idCli' : res[0],
            'LastName': Usr_Data[0],
            'FirstName': Usr_Data[1],
            'comment': res[1],
            'Date_written': res[2],
            'idComment':res[3],
            'pfpName':Usr_Data[2]
        }

        comments_data.append(comment_data)
        
    return render_template("Product_Description.html", offer=offer_data, comments=comments_data)


#Comment section 
@app.route("/submit_comment", methods=["POST"])
def submit_comment():
    productId = request.form.get("productId")
    idCli = session["idCli"]
    comment = request.form.get("comment")
    date = datetime.now()



    #Insert a comment :
    sql = "INSERT INTO comment (idOffer, idCli,comment_TEXT,Date_written ) VALUES (%s, %s, %s, %s);"
    data = (productId,idCli,comment,date)
    mycursor.execute(sql,data)
    myconnection.commit()


    return redirect(url_for("Product_Description",productId = productId))



#Delete comment 
@app.route('/DeleteComment', methods=["POST"])
def DeleteComment():
    productId = request.form.get("productId")
    idComment = request.form.get("idComment")

    sql = "DELETE FROM COMMENT WHERE idComment = %s"
    data = (idComment,)
    mycursor.execute(sql,data)
    myconnection.commit()

    return redirect(url_for("Product_Description",productId = productId))










# ContactUS ------------------------------------------------------------------------------
@app.route('/ContactUS', methods=["GET"])
def ContactUS():
    return render_template("ContactUS.html")

@app.route("/ConstactUSFormEmailSend", methods=["POST"])
def ConstactUSFormEmailSend():
    senderName = request.form.get("ContactUSName")
    senderEmail = request.form.get("ContactUSEmail")
    senderMSG = request.form.get("ContactUSMSG")
    email = "damsostream@gmail.com"

    # Contact us email config
    app.config['MAIL_USERNAME'] = app.config['MAIL_USERNAME_CONTACT']
    app.config['MAIL_PASSWORD'] = app.config['MAIL_PASSWORD_CONTACT']
    app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_DEFAULT_SENDER_CONTACT']
    mail.init_app(app)

    msg = Message(senderName + ' Contact request', sender="DamsoStream.ContactUS@gmail.com", recipients=[email])
    msg.body = senderMSG
    # A solution for sending an email using user email (because we can't do that)
    msg.reply_to = senderEmail
    mail.send(msg)

    # Reconfigure Flask-Mail for verification email
    app.config['MAIL_USERNAME'] = app.config['MAIL_USERNAME_VERIFICATION']
    app.config['MAIL_PASSWORD'] = app.config['MAIL_PASSWORD_VERIFICATION']
    app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_DEFAULT_SENDER_VERIFICATION']
    mail.init_app(app)








    return redirect("ContactUS")
# AboutUS --------------------------------------------------------------------------------
@app.route('/AboutUs', methods=["GET"])
def AboutUS():
    return render_template("AboutUs.html")


# Cart  ----------------------------------------------------------------------------------

#Add Offers to the cart :
@app.route('/AddOfferToCart', methods=["POST"])
def AddOfferToCart():

    if session['role'] == 'employee' :
        return redirect('home')

    idOffer = request.form.get('idOffer')   
    sql = "SELECT idCart FROM cart WHERE idCli = %s"
    data = (session["idCli"],)
    mycursor.execute(sql,data)
    results = mycursor.fetchall()


    idCart = results[0][0]

    #Only add offer if it doesn't exist in the cartoffers :
    sql = "SELECT idCart FROM cartoffers WHERE idCart = %s AND idOffer = %s"
    data = (idCart, idOffer,)
    mycursor.execute(sql, data)
    results = mycursor.fetchall()

    # If the offer doesn't exist in CARTOFFERS, insert it
    if not results:
        sql = "INSERT INTO cartoffers (idCart, idOffer) VALUES (%s, %s)"
        data = (idCart, idOffer,) 
        mycursor.execute(sql, data)
        myconnection.commit()

    return redirect("/Cart")





@app.route('/Cart', methods=["GET","POST"])
def Cart():
    if 'logged_in' not in session:
        return redirect('/Login')
    
    if 'role' not in session:
        return redirect('/Login')

    if session['role'] == 'employee' :
        return redirect('home')

    #get idCart : (using idCli)
    sql = "SELECT idCart from cart where idCli = %s"
    data = (session["idCli"],)
    mycursor.execute(sql,data)
    results = mycursor.fetchall()

    idCart = results[0][0]

    #Save idCart in a session 
    session["idCart"] = idCart

    
    #Calculat full price; (also il faut cree une jointure entre les deux tab cartOffers and Offers)
    sql = "SELECT SUM(O.Offer_price) AS total_price FROM cartoffers CO, offers O WHERE CO.idOffer = O.idOffer AND CO.idCart = %s "
    data = (idCart,)
    mycursor.execute(sql,data)
    results = mycursor.fetchall()
    fullprice = results[0][0]
    session["fullprice"] = fullprice


    #Insert full price in cart table :
    sql = "UPDATE cart SET fullprice = %s where idCart = %s"
    data = (fullprice,idCart,)
    mycursor.execute(sql,data)
    myconnection.commit()




    #get all offers (data) stored :(il faut faire une jointure entre les tableau (offers et offerCart)
    sql = "SELECT CO.idOffer,O.description, O.image_Name, O.Offer_price, O.name AS total_price FROM cartoffers CO, offers O WHERE CO.idOffer = O.idOffer AND idCart = %s"
    data = (idCart,)
    mycursor.execute(sql,data)
    OfferSresults = mycursor.fetchall()

    
    # all the offers of the current user cart is stored in results now ;
    offers_data = []
    for row in OfferSresults:
        offer = {
            'idOffer': row[0],
            'description': row[1],
            'image_Name': row[2],
            'Offer_price': row[3],
            'name': row[4]} 
        offers_data.append(offer) #add the offer to the end of the list offer_data


    return render_template("Cart.html", OFFERData = offers_data)

# Remove offers from the cart : 
@app.route('/RemoveOffer_Cart', methods=["POST"])
def RemoveOffer_Cart():
    idOffer = request.form.get('offerId')
    idCart = session["idCart"]

    # Delete row where idCart = %s and idOffer = %s

    sql = "DELETE FROM cartoffers WHERE idCart = %s AND idOffer = %s"
    data = (idCart,idOffer,)
    mycursor.execute(sql,data)
    myconnection.commit()

    #Insert full price in cart table :
    sql = "UPDATE cart SET fullprice = %s where idCart = null"
    data = (idCart,)
    mycursor.execute(sql,data)
    myconnection.commit()



    return redirect("/Cart")



#Send Order
@app.route("/SendOrder", methods = ["POST"])
def SendOrder():
    #Save the order and Offers  in Order and OrderOffers
        #Get cart id that corespond to the current usr :
    idCart = session["idCart"]

    # Check if the cart is empty or not (aka checking if cartoffer is empty )
    #Check if there is smth in the cartOffer corponding to the current cart :
    sql = "SELECT (idOffer) FROM cartoffers WHERE idCart = %s"
    data = (idCart,)
    mycursor.execute(sql,data,)
    results = mycursor.fetchall()
    
    if not results:
        return redirect("Offers")


    #fill order data :
    sql = "INSERT INTO orders (idCli,TotalPrice) VALUES (%s,%s)"
    data = (session["idCli"],session["fullprice"],)
    mycursor.execute(sql,data)
    myconnection.commit()

    #order id :
    idOrder = mycursor.lastrowid

    #fill orderOffers :
        #Get the data from CartOffers
    sql = "SELECT idOffer from cartoffers Where idCart = %s"
    data = (idCart,)
    mycursor.execute(sql,data)
    results = mycursor.fetchall()

    for id in results:
        #Insert data in orderOffers under the same idOrder
        sql = "INSERT INTO orderoffers (idOrder,idOffer) VALUES (%s,%s)"
        data = (idOrder,id[0],)
        mycursor.execute(sql,data)
        myconnection.commit()



    #Clear all cart data for the current user in the CartOffers
    sql = "DELETE FROM cartoffers WHERE idCart = %s"
    data = (idCart,)
    mycursor.execute(sql,data)
    myconnection.commit()
    return redirect("home")







# LogIn and Signup part | ______________________________________________________________________________


# Signup ---------------------------------------------------------------------------------

def format_whatsapp_number(number, country_code):

    # Check if the number already starts with a +
    if number.startswith('+'):
        # Parse the existing full number
        parsed_number = phonenumbers.parse(number)
        # Extract the national significant number (without country code)
        national_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        # Remove non-digit characters and leading zeros from the national number
        national_number = ''.join(filter(str.isdigit, national_number)).lstrip('0')
    else:
        # If there's no +, assume it's just a national number and remove leading zeros
        national_number = number.lstrip('0')

    # Combine the new country code with the national number
    full_number = f"+{country_code}{national_number}"
    
    parsed_number = phonenumbers.parse(full_number)
    return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)





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

        sql = "SELECT Email FROM user WHERE email = %s"
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
    whatsapp = request.form.get("WhatsappNumber")
    countryCode = request.form.get("countryCode")

    if whatsapp != '':
        whatsapp = format_whatsapp_number(whatsapp,countryCode)


    #The email should be case insensitive :
    email = email.lower()
    
    date = datetime.now()
    #No need to check the data because it's already checked by the route /CheckEmail
    sql = "INSERT INTO user (FirstName, LastName, Email, Password,Date_Joined,whatsapp) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (firstname, lastname, email, password,date,whatsapp)
    mycursor.execute(sql, data)
    myconnection.commit()  # Save

    idCli = mycursor.lastrowid
    
    # CART link with the user id
    sql = "INSERT INTO cart (idCli) VALUES (%s)" 
    data = (idCli,)
    mycursor.execute(sql, data)
    myconnection.commit()

    # generate a token with the operation code 50 for Email verification
    token = generate_verification_token(email, firstname,lastname, password,50)
    send_verification_email(email, token)

    return redirect(f'/Verify?email={email}')



#Verify the email : (so we can Eliminate invalid or spam emails from our list) -------------------

#Page showing to the usr that we sent an email to them and give them the choice to resend the link
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
    sql = "SELECT Password,FirstName,LastName FROM user WHERE email = %s"
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
        sql = "SELECT status from user WHERE Email = %s"
        data = (email,)
        mycursor.execute(sql, data)
        results = mycursor.fetchall()
        status = results[0][0]

        #if it's not verified | verify and go the done page
        if status != 'verified':
            # Change the USER status in the db :
            sql = "UPDATE user SET status = 'verified' WHERE Email = %s"
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

        sql = "SELECT Email,Password,FirstName,LastName,role,idCli,Date_Joined,whatsapp,pfpName FROM user WHERE email = %s"
        data = (email,)
        mycursor.execute(sql, data)
        results = mycursor.fetchall()



        if len(results) > 0:        # <=> if results:
            if results[0][0] == email and results[0][1] == passwd:
                # User already exists

                #Save the data in the session :
                session.permanent = True
                session["logged_in"] = True
                session["FirstName"] = results[0][2]
                session["LastName"] = results[0][3]
                session["Email"] = results[0][0]
                session["role"] = results[0][4]
                session["idCli"] = results[0][5]
                session["whatsapp"] = results[0][7]
                session["pfpName"] = results[0][8]


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

#Here is the page that apear after clicking forgotPWD:
@app.route('/ResetPassword',methods=["POST","GET"])
def ResetPassword():
    if request.method == "POST":
        email =  request.form.get("E_mail")
    else:
        email = request.args.get("E_mail")
        
    email = email.lower()
    #if the email exist send an email to the usr 
    sql = "SELECT Email,Password,firstname,lastname FROM user WHERE email = %s"
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

            #Page that says to the usr that the email is sent !
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
    sql = "SELECT Password,FirstName,LastName FROM user WHERE email = %s"
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
        sql = "SELECT Password FROM user WHERE email = %s"
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
    sql = "UPDATE user SET Password = %s WHERE Email = %s"
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
    sql = "SELECT Password,FirstName,LastName FROM user WHERE email = %s"
    data = (email,)
    mycursor.execute(sql, data)
    results = mycursor.fetchall()
    Password = results[0][0]
    FirstName = results[0][1]
    LastName = results[0][2]

    if ResendLink_Type == 'email':
        #operation code is 50 (email verification)
        token = generate_verification_token(email, FirstName, LastName, Password,50)
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

        

#___________________________________________________________________________________________________



#UserPage ___________________________________________________________________________________________


#Update User_Info: ----------------------------------------------------------------------------------
@app.route("/UpdateInfo", methods=["POST"])
def UpdateInfo():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    whatsapp = request.form.get('whatsappNumber')
    email = request.form.get('email')
    email = email.lower()
    
    if (whatsapp != ""):
        countryCode = request.form.get("CountryCode")
        whatsapp = format_whatsapp_number(whatsapp, countryCode)

    

    # if the email is changed verify the email :
    if(email != session["Email"]):

        #Change the status in the data base to unverified :
        sql = "UPDATE user SET status = 'unverified' WHERE Email = %s"
        data = (session["Email"],)
        mycursor.execute(sql,data)
        myconnection.commit()  # Save

        sql = "SELECT Password from user where Email = %s"
        data = (session["Email"],)
        mycursor.execute(sql,data)
        results = mycursor.fetchall()

        # update all :
        sql = "UPDATE user SET FirstName = %s,LastName= %s,whatsapp = %s,Email = %s WHERE Email = %s"
        data = (firstname,lastname,whatsapp,email,session["Email"],)
        mycursor.execute(sql,data)
        myconnection.commit()  # Save


        # Update session data and go verify email:
        session["FirstName"] = firstname
        session["LastName"] = lastname
        session["Email"] = email
        session["whatsapp"] = whatsapp 

        # generate a token with the operation code 50 for Email verification
        token = generate_verification_token(email, firstname,lastname,results[0][0],50)
        send_verification_email(email, token)

        return redirect(f'/Verify?email={email}')
    else:
        # update all :
        sql = "UPDATE user SET FirstName = %s,LastName= %s,whatsapp = %s,Email = %s WHERE Email = %s"
        data = (firstname,lastname,whatsapp,email,session["Email"],)
        mycursor.execute(sql,data)
        myconnection.commit()  # Save

    # Update session data :
    session["FirstName"] = firstname
    session["LastName"] = lastname
    session["whatsapp"] = whatsapp 
    return redirect('/USER_Page')

#logOut -----------------------------------------------------------------------------------------
@app.route("/logout" , methods=["POST","GET"])
def logout():
    session["logged_in"] = False
    session.pop("FirstName",None)
    session.pop("LastName",None)
    session.pop("Email",None)
    session.pop("role",None)
    session.pop("idCli",None)
    session.pop("whatsapp",None)
    session.pop("pfpName",None)
    session.pop("idCart",None)
    session.pop("fullprice",None)
    session.pop("ListOrders", None)
    session.pop("OrderNumber", None)
    session.pop("NumbSignup", None)
    session.pop("Revenue", None)
    return redirect("/home")


#DeleteAccount -----------------------------------------------------------------------------------
@app.route("/DeleteAccount" , methods=["POST"])
def DeleteAccount():
    sql = "DELETE FROM user WHERE Email = %s"
    data = (session["Email"],)
    mycursor.execute(sql,data)
    myconnection.commit()  # Save

    return redirect("/logout")


#UploadPFP ------------------------------------------------------------------------------------------
@app.route("/UploadPFP", methods=["POST","GET"])
def UploadPFP():
    profile_pic = request.files["file"]

    # change the name of the img to : email+Firstname.smth | ofc the data is of the current usr ;
    pic_filename = secure_filename(profile_pic.filename)
    file_Extention = pic_filename.rsplit('.', 1)[1].lower()
    #.rsplit('.', 1): This splits the filename into two parts using the dot (.) as the separator 
    #. The rsplit() method starts splitting from the right side (end) of the string.
    # The 1 as the second argument tells Python to split the string only once, 
    #and it will split at the last occurrence of the dot (.). This means the filename and its extension 
    # Are separated.| [1]: This accesses the second part of the resulting list after splitting
    UPLOAD_FOLDER = 'static\\Images\\Users_pfp'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    pic_name = f"{session["Email"]}_{session["FirstName"]}.{file_Extention}" 
    # If the current usr img name != user583abc_1649114257.png delete the old img saved in the session
    if session["pfpName"] != "user583abc_1649114257.png":
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'],session["pfpName"]))



    #Update session pfp name;
    session["pfpName"] = pic_name

    #Update data base pfp name of the current usr;
    sql = "UPDATE user SET pfpName = %s WHERE Email = %s"
    data = (session["pfpName"],session["Email"],)
    mycursor.execute(sql,data)
    myconnection.commit()

    #upload the pfp in the pfp folder
    profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER'],pic_name))

    return redirect("/home")







# Activity Page (Client Page, Employee Page, Admin Page) ---------------------------------------------

@app.route("/Activity_Page", methods=["POST","GET"])
def Activity_Page():
    if session["role"] == "client":
                #Count the non (treated/payed) orders
        sql = "select count(*) from orders where  StatOfTreatment = 'Pending Treatment' AND PaymentStat = 'Pending Payment' AND idCli = %s"
        data = (session['idCli'],)
        mycursor.execute(sql,data)
        resu = mycursor.fetchall()
        OrderNumber = resu[0][0]



            #Select the orders :
        sql = "SELECT idOrder,StatOfTreatment,PaymentStat,TotalPrice FROM orders WHERE idCli = %s AND StatOfTreatment = 'Pending Treatment' AND PaymentStat = 'Pending Payment' "
        data = (session["idCli"],)
        mycursor.execute(sql,data)
        Orders = mycursor.fetchall()

        #send the client orders and subscriptions
        ListOrders = []
        for order in Orders:
            ordVar = {
                'idOrder': order[0],
                'StatOfTreatment': order[1],
                'PaymentStat': order[2],
                'TotalPrice': order[3],
                'offers': []
            }

            #For each order get offers names
            sql = "SELECT O.name FROM orderoffers OO, offers O WHERE OO.idOffer = O.idOffer AND OO.idOrder = %s"
            data = (order[0],)
            mycursor.execute(sql,data)
            OffersNames = mycursor.fetchall()

            for OfferName in OffersNames :
                ordVar['offers'].append(OfferName[0])

            ListOrders.append(ordVar)

        #My subscriptions Part :
                        #Count the (Active) subscription :
        sql = "select count(*) from subscription WHERE subscriptionStatus = 'Active' AND idCli = %s"
        data = (session['idCli'],)
        mycursor.execute(sql,data)
        resu = mycursor.fetchall()
        ActiveSubNumber = resu[0][0]

        # jointure entre subscription and offer
        sql = "select S.idSubscription,S.idOffer,S.subscriptionStatus,S.StartDate,S.endDate,O.name from subscription S,offers O WHERE S.idOffer = O.idOffer AND idCli = %s ORDER BY subscriptionStatus ASC"
        data = (session['idCli'],)
        mycursor.execute(sql,data)
        Subs = mycursor.fetchall()

        #Check if endDate <= current date else change sub status to inActive
        currentDate = datetime.now().date()
        for sub in Subs:
            endDate = sub[4]
            if endDate < currentDate :
                sql = "UPDATE subscription SET subscriptionStatus = 'Inactive' WHERE idSubscription = %s"
                data = (sub[0],)  
                mycursor.execute(sql, data)
                myconnection.commit()


        ListOfSubs = []
        for sub in Subs:
            subInfo = {
                'idSubscription': sub[0],
                'idOffer': sub[1],
                'subscriptionStatus': sub[2],
                'StartDate': sub[3], 
                'EndDate': sub[4], 
                'OfferName': sub[5]
            }
            ListOfSubs.append(subInfo)

 
        return render_template("Activity_Page.html",USR = "client" ,ListOrders = ListOrders,OrderNumber = OrderNumber,ActiveSubNumber = ActiveSubNumber,ListOfSubs = ListOfSubs)
    
    
    elif session["role"] == "employee" or session["role"] == "admin":

        #Count the non (treated/payed) orders
        mycursor.execute("select count(*) from orders where  StatOfTreatment = 'Pending Treatment' AND PaymentStat = 'Pending Payment'")
        resu = mycursor.fetchall()
        OrderNumber = resu[0][0]




        #Send all non treated Orders

                    #Select all the non (treated/payed) orders with there client (info also):
        sql = " SELECT o.idOrder,o.StatOfTreatment, o.PaymentStat, o.TotalPrice,o.idCli, usr.FirstName,usr.LastName, usr.Email, usr.WhatsApp FROM orders o, user usr WHERE o.idCli = usr.idCli AND o.StatOfTreatment = 'Pending Treatment' AND PaymentStat = 'Pending Payment' ;"
        mycursor.execute(sql)
        Orders = mycursor.fetchall()

        #send the clients orders and subscriptions
        ListOrders = []
        for order in Orders:
            ordVar = {
                'idOrder': order[0],
                'StatOfTreatment': order[1],
                'PaymentStat': order[2],
                'TotalPrice': order[3],
                'idCli': order[4],
                'FirstName': order[5],
                'LastName': order[6],
                'Email': order[7],
                'WhatsApp':order[8] ,
                'offers': []
            }

            #For each order get offers names
            sql = "SELECT O.name FROM orderoffers OO, offers O WHERE OO.idOffer = O.idOffer AND OO.idOrder = %s"
            data = (order[0],)
            mycursor.execute(sql,data)
            OffersNames = mycursor.fetchall()

            for OfferName in OffersNames :
                ordVar['offers'].append(OfferName[0])

            ListOrders.append(ordVar)


        #Get the number of clients and total revenue
        mycursor.execute("SELECT count(*) FROM user WHERE role='client' ")
        result = mycursor.fetchall()
        NumbSignup = result[0][0]

        mycursor.execute("Select SUM(TotalPrice),count(*) from orders Where PaymentStat = 'Payed' ")
        result = mycursor.fetchall()
        Revenue =  result[0][0]
        NumbOrders = result[0][1]
        

        ''' Using this the data will be displayed on the top
        #Get data from the button  Show USERS :
        if request.method == "GET":
            ListOfClients = request.args.get('ListOfClients')
            ListOfEmployees = request.args.get('ListOfEmployees')
            ListOfAdmins = request.args.get('ListOfAdmins')
        else:
            ListOfClients = None
            ListOfEmployees = None
            ListOfAdmins = None  
        '''
        session['ListOrders'] = ListOrders
        session['OrderNumber'] = OrderNumber
        session['NumbSignup'] = NumbSignup
        session['Revenue'] = Revenue
        session['NumbOrders'] = NumbOrders

        if session["role"] == "admin":      
            #Do the same as the employee but can also add/remove offers | change role
            return render_template("Activity_Page.html",USR = "admin",ListOrders = ListOrders,OrderNumber = OrderNumber,offerToModify = None,NumbSignup = NumbSignup ,Revenue=Revenue,NumbOrders = NumbOrders)
        else:
                return render_template("Activity_Page.html",USR = "employee" ,ListOrders = ListOrders,OrderNumber = OrderNumber)








#Payment --------------------------------------------------------------------------------------------  

# Add data to subscription table for the client who sent the order : 
# And Change PaymentStat To payed
@app.route("/Payed", methods=["POST"])
def Payed():
    idOrder = request.form.get('idOrder')
    idCli = request.form.get('idCli')
    #Add offers to subscription data :
        #Select offers id and duration of the order:
    sql = "SElECT OO.idOffer, o.duration from offers AS o,orderoffers AS OO where OO.idOffer = o.idOffer AND idOrder = %s"
    data = (idOrder,)
    mycursor.execute(sql,data)
    Offersid_durations = mycursor.fetchall()

        #Add all offers to subscription :
    current_date = datetime.now()
    for orferid_duration in Offersid_durations:

        duration = timedelta(days = orferid_duration[1])
        endDate = current_date + duration

        sql = "INSERT INTO subscription (idCli,idOffer,subscriptionStatus,startDate,endDate) VALUES (%s,%s,%s,%s,%s)"
        data = (idCli,orferid_duration[0],'Active',current_date,endDate)
        mycursor.execute(sql,data)
        myconnection.commit()


    #Change PaymentStat in Orders table :
    sql = "UPDATE orders SET PaymentStat = 'Payed',StatOfTreatment = 'treated' WHERE idOrder = %s "
    data = (idOrder,)
    mycursor.execute(sql,data)
    myconnection.commit()


    return redirect('Activity_Page')







#Change StatOfTreatment To treated -------------------------------------------------------------------
@app.route("/Treated", methods=["POST"])
def Treated():
    idOrder = request.form.get('idOrder')
    sql = "UPDATE orders SET StatOfTreatment = 'treated' where idOrder = %s"
    data = (idOrder,)
    mycursor.execute(sql,data)
    myconnection.commit()

    return redirect('Activity_Page')





#ChangeRole ------------------------------------------------------------------------
@app.route('/ChangeRole', methods=["POST"])
def ChangeRole():
    #Get the email_UserID AND ROLE
    email_UserId = request.form.get('ChangeRoleInput')
    role = request.form.get('Role')

    #Check if it's an email or an id and Change sql query according to the results of the check :
    if email_UserId.isdigit():
        #Input is a number
        sql = "UPDATE user SET role = %s WHERE idCli = %s"

    else:
        #Input is a string
        sql = "UPDATE user SET role = %s WHERE Email = %s"
        email_UserId.lower()


    data = (role,email_UserId,)
    mycursor.execute(sql,data)
    myconnection.commit()

    return redirect('Activity_Page')


#(Add / Remove / Modify) OFFERS ---------------------------------------------------------------

#Check if the Name of the offer if it does actualy exist (axios) (for add Offer only)
@app.route('/CheckOfferName', methods=["POST"])
def CheckOfferName():
    if request.method == "POST":
        name = request.json['name']
        name = name.lower()

        sql = "SELECT LOWER(name) FROM offers WHERE LOWER(name) = %s"
        data = (name,)
        mycursor.execute(sql, data)
        results = mycursor.fetchall()


        if len(results) > 0:        # <=> if results:
            if results[0][0] == name:
                # User already exists
                return jsonify({"name_exist": "true"})
            else:
                # User doesn't exist
                return jsonify({"name_exist": "false"})
        else:
            return jsonify({"name_exist": "false"})

    else:
        # Handle invalid requests
        return jsonify({"error": "Invalid request method"})


#Check if the offer id exist (axios) (GENERAL FOR REMOVE / MODIFY )
@app.route('/CheckOfferID', methods=["POST"])
def CheckOfferID():
    if request.method == "POST":
        offerID = request.json['offerID']

        sql = "SELECT idOffer FROM offers WHERE idOffer = %s"
        data = (offerID,)
        mycursor.execute(sql, data)
        results = mycursor.fetchall()


        if len(results) > 0:        # <=> if results:
            return jsonify({"offerID_exist": "true"})
        else:
            # offer doesn't exist
            return jsonify({"offerID_exist": "false"})

    else:
        # Handle invalid requests
        return jsonify({"error": "Invalid request method"})





#Add offers (+ Upload offer img if there is no imsg use the default ):
@app.route("/AddOffer", methods = ["POST"])
def AddOffer():
        #Get the new data : 
    offer_pic = request.files["file"]
    description = request.form.get('description')
    duration = request.form.get('duration')
    Offer_price = request.form.get('Offer_price')
    name = request.form.get('name')

    # Insert the offer normal data :
    sql = "INSERT INTO offers (description,duration,Offer_price,name) VALUES (%s,%s,%s,%s)"
    data = (description,duration,Offer_price,name)
    mycursor.execute(sql,data)
    myconnection.commit()

    offerID = mycursor.lastrowid

    #Upload the img if it does exist else it will be automaticaly set to the default pic:
    if offer_pic:
        # change the name of the img to : offername + ...
        pic_filename = secure_filename(offer_pic.filename)
        file_Extention = pic_filename.rsplit('.', 1)[1].lower()

        UPLOAD_FOLDER = 'static\\Images\\product_pics'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        pic_name = f"{name}.{file_Extention}" 
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],pic_name)

        #upload the offer img in products-pics
        offer_pic.save(file_path)

        #Update data base offer name :
        sql = "UPDATE offers SET image_Name = %s WHERE idOffer = %s"
        data = (pic_name,offerID,)
        mycursor.execute(sql,data)
        myconnection.commit()

    return redirect('Activity_Page')





#Remove Offers :
@app.route("/RemoveOffer", methods=["POST"])
def RemoveOffer():
    offerID = request.form.get('offerID')
   
        #Remove the offer :
            #Delete All offers with same offer id in CartOffers 
    cart_offers_sql = "DELETE FROM cartoffers WHERE idOffer = %s"
    data = (offerID,)
    mycursor.execute(cart_offers_sql,data,)
    myconnection.commit()


            #Delete All offers with same offer id in OrderOffers 
    order_offers_sql = "DELETE FROM orderoffers WHERE idOffer = %s"
    data = (offerID,)
    mycursor.execute(order_offers_sql,data,)
    myconnection.commit()

            #Delete All offers with same offer id in Subscription 
    subscription_sql = "DELETE FROM subscription WHERE idOffer = %s"
    data = (offerID,)
    mycursor.execute(subscription_sql,data,)
    myconnection.commit()



    #Also delete the img of the offer saved in product_pics if it's not a default img !
    sql = "SELECT image_Name FROM offers WHERE idOffer = %s"
    data = (offerID,)
    mycursor.execute(sql, data)
    results = mycursor.fetchall()

    UPLOAD_FOLDER = 'static\\Images\\product_pics'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if results:
        pic_name = results[0][0]
        if pic_name != 'default-product-image.png':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], pic_name)
            os.remove(file_path)


    # Delete Offer
    sql = "DELETE FROM offers WHERE idOffer = %s "
    data = (offerID,)
    mycursor.execute(sql,data)
    myconnection.commit()

    return redirect("/Activity_Page")



#Modify Offers :

    #Get the offerToModify data :
@app.route("/get_OfferToModify_Data", methods=["POST"])
def get_OfferToModify_Data():
    offerID = request.form.get('offerID')
    sql = "SELECT name,Offer_price,duration,description FROM offers WHERE idOffer = %s "
    data = (offerID,)
    mycursor.execute(sql,data)
    offer = mycursor.fetchall()

    offerToModify = {
        'name': offer[0][0],
        'Offer_price': offer[0][1],
        'duration': offer[0][2],
        'description': offer[0][3],
        'offerID': offerID}   
    return render_template("Activity_Page.html", offerToModify=offerToModify)



    #Update the offer data :
@app.route("/modifyOffer", methods=["POST"])
def modifyOffer():
    #Get the new data : 
    offer_pic = request.files["file"]
    description = request.form.get('description')
    duration = request.form.get('duration')
    Offer_price = request.form.get('Offer_price')
    name = request.form.get('name')
    offerID = request.form.get('offerID')

    #Update the offer normal data :
    sql = "UPDATE offers SET description = %s , duration = %s,Offer_price = %s ,name = %s WHERE idOffer = %s"
    data = (description,duration,Offer_price,name,offerID,)
    mycursor.execute(sql,data)
    myconnection.commit()

    #Upload the img in the offers imgs, if the img is changed and save it's name in the offer table :
    if offer_pic:
        # change the name of the img to : offername + ...
        pic_filename = secure_filename(offer_pic.filename)
        file_Extention = pic_filename.rsplit('.', 1)[1].lower()

        UPLOAD_FOLDER = 'static\\Images\\product_pics'
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        pic_name = f"{name}.{file_Extention}" 
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],pic_name)

        # Remove the existing file if it exists
        if os.path.exists(file_path):
            os.remove(file_path)
        #upload the offer img in products-pics
        offer_pic.save(file_path)

        #Update data base offer name :
        sql = "UPDATE offers SET image_Name = %s WHERE idOffer = %s"
        data = (pic_name,offerID,)
        mycursor.execute(sql,data)
        myconnection.commit()

    return redirect("/Activity_Page")


#Delete subscription ---------------------------------------------------------------------------
@app.route("/DeleteSub", methods = ["POST","GET"])
def DeleteSub():
    if request.method == "POST":
        idSub = request.form.get('idSub')
    else:
        idSub = request.args.get('idSub')

    sql = "DELETE FROM subscription WHERE idSubscription = %s"
    data = (idSub,)
    mycursor.execute(sql,data)
    myconnection.commit()

    return redirect("/Activity_Page")

#Renew subscription  --------------------------------------------------------------------------
@app.route("/RenewSub", methods = ["POST"])
def RenewSub():
    idCli = session['idCli']
    idOffer = request.form.get('idOffer')
    idSub = request.form.get('idSub')


    #Get offer price :
    sql = "SELECT Offer_price FROM offers WHERE idOffer = %s"
    data = (idOffer,)
    mycursor.execute(sql,data)
    resu = mycursor.fetchall()
    OfferPrice = resu[0][0]
    
    #Fill order table :
    sql = "INSERT INTO orders (idCli, TotalPrice) VALUES (%s, %s)"
    data = (idCli,OfferPrice) 
    mycursor.execute(sql, data)
    myconnection.commit()

    idOrder = mycursor.lastrowid

    #Fill orderOffers table :
    sql = "INSERT INTO orderoffers (idOrder,idOffer) VALUES (%s, %s)"
    data = (idOrder,idOffer) 
    mycursor.execute(sql, data)
    myconnection.commit()

    return redirect(url_for('DeleteSub', idSub=idSub))

#CheckUserID --------------------------------------------------------------------------------------

#Check if the UserID exist (axios)
@app.route('/CheckUserID', methods=["POST"])
def CheckUserID():
    if request.method == "POST":
        UserID = request.json['UserID']

        #If the id is a number :
        if (UserID.isdigit()):
            sql = "SELECT idCli FROM user WHERE idCli= %s"

        else:
        #the id is an email :
            UserId = UserId.lower()
            sql = "SELECT idCli FROM user WHERE Email = %s"

    
        data = (UserID,)
        mycursor.execute(sql, data)
        results = mycursor.fetchall()
        UserID = results[0][0]


        sql = "SELECT role from user where idCli = %s"
        data = (UserID,)
        mycursor.execute(sql,data)
        role = mycursor.fetchall()

        if len(results) > 0:        # <=> if results:
            if role[0][0] == 'admin':
                return jsonify({"UserID_exist": "admin"})
            else:
                return jsonify({"UserID_exist": "true"})
        else:
            # User doesn't exist
            return jsonify({"UserID_exist": "false"})

    else:
        # Handle invalid requests
        return jsonify({"error": "Invalid request method"})
    

#RemoveUSER -------------------------------------------------------------------------------------
@app.route("/RemoveUSER", methods = ["POST"])
def RemoveUSER():
    #Delete the user using only user id because these a way to see users id :

    #It's 100% not an admin so we can delete the account : 
    UserId = request.form.get('UserID')


    #Can't delete user directly 
    data = (UserId,)

    # Delete cartOffers data about the user if it exists
    sqlCartOffers = "DELETE FROM cartoffers WHERE idCart IN (SELECT idCart FROM cart WHERE idCli = %s)"
    mycursor.execute(sqlCartOffers, data)
    myconnection.commit()

    # Delete cart data about the user
    sqlCart = "DELETE FROM cart WHERE idCli = %s"
    mycursor.execute(sqlCart, data)
    myconnection.commit()

    # Delete orderOffers data about the user 
    sqlOrderOffers = "DELETE FROM orderoffers WHERE idOrder IN (SELECT idOrder FROM orders WHERE idCli = %s)"
    mycursor.execute(sqlOrderOffers, data)
    myconnection.commit()

    # Delete order data about the user
    #on peux pas car si on supprime les order on va trouver un problem sur le calcule de revenue donc on va set idCli dans orders a ‘null’ 
    sqlOrders = "UPDATE orders SET idCli = NULL WHERE idCli = %s"
    mycursor.execute(sqlOrders, data)
    myconnection.commit()

    # Delete subscription data about the user
    sqlSubscription = "DELETE FROM subscription WHERE idCli = %s"
    mycursor.execute(sqlSubscription, data)
    myconnection.commit()

    # Delete user
    sqlUser = "DELETE FROM user WHERE idCli = %s"
    mycursor.execute(sqlUser, data)
    myconnection.commit()


    return redirect("/Activity_Page")


#Show All Users -----------------------------------------------------------------------------------
@app.route("/showUsers", methods=["POST"])
def showUsers():
    #SET the List of Clients :
    sql = "SELECT idCli,Email,FirstName,LastName,status ,role,Date_Joined,whatsapp FROM user where role='client'"
    mycursor.execute(sql)
    Clients = mycursor.fetchall()
    ListOfClients = []
    for client in Clients:
        clientData = {
            'idCli': client[0],
            'Email': client[1],
            'FirstName': client[2],
            'LastName': client[3],
            'status': client[4],
            'role': client[5],
            'Date_Joined': client[6],
            'whatsapp': client[7]
        }
        ListOfClients.append(clientData)



    #SET the List of Employees :
    sql = "SELECT idCli,Email,FirstName,LastName,status ,role,Date_Joined,whatsapp FROM user where role='employee'"
    mycursor.execute(sql)
    Employees = mycursor.fetchall()
    ListOfEmployees = []
    for Employee in Employees:
        employeeData = {
            'idCli': Employee[0],
            'Email': Employee[1],
            'FirstName': Employee[2],
            'LastName': Employee[3],
            'status': Employee[4],
            'role': Employee[5],
            'Date_Joined': Employee[6],
            'whatsapp': Employee[7]
        }
        ListOfEmployees.append(employeeData)


    #SET the List of Admins :
    sql = "SELECT idCli,Email,FirstName,LastName,status ,role,Date_Joined,whatsapp FROM user where role='admin'"
    mycursor.execute(sql)
    Admins = mycursor.fetchall()
    ListOfAdmins = []
    for Admin in Admins:
        adminData = {
            'idCli': Admin[0],
            'Email': Admin[1],
            'FirstName': Admin[2],
            'LastName': Admin[3],
            'status': Admin[4],
            'role': Admin[5],
            'Date_Joined': Admin[6],
            'whatsapp': Admin[7]
        }
        ListOfAdmins.append(adminData)

    #If i used the simple way to redirect the data will be shown in the top but i dont want that :
    ListOrders = session['ListOrders']
    OrderNumber = session['OrderNumber']
    NumbSignup = session['NumbSignup']
    Revenue = session['Revenue']
    NumbOrders = session['NumbOrders']


    return render_template("Activity_Page.html",USR = "admin",ListOrders = ListOrders,OrderNumber = OrderNumber,offerToModify = None,NumbSignup = NumbSignup ,Revenue=Revenue,ListOfClients=ListOfClients,ListOfEmployees = ListOfEmployees,ListOfAdmins = ListOfAdmins,NumbOrders=NumbOrders)


# ----------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
