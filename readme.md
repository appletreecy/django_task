1. How to run this application
python manage.py runserver

2. How to manually test this application

endpoint to let user place trades.
curl -X POST http://127.0.0.1:8000/api/trades/ -H 'Content-Type: application/json' -u test_user:splunk3du -d '{"stock": 1, "quantity": 10, "trade_type": "BUY"}'

confirm the trade was placed on localhost:8000/admin/ (admin/password)

endpoint to retrieve the total value invested in a single stock by a user:
curl -X GET "http://127.0.0.1:8000/api/trades/total_value/?stock_id=1" -u test_user:splunk3du

3. How to run the Djanto test

python manage.py test

4. How to schedule the bulk trades:
4.1 please the csv file under the directory
trading_system/trading_system/bulk_trades.csv
username,stock,quantity,trade_type
test_user,TestStock,120,BUY
test_user,TestStock,51,SELL


4.2 start the Celery Workers:
celery -A trading_system worker --loglevel=info

4.3 start the Celery Beat Scheduler:
celery -A trading_system beat --loglevel=info
