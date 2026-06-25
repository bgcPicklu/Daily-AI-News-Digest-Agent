from sqlalchemy import func
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from app.database.db import engine, SessionLocal
from app.database.models import Base, Article

from app.services.news_pipeline import run_pipeline

app = FastAPI()

Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="app/dashboard/templates")

@app.get("/")
def home():
    return {
        "message": "AI News Digest Running"
    }

@app.get("/run")
def run():
    result = run_pipeline()

    return {
        "success": True,
        "message": "Pipeline executed successfully",
        "digest": result["digest"],
        "stats": result["stats"],
        "top_news": result["top_news"]
    }

@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "digest": "Loading..."
        }
    )

@app.get("/analytics")
def analytics():
    db = SessionLocal()

    try:
        articles = db.query(Article).all()

        topic_data = {
            "AI": 0,
            "Python": 0,
            "Machine Learning": 0,
            "Cybersecurity": 0,
            "Cloud": 0
        }

        for article in articles:
            text = (
                article.title +
                " " +
                (article.summary or "")
            ).lower()

            for topic in topic_data:
                if topic.lower() in text:
                    topic_data[topic] += 1

        source_rows = (
            db.query(
                Article.source,
                func.count(Article.id)
            )
            .group_by(Article.source)
            .all()
        )

        source_data = {
            source: count
            for source, count in source_rows
        }

        return {
            "topics": topic_data,
            "sources": source_data
        }

    finally:
        db.close()