Manual：
https://flower.readthedocs.io/en/latest/index.html

Intro：
https://flower.readthedocs.io/en/latest/screenshots.html


Run Server： 
flower -A noty --port=5555 --conf=celeryconfig.py
celery flower -A proj --address=127.0.0.1 --port=5555

Open the Web admin panel:
http://localhost:5555/broker

Run test message: 
python -m noty.run_tasks