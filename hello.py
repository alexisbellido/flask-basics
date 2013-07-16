from flask import Flask, url_for
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def  index():
    return 'Index page. Method: %s' % request.method

@app.route('/hello/', methods=['GET', 'POST'])
@app.route('/hello/<name>', methods=['GET', 'POST'])
def  hello(name='Anybody'):
    print "request method", request.method
    print "key", request.args.get('key', '')
    if request.method == 'POST':
        #print "username", request.form['username']
        name = request.form.get('username', 'no username')
        print "username", name
    #app.logger.debug('This is the logger line for %s' % name)
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
    app.run(host='0.0.0.0')
