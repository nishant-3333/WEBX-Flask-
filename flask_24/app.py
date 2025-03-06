from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

projects = [
    {"title": "Project 1", "description": "Description for Project 1", "image": "project1.jpg", "link": "#"},
    {"title": "Project 2", "description": "Description for Project 2", "image": "project2.jpg", "link": "#"},
    {"title": "Project 3", "description": "Description for Project 3", "image": "project3.jpg", "link": "#"}
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html", projects=projects)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        return render_template("success.html", name=name, email=email, subject=subject, message=message)
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)