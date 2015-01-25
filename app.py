from eve import Eve
from eve_docs import eve_docs
from flask.ext.bootstrap import Bootstrap

app = Eve()
Bootstrap(app)
app.register_blueprint(eve_docs, url_prefix='/docs')

if __name__ == '__main__':
    app.run(debug=True)
