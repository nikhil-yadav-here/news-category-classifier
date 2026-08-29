# News Category Classifier – Rule Based

## Description

A simple Flask web application that analyzes news articles using
rule-based (keyword matching) logic — no AI, no machine learning,
no external APIs. This project converts an original console-based
Python program into a beginner-friendly web application.

## Objective

The application takes a news title and description, then uses
keyword-matching rules to determine the most likely category
(Sports, Technology, Politics, Business, or Entertainment). If no
category has a clear keyword match, the article is labeled "General".

## Features

- Rule-based classification (keyword scoring)
- Keyword extraction (lowercase, punctuation removal, duplicate removal)
- Duplicate detection (case-insensitive title match)
- News archive (view all articles)
- Search (by title, description, category, or keyword)
- Trend summary (category counts + trending category)

## Technologies

- Python 3
- Flask
- HTML5 / CSS3
- Jinja2
- Gunicorn
- Render (hosting)

## Project Structure

```
news-category-classifier/
│
├── app.py              # Flask routes and app entry point
├── classifier.py        # Rule-based classification logic
├── requirements.txt      # Python dependencies
├── README.md
├── .gitignore
│
├── templates/
│   ├── base.html         # Shared layout and navigation
│   ├── index.html        # Home / Add News page
│   ├── archive.html       # News Archive page
│   ├── trend.html         # Trend Summary page
│   └── search.html        # Search page
│
└── static/
    └── style.css
```

## Local Setup

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000 in your browser.

## Render Deployment

Deploy as a Render **Web Service** (Free plan) connected to your
GitHub repository.

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

See the full step-by-step deployment guide provided separately.

## Data Storage Limitation

This application stores news articles **only in memory** (a Python
list) while the app is running. There is no database or file-based
storage. This means:

- All added articles are available during the current running session.
- Data will **reset** whenever the application restarts or is
  redeployed on Render (including Render's free-plan auto-sleep/wake
  cycle).
- This is expected behavior for this project and not a bug.
