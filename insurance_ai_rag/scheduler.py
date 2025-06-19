from apscheduler.schedulers.background import BackgroundScheduler
from insurance_ai_rag.vector_updater import update_vector_store

scheduler = BackgroundScheduler()

# Simulated document poller
def fetch_new_documents():
    return [
        "Client submitted a new cancellation request on March 5th.",
        "Financial hardship email received March 4th."
    ]

def scheduled_update_job():
    docs = fetch_new_documents()
    update_vector_store(docs)
    print(f"Updated vector store with {len(docs)} documents.")

def start_scheduler():
    scheduler.add_job(scheduled_update_job, 'interval', minutes=30)
    scheduler.start()
