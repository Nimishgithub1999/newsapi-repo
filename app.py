from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

# Initialize News API client
newsapi = NewsApiClient(api_key='5519a303a0574dd99f6272b39f0fbc37')

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

if __name__ == '__main__':
    app.run(debug=True)