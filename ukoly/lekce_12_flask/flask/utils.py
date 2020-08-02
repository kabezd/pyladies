from flask import Flask, url_for, render_template, request, session
import os
import json
import unicodedata
# find if city already in db

# process form?

def load_json(app):
    filename = os.path.join(app.static_folder, 'data.json')
    with open(filename) as file:
        cities = json.load(file)
        return cities


def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    text = text.strip()
    return str(text.lower())

def add_entry(app, cities, city, population):
    cities[city] = population
    #json = json.dumps(cities, indent=2, ensure_ascii=False)
    filename = os.path.join(app.static_folder, 'data.json')
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(cities, file, ensure_ascii=False, indent=4)