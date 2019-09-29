# -*- coding: utf-8 -*-
import csv
import re

with open(r"D:\create\text-generator\data\Hals_SC190929.csv",encoding="utf-8") as f:
    reader=csv.reader(f)
    l=[low for low in reader]

with open("data.txt",mode="w",encoding="utf-8") as f:
    for low in l:

        #ポスト数ツイートはスキップ
        if "のポスト数：" in low[2]:
            continue

        #リンクの削除
        low[2]=re.sub(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-…_]+", "" ,low[2])

        #「まぁじ占い」の削除(結果は残す)
        low[2]=re.sub("⭐まぁじ占い⭐","",low[2])

        #個人的に出てきてほしくないので「#peing」「#質問箱」を消す
        low[2]=re.sub("#peing","",low[2])
        low[2]=re.sub("#質問箱","",low[2])
        f.write(low[2])
