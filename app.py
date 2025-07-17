from flask import Flask, Response, abort
import requests

app = Flask(__name__)

STORAGE_ACCOUNT = "yourstorageaccount"
CONTAINER_NAME = "$web"
SAS_TOKEN = "your-SAS-token"  # generated for blob service

@app.route("/<path:folder>/")
def serve_static(folder):
    blob_url = f"https://{STORAGE_ACCOUNT}.blob.core.windows.net/{CONTAINER_NAME}/{folder}/index.html?{SAS_TOKEN}"
    response = requests.get(blob_url)
    if response.status_code == 200:
        return Response(response.content, mimetype="text/html")
    return abort(404)
