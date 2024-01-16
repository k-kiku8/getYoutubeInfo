"""
　指定した動画の情報を取得
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

# APIキーの設定
API_KEY = os.getenv("API_KEY")
VIDEO_LIST = [""]

# YouTube APIクライアントを初期化
youtube = build("youtube", "v3", developerKey=API_KEY)


def get_video_details(video_id):
    """
    指定のチャンネルに投稿されている動画の情報を一覧で取得する関数。

    Args:
        video_id      (str): 動画ID

    Returns:
        object: 動画情報
    """

    # 動画の詳細情報を取得
    request = youtube.videos().list(
        part="snippet,contentDetails",
        id=video_id
    )
    response = request.execute()

    if not response["items"]:
        print('error')
        return None

    item = response["items"][0]
    video_info = {
        "id": video_id,
        "title": item["snippet"]["title"],
        "publishedAt": item["snippet"]["publishedAt"],
        "tags": item["snippet"].get("tags", []),
        "duration": item["contentDetails"]["duration"]
    }
    return video_info


# 動画データをJSONファイルに書き出す関数
def write_to_json_file(video_info, filename):
    """
    一覧データをjson形式で保存する。

    Args:
        video_info  (object): 動画情報
        filename    (str): jsonファイル名
    Returns:
    """

    with open(filename, 'a', encoding='utf-8') as file:
        # JSONデータを追記
        json.dump(video_info, file, ensure_ascii=False, indent=4)
        file.write(',\n')


for video_id in VIDEO_LIST:
    video_info = get_video_details(video_id)
    if video_info:
        write_to_json_file(video_info, f"videos/youtube_video.txt")
