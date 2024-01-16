# YouTube Data API v3でいろいろするツール

## 機能一覧
- get_channel.py：　チャンネル名を指定してチャンネル情報を検索する
- get_video_list.py： チャンネルIDを指定して投稿された動画一覧を取得する。jsonファイルに出力
- get_video_info： 動画IDを指定して動画の詳細情報を取得する。jsonファイルに出力
- generate_urls.py： jsonファイルを参照してYouTubeの動画ダウンロード用のURLを出力する。

## 使い方
1. Google Cloud Consoleに接続
2. YouTube Data API v3を有効にする。
3. Keyを生成してコピー
4. .env.sampleをコピーして.envに変更。
5. key情報や検索項目を.envに指定する。
6. conda環境を作成 
    ```shell
    conda env create -f=env.yml
    ```
7. プロジェクトフォルダに移動して、環境をアクティブにする。
    ```shell
    conda activate [環境名]
    ```
8. 各処理を実行。