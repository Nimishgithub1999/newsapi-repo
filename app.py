from flask import Flask, render_template
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


apiKey = os.getenv('apikey')
# Initialize News API client
newsapi = NewsApiClient(api_key=apiKey)

@app.route('/')
def homepage():
    # Example: Get top headlines without specifying sources
    top_headlines = newsapi.get_top_headlines(
        q='bitcoin',
        category='business',
        language='en',
        country='us'
    )

    # Example: Get sources
    sources = newsapi.get_sources()

    return render_template("index.html", top_headlines=top_headlines, sources=sources)

