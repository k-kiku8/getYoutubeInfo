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
6. Anaconda NavigatorからPowershell Promptで立ち上げる
7. envファイルからconda環境を作成 
    ```shell
    conda env create -f=env.yml
    ```
8. 環境一覧
   ```shell 
   conda env list
   ```
9. プロジェクトフォルダに移動して、環境をアクティブにする。
    ```shell
    conda activate [環境名]
    ```

## ファイル一覧
### get_channel_info.py
チャンネル名を見てチャンネルの詳細情報を取得する。  
取得した情報にチャンネルIDが含まれているので、その情報を.envに設定する。
### get_video_list.py
チャンネルIDを見て、動画の一覧を取得してJSONに吐き出す。
クロールするので攻撃とみなされないようにアクセスに間をあける。

### get_video_info.py
記憶にない。使ってない？

### generate_urls.py
動画情報のJSONからURL一覧のテキストを吐き出す。
これを動画ダウンロードソフトに入れることでダウンロードできる。

### .env.sample
必要な固定値の例を入れておく。
ここから.envを作成して実際の値を入れる。.envはgitignore
### videos
動画情報の一覧とURL一覧のファイルが吐き出される場所。