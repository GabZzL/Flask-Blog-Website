from flask import Flask, render_template, request
from datetime import datetime
from functions import Blogs, Email

app = Flask(__name__)

# get the blogs data from the API
blogs = Blogs()
blogs_data = blogs.get_blogs()


@app.context_processor
def inject_now():
    return {'now': datetime.now()}


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs_data)


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def get_contact():
    # check the method
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        # handle the user information
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone"]
        message = request.form["message"]

        # send the email
        user_email = Email(name, email, phone_number, message)
        user_email.send_email()

        return render_template("contact.html")


@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    blog_list = [blog for blog in blogs_data if blog_id == blog["id"]]
    return render_template("post.html", blog=blog_list[0])


if __name__ == "__main__":
    app.run(debug=True)
