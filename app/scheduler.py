from apscheduler.schedulers.blocking import BlockingScheduler

from app.services.news_pipeline import run_pipeline

scheduler = BlockingScheduler()

scheduler.add_job(
    run_pipeline,
    "cron",
    hour=7,
    minute=0
)

scheduler.start()