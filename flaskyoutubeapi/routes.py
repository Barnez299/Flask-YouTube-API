import requests
from flask import Blueprint, render_template, current_app


main = Blueprint('main', __name__)

@main.route("/")
def index():
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    search_params = {
        'key': current_app.config['YOUTUBE_API_KEY'],
        'q': 'learn flask',
        'part': 'snippet',
        'maxResults': 9,
        'type': 'video'

    }

    r = requests.get(search_url, params=search_params)

    results = r.json()['items']



    video_ids =[]
    for result in results:
        video_ids.append(result['id']['videoId'])

    print(video_ids)

    return render_template('index.html')

