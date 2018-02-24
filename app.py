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
    return render_template('index.html')

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
    results=[column.key for column in Samples.__table__.columns]
    session.close()
    return jsonify(samples=results)

@app.route('/samples/<sample>')
def samples(sample):
    
    #/samples/<sample>
    import os

    import pandas as pd
    import numpy as np

    import sqlalchemy
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    import sqlite3
    import json

    from flask import Flask, jsonify, render_template
    app = Flask(__name__)

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

    args=sample

    sample_id=int(args[3:6])

    qSamples = session.query(Samples.otu_id, getattr(Samples, args))
    #print(qSamples[1])
    dfSamples = pd.read_sql(qSamples.statement, qSamples.session.bind)
    dfSamples.columns = ['otu_ids', 'sample_values']
    dfSamples_sorted = dfSamples.sort_values('sample_values', axis=0, ascending=False)
    dSamples = dfSamples_sorted.to_dict('list')
    session.close()
    return jsonify(samples=dSamples)
   
if __name__ == "__main__":
    app.run(debug=True)