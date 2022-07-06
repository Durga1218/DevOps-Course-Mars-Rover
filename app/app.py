from flask import Flask, render_template, request, redirect, url_for
import json, requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=pwJgwXoYoQo3wchIFf32MI9Emb01fBW80Ho4BcCn")
    data = response.json()
    return render_template('index.html', landing_image=data["url"])

@app.route('/mars')
def mars():
    mars_img_list=[]
    response_mars = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=pwJgwXoYoQo3wchIFf32MI9Emb01fBW80Ho4BcCn")
    data_mars = response_mars.json()["photos"][0]["img_src"]
    return render_template('mars.html', mars_img=data_mars)