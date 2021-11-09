import json
import os
from datetime import datetime, timezone

import flask
from flask import request, abort, send_from_directory
from flask_cors import CORS
import requests

from flask_pymongo import PyMongo
from pandas import DataFrame
from werkzeug.utils import secure_filename

# import CSVStructrPopulation

UPLOAD_DIRECTORY = "../api_uploaded_files"
UPLOAD_SUMMARY_DIRECTORY = "../api_uploaded_files/Summary"
TEMPLATE_SUMMARY_DIRECTORY = "../Template"



app = flask.Flask(__name__)
CORS(app)

app.config["DEBUG"] = True
# app.config['UPLOAD_DIRECTORY'] = UPLOAD_DIRECTORY


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

"""
Get : get Categories of 10bis restaurants 
"""
@app.route("/api/v1/resources/10bis/GetRestaurantCuisineTypes", methods=["GET"])
def GetRestaurantCuisineTypes():
    try:
        response = requests.get('https://www.10bis.co.il/NextApi/GetRestaurantCuisineTypes', timeout=2.50)
        print(response)
        return response.json()
    except:
        return "", 400



@app.route("/drinks", methods=["GET"])
def GetAllDrinks():
    try:

        response = requests.get\
                  ('https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup',
                   timeout=2.50)
        all_dishes = response.json()['Data']['categoriesList']
        print(all_dishes)
        drinks = [obj['dishList'][0] for obj in all_dishes]
        drinksdrinks = [{'dishId': obj['dishId'],} for obj in drinks]

        return json.dumps(drinksdrinks), 200
    except:
        return "", 400

@app.route("/getdrink/<id>", methods=["GET"])
def Get_specific_drink(id):
    try:
        response = requests.get\
                  ('https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup',
                   timeout=2.50)
        all_dishes = response.json()['Data']['categoriesList']
        print(all_dishes)
        drinks = [obj['dishList'][0] for obj in all_dishes]
        drinksdrinks = [{'dishId': obj['dishId'],} for obj in drinks]
        if(int(drinksdrinks['dishId']) == id) :
              return json.dumps(drinksdrinks[id]), 200
    except:
        return "", 400

@app.route("/pizzas", methods=["GET"])
def Get_ALL_pizzas():
    try:
        response = requests.get\
                  ('https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup',
                   timeout=2.50)
        all_dishes = response.json()['Data']['categoriesList']
        print(all_dishes)
        drinks = [obj['dishList'][1] for obj in all_dishes]
        drinksdrinks = [{'dishId': obj['dishId'],} for obj in drinks]

        return json.dumps(drinksdrinks), 200
    except:
        return "", 400

@app.route("/get_pizza/<id>", methods=["GET"])
def Get_specific_pizza(id):
    try:
        response = requests.get \
            ('https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup',
             timeout=2.50)
        all_dishes = response.json()['Data']['categoriesList']
        print(all_dishes)
        drinks = [obj['dishList'][1] for obj in all_dishes]
        drinksdrinks = [{'dishId': obj['dishId'], } for obj in drinks]
        if (int(drinksdrinks['dishId']) == id):
            return json.dumps(drinksdrinks[id]), 200
    except:
        return "", 400


@app.route("/desserts", methods=["GET"])
def Get_ALL_desserts():
    try:
        response = requests.get\
                  ('https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup',
                   timeout=2.50)
        all_dishes = response.json()['Data']['categoriesList']
        print(all_dishes)
        drinks = [obj['dishList'][2] for obj in all_dishes]
        drinksdrinks = [{'dishId': obj['dishId'],} for obj in drinks]

        return json.dumps(drinksdrinks), 200
    except:
        return "", 400

@app.route("/get_dessert/<id>", methods=["GET"])
def Get_specific_dessert(id):
    try:
        response = requests.get \
            ('https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup',
             timeout=2.50)
        all_dishes = response.json()['Data']['categoriesList']
        print(all_dishes)
        drinks = [obj['dishList'][1] for obj in all_dishes]
        drinksdrinks = [{'dishId': obj['dishId'], } for obj in drinks]
        if (int(drinksdrinks['dishId']) == id):
            return json.dumps(drinksdrinks[id]), 200
    except:
        return "", 400


@app.route("/calac_order", methods=["GET"])
def calc_order(id):
    try:
        response = requests.get \
            ('https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup',
             timeout=2.50)
        all_dishes = response.json()['Data']['categoriesList']
        print(all_dishes)
        drinks = [obj['dishList'][1] for obj in all_dishes]
        drinksdrinks = [{'dishId': obj['dishId'], } for obj in drinks]
        if (int(drinksdrinks['dishId']) == id):
            return json.dumps(drinksdrinks['price']), 200
    except:
        return "", 400

app.run()
x = requests.get("http://127.0.0.1:5000/api/v1/resources/10bis/GetRestaurantMenu")