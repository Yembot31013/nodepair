release: python manage.py migrate
web: daphne software.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker websocket_handler --settings=software.settings -v2