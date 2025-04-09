from flask import Flask, render_template, jsonify
import  requests #used to make network calls


app = Flask(__name__)

artist = "SZA"
song = "Good Days"

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

#below app declaration
@app.route("/about")
def about():
    return render_template("about.html")

#Let's get some song lyrics
@app.route('/lyrics')
def get_lyrics():
    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Could not fetch lyrics"}), 500
    

@app.route('/lyrics/<artist>/<song>')
def get_any_lyrics(artist, song):
    # Replace spaces with %20 (URL encoding)
    artist = artist.replace(" ", "%20")
    song = song.replace(" ", "%20")

    url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Could not fetch lyrics"}), 500
    
    
@app.route('/apod')
def get_apod():

    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    else: 
        return jsonify({"error": "Could not fetch lyrics"}), 500
    

@app.route('/rick-and-morty/<id>')
def get_rick_and_morty_character(id):

    url = f'https://rickandmortyapi.com/api/character/{id}'
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    else: 
        return jsonify({"error": "Could not fetch lyrics"}), 500
    