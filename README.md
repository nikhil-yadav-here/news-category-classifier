# News Category Classifier

A simple Flask web app that reads a news title and description and puts it into a category (Sports, Technology, Politics, Business, Entertainment) using keyword matching. No AI or machine learning is used, it's fully rule-based.

## Features

- Classifies news into categories based on keywords
- Extracts keywords from title and description
- Detects duplicate news (same title)
- View all added news in Archive
- Search news by keyword or category
- Shows trend summary (which category has most news)

## How it works

Each category has a list of keywords. When a news article is added, the app checks how many keywords from each category match the text. Whichever category matches the most, that becomes the news category. If nothing matches, it's marked as "General".

## Tech used

- Python
- Flask
- HTML/CSS
- Jinja2

## Live Demo

[Click here to view the live site](https://news-category-classifier-k95g.onrender.com/)

## Note

News data is stored only in memory (a Python list), so it resets when the app restarts.
