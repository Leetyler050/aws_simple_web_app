import serverless_wsgi
from app_2 import app
#from plotly_test import app

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)

