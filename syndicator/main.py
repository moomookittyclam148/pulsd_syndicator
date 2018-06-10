from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event.db'
db = SQLAlchemy(app)

from models import *

#index Page
@app.route('/', methods=["GET","POST"])
def base_page():
    if request.method == "POST":
        error_msg = []
        print(request.form)

        event_name = request.form['event_title']
        address = request.form['address_1'] + " " + request.form['address_2']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        country = request.form['country']

        if not isValidDate(request.form['start_date']):
            error_msg.append('Start date is not a valid date')
            return render_template('base.html', error_msg=error_msg)

        if not isValidDate(request.form['end_date']):
            error_msg.append('End date is not a valid date')
            return render_template('base.html', error_msg=error_msg)

        month,day,year = request.form['start_date'].split('/')
        hour,minutes = request.form['start_time'].split(':')
        start_date = datetime.datetime(int(year),int(month),int(day),int(hour),int(minutes))

        month,day,year = request.form['end_date'].split('/')
        hour,minutes = request.form['end_time'].split(':')
        end_date = datetime.datetime(int(year),int(month),int(day),int(hour),int(minutes))

        event_img = request.form['event_img']
        event_desc = request.form['event_desc']
        event_type = request.form['event_type']
        ticket_type = request.form['Radio']

        new_event = event(event_name, address, city, state, zip_code,
                          country, start_date, end_date, event_img,
                          event_desc, event_type, ticket_type)

        try:
            new_event.add_event()
        except:
            error_msg.append('Error in adding event to database')
            return render_template('base.html', error_msg=error_msg)

        return render_template('success.html')
    else:
        return render_template('base.html')

#Helper Functions
def isValidDate(date):
    isValidDate = True
    month,day,year = date.split('/')

    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        isValidDate = False

    return isValidDate


if __name__ == "__main__":
    app.run(debug=True)
