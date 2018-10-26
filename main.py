from flask import Flask ,request,redirect,render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template("home_page.html",username="",username_error="",password= "",verifyPassword="",
                        password_error="",verifyPassword_error="",email="",email_error="")

@app.route("/",methods=["POST"])
def validate():
    username = request.form["username"]
    password = request.form["password"]
    verifyPassword = request.form["verifyPassword"]
    email = request.form["email"] 
  
    username_error=""
    password_error = ""
    verifyPassword_error = ""
    email_error = ""

   
    if (len(username) >30) or (len(username) < 3) or " " in username:
        username_error = "That's not a valid username"
        username = ""
        
        
    if (len(password) > 30) or (len(password) < 3) or " " in password:
        password_error = "That's not a valid password"
        password = ""
     
    if password != verifyPassword:
         verifyPassword_error = "Passwords don't match"
         verifyPassword = ""
         password = ""
    
    if  (email != '') and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
            email_error = 'This is not a valid email.'
            email = ''
    if  username_error :
           password = ""
           verifyPassword = ""
    if  email_error :
           password = ""
           verifyPassword = ""

         
     
     
    if not username_error and not password_error and not verifyPassword_error and not email_error:
        return redirect("/welcome_page?username={0}".format(username))
    else :
        return render_template("home_page.html",username = username,password= password,verifyPassword=verifyPassword,username_error= username_error,
                        password_error=password_error,verifyPassword_error=verifyPassword_error,email=email,email_error=email_error )

@app.route("/welcome_page")
def welcome():
    username = request.args.get("username")
    return render_template("welcome_page.html",username=username)
app.run()