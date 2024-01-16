"""
　指定したチャンネルの動画一覧を取得
　※ ショート動画は秒数判断
"""

import os
import json
import datetime
from isodate import parse_duration
from dotenv import load_dotenv
from googleapiclient.discovery import build

# 環境変数を読み込む
load_dotenv()

# APIキーとチャンネルIDの設定
API_KEY = os.getenv('API_KEY')
CHANNEL_ID = os.getenv('CHANNEL_ID')
MAX_RESULTS = 50
NEXT_PAGE_TOKEN = None
youtube = build('youtube', 'v3', developerKey=API_KEY)


def get_videos(channel_id, max_results, next_page_token):
    """
    指定のチャンネルに投稿されている動画の情報を一覧で取得する関数。

    Args:
        channel_id      (str): チャンネルID
        max_results     (int): 1度に何件取得するか(max:50)
        next_page_token (str): 開始ページトークン

    Returns:
        list: チャンネルの動画一覧
    """
    video_data = []
    while True:
        request = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            maxResults=max_results,
            pageToken=next_page_token,
            type='video',
            order='date'
        )
        response = request.execute()

        video_ids = [item['id']['videoId'] for item in response['items']]
        # 詳細情報の取得
        details_request = youtube.videos().list(
            part="contentDetails",
            id=','.join(video_ids)
        )
        details_response = details_request.execute()

        for item in response['items']:
            video_id = item['id']['videoId']
            duration_iso8601 = next((detail['contentDetails']['duration'] for detail in details_response['items'] if detail['id'] == video_id), None)
            if duration_iso8601:
                duration_seconds = parse_duration(duration_iso8601).total_seconds()
                if duration_seconds > 60:
                    video_info = {
                        'id': video_id,
                        'title': item['snippet']['title'],
                        'publishedAt': item['snippet']['publishedAt'],
                        'tags': item['snippet'].get('tags', []),
                        'duration': duration_iso8601,
                    }
                    video_data.append(video_info)

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
            # print(next_page_token)

    return video_data


def write_to_json_file(videos, filename):
    """
    一覧データをjson形式で保存する。

    Args:
        videos      (list): 動画一覧
        filename    (str): jsonファイル名
    Returns:

    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(videos, file, ensure_ascii=False, indent=4)


videos = get_videos(CHANNEL_ID, MAX_RESULTS, NEXT_PAGE_TOKEN)
dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
write_to_json_file(videos, f"youtube_videos_{dt}.json")
