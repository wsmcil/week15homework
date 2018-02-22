Notes

@app.route("/")
def index():
    """Return the homepage."""
    return render_template('index.html')
​
​
@app.route('/names')
def names():
    """Return a list of sample names."""
​
    # Use Pandas to perform the sql query
    stmt = session.query(Samples).statement
    df = pd.read_sql_query(stmt, session.bind)
    df.set_index('otu_id', inplace=True)
​
    # Return a list of the column names (sample names)
    return jsonify(list(df.columns))
    
    
    