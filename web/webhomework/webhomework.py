from flask import *

app = Flask(__name__)

info = [
    {"image": 'http://bit.ly/2npKQYD'},
    {"Full Name": 'TaThuyTien'},
    {"Education": '???'},
    {"Work Experiences": 'Yea Vietnam'},
    {"Location": 'Ha Noi - Vietnam'},
    {"Status": 'None'},
    {"Quote": "Stay hungry - Stay foolish"},
    {"Email": 'tathuytien@outlook.com.vn'},
    {"Phone No.": 'ศูนย์หนึ่งหกสามสามสองหนึ่งห้าแปด'},
    {"D.O.B": 1/1/1111}
]

@app.route('/')
def home_page():
    return 'Hello World!'

@app.route('/contact')
def contact_page():
    return template_rendered("contact.html")


if __name__ == '__main__':
    app.run()
