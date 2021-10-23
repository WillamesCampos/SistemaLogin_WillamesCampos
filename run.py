import os
from app import app

if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
	    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
	    app.run(host='localhost', port=8080, debug=False, reloader=True)