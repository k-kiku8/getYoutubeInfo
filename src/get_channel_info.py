"""
　指定したチャンネルの情報を取得
"""

import os
import json
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

API_KEY = os.getenv('API_KEY')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')

youtube = build('youtube', 'v3', developerKey=API_KEY)

response = youtube.search().list(q=CHANNEL_NAME, part='id,snippet', maxResults=10).execute()

for item in response.get('items', []):
    if item['id']['kind'] != 'youtube#channel':
        continue
    print('*' * 10)
    print(json.dumps(item, indent=2, ensure_ascii=False))
    print('*' * 10)
