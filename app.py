from flask import Flask, render_template, jsonify, redirect
import os
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'
    # Initialize PyMongo to work with MongoDBs
#    conn = 'mongodb://localhost:27017'
#    client = pymongo.MongoClient(conn)
    
    # Define database and collection
#    db = client.mars
#    collection = db.items
#    mars = collection.find_one()
#    return render_template('index.html', mars=mars)

@app.route('/names')
def names():
    # DB connection setup
    dbfile = os.path.join('db', 'data/belly_button_biodiversity.sqlite')
    engine = create_engine("sqlite:///data/belly_button_biodiversity.sqlite")

    # reflect an existing database into a new model
    Base = automap_base()
    # reflect the tables
    Base.prepare(engine, reflect=True)

    # Save references to each table
    Samples_Metadata = Base.classes.samples_metadata
    OTU = Base.classes.otu
    Samples = Base.classes.samples

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query samples
    result=[column.key for column in Samples.__table__.columns]
    session.close()

    return render_template('index.html', names=result)

   
if __name__ == "__main__":
    app.run(debug=True)