from flask import Flask

app = Flask(__name__)

from app import views
from app.helpers import get_page_display_name, get_page_url_name

app.jinja_env.globals.update(get_page_display_name=get_page_display_name)
app.jinja_env.globals.update(get_page_url_name=get_page_url_name)