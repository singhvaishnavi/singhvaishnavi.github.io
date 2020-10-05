import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return flask.render_template('home.html')

@app.route('/about',methods=['GET'])
def about():
    return flask.render_template('about.html')

@app.route('/skills',methods=['GET'])
def skills():
    return flask.render_template('skills.html')

@app.route('/project',methods=['GET'])
def project():
    return flask.render_template('project.html')

@app.route('/contact',methods=['GET'])
def contact():
    return flask.render_template('contact.html')

@app.route('/cont',methods=['GET'])
def cont():
    return flask.render_template('cont.html')

if __name__ == '__main__':
    app.run()