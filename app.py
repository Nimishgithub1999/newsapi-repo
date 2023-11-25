from flask import Flask, render_template
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

apiKey = os.getenv('apikey')
newsapi = NewsApiClient(api_key=apiKey)

@app.route('/')
def homepage():
    top_headlines = newsapi.get_top_headlines(
        q='bitcoin',
        category='business',
        language='en',
        country='us'
    )
    sources = newsapi.get_sources()

    return render_template("index.html", top_headlines=top_headlines, sources=sources)

# Set the 'run' attribute as the Flask app instance
run = app
