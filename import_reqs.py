from tqdm import tqdm
import random
import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import Lock
import random
from datetime import datetime, timedelta
import base64
import os
import json
from pathlib import Path
from urllib.parse import urlparse
import time
import requests
from quart import Quart, g, jsonify, request, Response, abort, stream_with_context
from quart_cors import cors
import tempfile
import yaml
from quart import current_app
from dotenv import load_dotenv

load_dotenv()
 

def proxy_post(url, data):
    return requests.post(url, json=data)

app = Quart(__name__)
# Allow localhost:3000 to not get CORS errors
app = cors(app, allow_origin="*")

with open("config/config.yaml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
