from flask import Flask
from flask_cors import CORS
import sqlite3
from config import SECRET_KEY

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# cors = CORS(app, resources={r"/api/*": {origins:"*"}})
CORS(app)

app.config['SECRET KEY'] = SECRET_KEY

from app import routes
