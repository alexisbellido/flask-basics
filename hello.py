from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import make_response
from flask import abort, redirect, escape, session


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def  index():
    resp = make_response('some text for index')
    resp.set_cookie('color', 'red')
    return resp

    #return 'Index page. Method: %s' % request.method

@app.route('/custom-response')
def  custom_response():
    return ('Text', 200, {'Custom-Header': 'Some Value'})

@app.route('/hello/', methods=['GET', 'POST'])
@app.route('/hello/<name>', methods=['GET', 'POST'])
def  hello(name='Anybody'):
    print "request method", request.method
    key = request.args.get('key', '')
    print "key", key
    print "cookies", request.cookies
    if request.method == 'POST':
        #print "username", request.form['username']
        name = request.form.get('username', 'no username')
        print "username", name
    #app.logger.debug('This is the logger line for %s' % name)
    if key == 'redirect':
        return redirect(url_for('index'))
    if key == '404':
        abort(404)
    if key == '401':
        abort(401)
    if key == 'save_session':
        session['session_var'] = 'a value in session variable'
    if key == 'delete_session':
        session.pop('session_var', None)
    return render_template('hello.html', name=name, session_var=session.get('session_var', None))

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

app.secret_key = '|$\x8d\xd6\xe4{\xeb7\xafi\xbd+\xf6\x94\x80\xac\xdc\xd7 2u\x87Oo'
app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0')
