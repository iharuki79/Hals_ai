#Hals_ai
@Hals_SCっぽいものを作るコードです

#各ファイル
###README.md
これ

##～マルコフ連鎖
##GenerateText.py , PrepareChain.py
data.txtから3つ組のchainを作成→chain.dbに保存

###schema.sql
db作成のためのスキーマファイル

###chain.db
3つ組チェーンのデータが入る(gitで管理されていない)

##ツイート収集&ツイート
###data.txt
ツイートデータを格納(gitで管理されていない)

###GetTweet.py
APIから@Hals_SCの最新のツイート50件を得、data.txtに格納

###TextTweet.py
data.txtからPrepareChain.pyとGenerateText.pyで文章を生成、ツイートする

##herokuで定期的に動かす
###clock.py
30分ごとにツイート取得・文章生成・ツイートする

###index.py
ダミーファイル、内容に特に意味はない

###Procfile,runtime.txt,requirements.txt,.caller
herokuで動かす環境を作成
※pip freeze>requirements.txtをコマンドプロンプトで実行し、一部削除した
