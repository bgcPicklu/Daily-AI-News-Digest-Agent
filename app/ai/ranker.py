TOPICS = [

    "AI",

    "Python",

    "Machine Learning",

    "Cybersecurity",

    "Cloud"
]

def calculate_score(article):

    text = (
        article["title"] +
        article["summary"]
    ).lower()

    score = 0

    for topic in TOPICS:

        if topic.lower() in text:
            score += 10

    return score