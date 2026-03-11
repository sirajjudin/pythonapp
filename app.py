# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Example of accessing an environment variable set in Azure App Service
    website_name = os.environ.get("WEBSITE_SITE_NAME", "World")
    return f"<h1>Hello, {website_name}!</h1>"

if __name__ == "__main__":
    # The port can be dynamically set by Azure, so we use an environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
