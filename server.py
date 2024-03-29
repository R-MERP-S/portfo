import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import csv
from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)
print(__name__)


@app.route('/')
def my_homepage():
    return render_template('index.html')


'''@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/works.html')
def works():
    return render_template('works.html')


@app.route('/index.html')
def my_home():
    return render_template('index.html')'''
# using dynamic code


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a' ) as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a' ) as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')

        except:
            return'DID NOT SAVE THE CHANGE'
    else:
        return 'Something went Wrong!.TRY AGAIN'

