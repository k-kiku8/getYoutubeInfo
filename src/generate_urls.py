"""
　ダウンロードソフト用に取得した動画一覧から
　YouTubeのURL一覧を作成してtxt形式で保存
"""

import json


base_url = "https://www.youtube.com/watch?v="

with open('videos/youtube_videos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

with open('videos/urls.txt', 'w') as file:
    for item in data:
        video_id = item['id']
        file.write(f"{base_url}{video_id}" + '\n')
