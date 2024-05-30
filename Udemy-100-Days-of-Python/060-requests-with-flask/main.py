from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get('https://api.npoint.io/ea78e9a6954877c3ae4d').json()
OWN_EMAIL = "YOUR EMAIL"
OWN_PASSWORD = "YOUR PASSWORD"
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', all_posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data['name'], data['email'], data['phone'], data['message'])
        send_email(data['name'], data['email'], data['phone'], data['message'])
        return render_template('contact.html', msg_sent=True)
    else:
        return render_template('contact.html', msg_sent=False)


@app.route('/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == '__main__':
    app.run(debug=True)
