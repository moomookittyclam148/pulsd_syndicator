#Pulsd Syndicator  
Look up 5 websites/apps where Pulsd events can be reposted e.g. eventbrite.com. Write code
to automate this syndication process.

The end product should have an admin panel to add new events/products to database and in
the backend there should be a process e.g. cron job, ruby worker etc which checks database for
new entries at a given interval, say once every hour, and in case of new entries, takes all new
data and syndicates it to all the 5 websites that you looked up earlier.

You may create any tables (such as products etc.) and fields (such as product_name,
product_description, product_price etc.) in database as per requirement.

##Assumptions
- User is running the app with Chrome using Mac Os(selenium uses a specific Mac Os Google Chrome driver)
- Most security features not implemented(Such as, Cross-site-scripting, sql-injection, etc)
- Only basic information is used to create the event(Such as, Event name, address, dates and times)

##requirements
Python 3.6.3  
APScheduler==3.5.1  
certifi==2018.4.16  
chardet==3.0.4  
click==6.7  
Flask==1.0.2  
Flask-SQLAlchemy==2.3.2  
idna==2.6  
itsdangerous==0.24  
Jinja2==2.10  
MarkupSafe==1.0  
pytz==2018.4  
requests==2.18.4  
selenium==3.12.0  
six==1.11.0  
SQLAlchemy==1.2.8  
tzlocal==1.5.1  
urllib3==1.22  
Werkzeug==0.14.1  

To install, within a new environment run  
`pip install -r requirements.txt`  
To run  
`python main.py`
