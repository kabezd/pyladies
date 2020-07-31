from flask import Flask, url_for, render_template
# linux a mac maji male "flask"
app = Flask(__name__)
# zapnuti "ladiciho rezimu", to same jako debug=True v app.run
#app.config['DEBUG'] = True

@app.route('/home/')
@app.route('/')
def index():
    """Tato funkce se zavola, kdyz uzivatel prijde na domovskou stranku"""
    return 'Hello Pyladies!'
    #return 20/0

# nema smysl davat string: protoze je to vychozi :) i kdyz se tam zada cislo 11, tak se url zobrazi
@app.route('/user/<string:username>/')
def profile(username):
    return 'Hello user: {}'.format(username)
    #return 20/0

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)

# primo vytvori odkaz na nasi strance?
# funkce profile, username jako argument dane funkce
@app.route('/url/<name>')
def show_url(name):
    return url_for('profile', username=name)

# konvence kdyz se spusti ten skript a neimportujeme
if __name__ == "__main__":
    # spusti FLask aplikaci (i s indexem)
    # port 5000 je defaultne
    app.run(port=5000, debug=True)
    #app.run()