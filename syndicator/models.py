from main import db
from sqlalchemy.exc import *
import datetime

class event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    event_name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    state = db.Column(db.String(25), nullable=False)
    zip_code = db.Column(db.String(5), nullable=False)
    country = db.Column(db.String(25), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    event_img = db.Column(db.String(80), nullable=False)
    event_desc = db.Column(db.String(1000))
    event_type = db.Column(db.String(50))
    ticket_type = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, nullable=False)

    def __init__(self, event_name, address, city, state, zip_code, country, start_date, end_date, event_img,
                 event_desc, event_type, ticket_type):
                 self.event_name = event_name
                 self.address = address
                 self.city = city
                 self.state = state
                 self.zip_code = zip_code
                 self.country = country
                 self.start_date = start_date
                 self.end_date = end_date
                 self.event_img = event_img
                 self.event_desc = event_desc
                 self.event_type = event_type
                 self.ticket_type = ticket_type
                 self.date_created = datetime.datetime.now()

    def get_id(self):
        return str(self.id)

    def add_event(self):
        db.session.add(self)
        return db.session.commit()

    def delete_event(self):
        db.session.delete(self)
        return db.session_commit()
