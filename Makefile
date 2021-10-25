lint:
	flake8 --exclude=bottle.py --count --ignore=W191
redis:
	../redis-6.2.6/src/redis-server