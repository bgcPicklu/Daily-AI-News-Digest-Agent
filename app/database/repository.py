from app.database.db import SessionLocal
from app.database.models import Article

def save_article(article):

    db = SessionLocal()

    try:

        existing = db.query(Article).filter(
            Article.url == article["url"]
        ).first()

        if existing:
            return

        record = Article(
            title=article["title"],
            url=article["url"],
            source=article.get("source",""),
            summary=article.get("summary",""),
            score=article.get("score",0),
            published=article.get("published","")
        )

        db.add(record)

        db.commit()

    except Exception as e:

        db.rollback()

        print("DB Error:", str(e))

    finally:

        db.close()