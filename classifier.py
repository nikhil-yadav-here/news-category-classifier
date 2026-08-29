# ============================================
# NEWS CATEGORY CLASSIFIER - RULE BASED LOGIC
# (Refactored from original console project)
# ============================================

# Category rules
category_keywords = {
    "Sports": [
        "cricket", "football", "match", "player", "tournament",
        "sports", "goal", "team", "win", "championship"
    ],

    "Technology": [
        "technology", "tech", "ai", "artificial intelligence",
        "software", "computer", "smartphone", "robot",
        "app", "internet", "cyber"
    ],

    "Politics": [
        "election", "government", "minister", "president",
        "politics", "political", "vote", "parliament",
        "party", "policy"
    ],

    "Business": [
        "business", "market", "stock", "company", "economy",
        "bank", "investment", "finance", "profit", "startup"
    ],

    "Entertainment": [
        "movie", "film", "actor", "actress", "music",
        "celebrity", "bollywood", "hollywood", "singer",
        "entertainment"
    ]
}


# Common words ignored during keyword extraction
common_words = [
    "the", "is", "a", "an", "and", "or", "of", "to",
    "in", "on", "for", "with", "at", "by", "from",
    "this", "that", "has", "have", "new", "will",
    "was", "are", "as", "it", "its"
]


# ============================================
# 1. RULE-BASED CATEGORY CLASSIFICATION
# ============================================

def classify_news(title, description):
    """Classify news into a category based on keyword matching."""

    text = (title + " " + description).lower()

    category_scores = {}

    for category in category_keywords:
        score = 0

        for keyword in category_keywords[category]:
            if keyword in text:
                score += 1

        category_scores[category] = score

    highest_category = "General"
    highest_score = 0

    for category in category_scores:
        if category_scores[category] > highest_score:
            highest_score = category_scores[category]
            highest_category = category

    return highest_category


# ============================================
# 2. KEYWORD EXTRACTION
# ============================================

def extract_keywords(title, description):
    """Extract simple, unique keywords from title + description."""

    text = title + " " + description

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    punctuation = ".,!?;:()[]{}\"'"

    for symbol in punctuation:
        text = text.replace(symbol, "")

    words = text.split()

    keywords = []

    for word in words:
        if word not in common_words and len(word) > 2:
            if word not in keywords:
                keywords.append(word)

    return keywords[:10]


# ============================================
# 3. DUPLICATE DETECTION
# ============================================

def check_duplicate(title, news_data):
    """Check if a news title already exists (case-insensitive)."""

    title = title.lower().strip()

    for article in news_data:
        old_title = article["title"].lower().strip()

        if title == old_title:
            return True

    return False


# ============================================
# 4. TREND SUMMARY HELPER
# ============================================

def get_trend_summary(news_data):
    """Return category counts and the trending category."""

    category_count = {}

    for article in news_data:
        category = article["category"]

        if category not in category_count:
            category_count[category] = 1
        else:
            category_count[category] += 1

    highest_category = ""
    highest_count = 0

    for category in category_count:
        if category_count[category] > highest_count:
            highest_count = category_count[category]
            highest_category = category

    return category_count, highest_category


# ============================================
# 5. SEARCH HELPER
# ============================================

def search_news(query, news_data):
    """Search title, description, category and keywords (case-insensitive)."""

    query = query.lower().strip()
    results = []

    if query == "":
        return results

    for article in news_data:
        text = (
            article["title"]
            + " "
            + article["description"]
            + " "
            + article["category"]
            + " "
            + " ".join(article["keywords"])
        ).lower()

        if query in text:
            results.append(article)

    return results
