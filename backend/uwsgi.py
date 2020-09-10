[uwsgi]
socket=127.0.0.1:8080
#http=127.0.0.1:8080
chdir=/home/python/Desktop/market
wsgi-file=market/wsgi.py
processes=4
threads=2
master=True
pidfile=uwsgi.pid
daemonize=uwsgi.log
virtualenv=/home/python/.virtualenvs/test1