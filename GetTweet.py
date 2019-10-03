import os
import re
import requests
import tweepy

# APIの秘密鍵
CK,CKS,AT,ATS=os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"]

def gettweet(CK, CKS, AT, ATS):
    auth = tweepy.OAuthHandler(CK, CKS)
    auth.set_access_token(AT, ATS)
    api = tweepy.API(auth)

    name="Hals_SC"
    results=api.user_timeline(screen_name=name,count=50,include_rts=False)

    f=open(r"data.txt",mode="a",encoding="utf-8")

    for result in results:
        #ポスト数ツイートはスキップ
        if "のポスト数：" in result.text:
            continue

        #リンクの削除
        result.text=re.sub(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-…_]+", "" ,result.text)

        #@ツイートの削除(昔仲良くしていたけど今ブロ解された…みたいな人に行くと地獄なので)
        result.text=re.sub("@[\w]+","",result.text)

        #「まぁじ占い」の削除
        result.text=re.sub("⭐まぁじ占い⭐","",result.text)

        #個人的に出てきてほしくないので「#peing」「#質問箱」を消す
        result.text=re.sub("#peing","",result.text)
        result.text=re.sub("#質問箱","",result.text)

        #data.txtに追加で書き込み
        f.write(result.text+"\n")

    f.close()

if __name__=="__main__":
    gettweet(CK,CKS,AT,ATS)
