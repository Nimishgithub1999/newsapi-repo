
# Flask News App

## Introduction

This is a simple web application built using Flask that fetches and displays top headlines related to Bitcoin from the News API. Additionally, it also provides a list of news sources in the business category.

## Prerequisites

Before you start, ensure you have the following dependencies installed:

- Flask
- gunicorn
- newsapi-python
- python-dotenv
- requests

You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root directory and add your News API key:

```
apikey=your_news_api_key
```

Replace `your_news_api_key` with your actual News API key.

5. Run the application:

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your web browser to view the application.

## Usage

- The homepage displays top headlines related to Bitcoin and a list of news sources in the business category.
- Click on "Read more" to view the full article.
- Click on "Visit website" to visit the news source's website.


## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [News API](https://newsapi.org/)
- [gunicorn](https://gunicorn.org/)
