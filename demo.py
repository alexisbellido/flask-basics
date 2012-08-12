import flask, flask.views


app = flask.Flask(__name__)

class View(flask.views.MethodView):
    def get(self):
        #return "Hello world"
        return flask.render_template('index.html')

    def post(self):
        return "works!"

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

@app.route('/test')
def test():
    return 'Test Hello World'

app.debug = True
app.run(host='192.168.0.185')
