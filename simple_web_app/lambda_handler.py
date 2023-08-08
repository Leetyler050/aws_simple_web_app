import serverless_wsgi
from app_flask_template import app

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)

