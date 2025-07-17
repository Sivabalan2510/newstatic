from flask import Flask, Response, abort
import requests

app = Flask(__name__)

STORAGE_ACCOUNT = "staticaccweb"
CONTAINER_NAME = "$web"
SAS_TOKEN = "sv=2024-11-04&ss=b&srt=sco&sp=rltfx&se=2025-07-17T17:14:39Z&st=2025-07-10T08:59:39Z&spr=https,http&sig=erya6iQg3Hr2FI8c5gyOudvMwaTBbD%2FsPmo6SHs2esI%3D"  # generated for blob service

@app.route("/<path:folder>/")
def serve_static(folder):
    blob_url = f"https://{STORAGE_ACCOUNT}.blob.core.windows.net/{CONTAINER_NAME}/{folder}/index.html?{SAS_TOKEN}"
    response = requests.get(blob_url)
    if response.status_code == 200:
        return Response(response.content, mimetype="text/html")
    return abort(404)
