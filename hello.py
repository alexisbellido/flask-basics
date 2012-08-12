from flask import Flask, url_for
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def  index():
    return 'Index page'

@app.route('/hello/')
@app.route('/hello/<name>')
def  hello(name=None):
    app.logger.debug('This is the logger line for %s' % name)
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    output = "User %s" % username
    output += '<p>'
    output += url_for('hello')
    output += '</p>'
    return output

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post %d" % post_id

app.debug = True
if __name__ == '__main__':
    app.run(host='192.168.0.185')
