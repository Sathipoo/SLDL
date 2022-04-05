from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
@app.route("/pulak")
def pulak_world():
    return "<p>Hello, lipi!</p>"

@app.route("/login")
def login():
    return render_template("login.html", message="Hello Flask!");

@app.route("/index")
def login_to_sldl():
    return render_template("index.html", message="Hello Flask!");


if __name__ == "__main__":
    # website_url = 'DataIntegration.ETL.DIP:5000'
    # app.config['SERVER_NAME'] = website_url 
    app.run()