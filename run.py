import os

from app import create_app

app = os.getenv('FLASK_ENV')

if __name__ == '__main__':
    app.run(debug=True)