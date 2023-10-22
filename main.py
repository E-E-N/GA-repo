# Modules & Classes
from flask import Flask, render_template, request, jsonify
from flask import redirect, url_for
from api_main import APIhandler 

# variable for module's name
app = Flask(__name__)


# Username & Password set for login page 
valid_username = "admin"
valid_password = "1qaz2wsx"

# Standardize credentials for login page
credentials = valid_username.lower(), valid_password


#login page
@app.route("/")
def login_page():
    return render_template("login.html")


#username & password performs the cross-checks
@app.route("/login", methods=["POST"])
def login():
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")
    entered_credentials = entered_username.lower(), entered_password

    if entered_credentials == credentials:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login_page", error=1))
#Redirects to /home if the credentials are correct.


#Homepage, which I added 3 Hyperlinks. geocoding, forecast weather, credits
@app.route("/home")
def home():
    return render_template("homepage.html")

#Geocoding App Page, which basically for users to fill up the inputs.
@app.route("/geocoding-app")
def geocoding_app():
    return render_template("geocoding.html")

#The output of the API Package Data's will be in this.
@app.route("/process-geocoding", methods=["POST"])
def process_geocoding():
    location = request.form.get("location")
    count = request.form.get("count")
    api_handler = APIhandler(location, count)
    response = api_handler.Geocoding_data()
    return jsonify(response)


#Credits
@app.route("/credits")
def credits():
    return "Credits truly goes to GA Instructor for the guidance & support: Deeban, Yi Han, Zahid"

#implements the code even while the script is running behind the scene.
if __name__ == "__main__":
    app.run(debug=True)