from flask import Flask, render_template
import pymysql
from controllers import routes

app = Flask(__name__, template_folder='views')

routes.init_app(app)

app.run(host='localhost', port=5000, debug=True)