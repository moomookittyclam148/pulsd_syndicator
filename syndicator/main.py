from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event.db'
db = SQLAlchemy(app)

from models import *

@app.route('/', methods=["GET","POST"])
def base_page():
    if request.method == "POST":
        return render_template('base.html')
    else:
        return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
