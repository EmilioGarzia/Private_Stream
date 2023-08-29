from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    with open("static/JSON/media.json", "r") as json_file:
        json_data = json_file.read()

    all_media = json.loads(json_data)
    selected_video = all_media[0]["title"]

    if request.method == "POST":
        selected_video = request.form["videos"]
    
    movie_title = selected_video[:-4]
    return render_template("index.html", selected_video=selected_video, videos=all_media, movie_title=movie_title)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)