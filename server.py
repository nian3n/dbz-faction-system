from app import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/success/<name>')
def sucess(name):
    return 'welcome %s' % name

@app.route('/', methods=['GET', 'POST', 'DELETE'])
# ‘/’ URL is bound with hello_world() function.
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return 
redirect(url_for('success', name=user))
    
# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)