from flask import Flask, url_for, render_template, request, session, redirect
import utils


app = Flask(__name__)
app.config['SECRET_KEY'] = "Some_secret_string"


@app.route('/home/')
@app.route('/')
def home():
    session.clear()
    cities = utils.load_json(app)
    return render_template("index.html", cities=cities)


@app.route('/city/<city>/')
def profile(city):
    cities = utils.load_json(app)
    city_processed = city.lower()
    if(city_processed not in cities.keys()):
        message = "City not found"
        return render_template('message.html', message=message)
    else:
        city_data = cities[city_processed]
        return render_template("profile.html", city=city, data=city_data)


@app.route('/add_city/')
def form():
    return render_template('add_form.html')


@app.route('/submit_form/', methods=['POST'])
def form_post():
    city = request.form['city']
    population = request.form['population']
    city_processed = utils.strip_accents(city)

    cities = utils.load_json(app)

    if(city_processed in cities.keys()):
        session['message'] = "Entry for city: " + city_processed + " already exists!"
        return render_template('add_form.html')
    else:
        utils.add_entry(app, cities, city_processed, population)
        message = "Entry for city: " + city_processed + " created!" 
        return render_template('message.html', message=message)
    

@app.route('/find_city/')
def find_city():
    return render_template('find_form.html')


@app.route('/submit_find_city/', methods=['POST'])
def find_city_post():
    if request.method == 'POST':
        city = request.form['city']
        city_processed = utils.strip_accents(city)
        return redirect(url_for('profile', city=city_processed))
    

if __name__ == "__main__":
    app.run(port=5000, debug=True)
    #app.run()