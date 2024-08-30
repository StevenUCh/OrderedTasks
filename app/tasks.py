from app import celery, db, mail
from app.models import Task
from flask_mail import Message
from datetime import datetime, timedelta

@celery.task
def send_reminder(task_id):
    task = Task.query.get(task_id)
    if task:
        msg = Message('Task Reminder', sender='your-email@example.com', recipients=[task.owner.email])
        msg.body = f"Reminder: Task '{task.title}' is due on {task.due_date}"
        mail.send(msg)

@celery.task
def send_reminders():
    tasks_due_soon = Task.query.filter(Task.due_date <= datetime.utcnow() + timedelta(days=1)).all()
    for task in tasks_due_soon:
        send_reminder.delay(task.id)
