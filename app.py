import os
from flask import Flask, render_template, request

from classifier import (
    classify_news,
    extract_keywords,
    check_duplicate,
    get_trend_summary,
    search_news,
)

app = Flask(__name__)

# ============================================
# IN-MEMORY DATA STORE
# (Resets when the app restarts/redeploys)
# ============================================

news_data = []


def add_sample_articles():
    """Preload a few sample articles across different categories."""

    samples = [
        {
            "title": "India wins thrilling cricket match against Australia",
            "description": "The cricket team secured a last-over win in the championship tournament, delighting fans across the country."
        },
        {
            "title": "New AI software revolutionizes smartphone technology",
            "description": "A tech startup launched an AI-powered app that uses smart software to improve computer performance."
        },
        {
            "title": "Government announces new policy ahead of election",
            "description": "The president and parliament discussed a new political policy expected to influence the upcoming election."
        },
        {
            "title": "Stock market rallies as company profits rise",
            "description": "The business sector saw growth as bank investments and startup funding boosted overall market economy."
        },
        {
            "title": "Bollywood actor announces new movie with popular singer",
            "description": "The entertainment industry is buzzing after a famous actress and singer confirmed their upcoming film."
        },
    ]

    for item in samples:
        category = classify_news(item["title"], item["description"])
        keywords = extract_keywords(item["title"], item["description"])

        news_data.append({
            "title": item["title"],
            "description": item["description"],
            "category": category,
            "keywords": keywords,
        })


add_sample_articles()


# ============================================
# ROUTES
# ============================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()

    error = None
    duplicate = False
    result = None

    if title == "":
        error = "Title cannot be empty."
    elif check_duplicate(title, news_data):
        duplicate = True
    else:
        category = classify_news(title, description)
        keywords = extract_keywords(title, description)

        article = {
            "title": title,
            "description": description,
            "category": category,
            "keywords": keywords,
        }

        news_data.append(article)

        result = article

    return render_template("index.html", error=error, duplicate=duplicate, result=result)


@app.route("/archive")
def archive():
    return render_template("archive.html", articles=news_data)


@app.route("/trend")
def trend():
    category_count, highest_category = get_trend_summary(news_data)
    return render_template(
        "trend.html",
        category_count=category_count,
        highest_category=highest_category,
        has_data=len(news_data) > 0,
    )


@app.route("/search")
def search():
    query = request.args.get("query", "").strip()
    results = search_news(query, news_data) if query else []
    searched = query != ""

    return render_template(
        "search.html",
        query=query,
        results=results,
        searched=searched,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
