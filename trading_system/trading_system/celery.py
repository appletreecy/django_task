from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trading_system.settings')

app = Celery('trading_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'process-bulk-trades-every-5-minutes': {
        'task': 'trading.tasks.process_bulk_trades_task',
        'schedule': crontab(minute='*/1'),
    },
}
