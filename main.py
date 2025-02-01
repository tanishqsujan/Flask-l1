from flask import Flask, render_template, request 
from datetime import datetime

# Initialize the Flask application

app = Flask(__name__)

# Route for the homepage

@app.route("/")

def home():

# Render the index.html template

 return render_template("index.html")

def calculate_age():
    try:
        birth_year= int(request.form.get("birth_year"))
        current_year= datetime.now().year
        if birth_year> current_year or birth_year< 1900:
            return render_template("index.html", error= "Please enter a valid year")
        age= current_year - birth_year
        return render_template("index.html", age=age)
    
    except ValueError:
        return render_template("index.html", error= "Please enter a valid number")
app.run(host='0.0.0.0', port= 8080)
if __name__ == "__main__":
    app.run(debug= True)