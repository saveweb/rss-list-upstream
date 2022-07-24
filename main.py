import requests
import json


data = requests.get("https://zhblogs.ohyee.cc/api/blogs?size=-1&status=0").content
data = json.loads(data)
data = json.dumps(data, indent=2, sort_keys=False, ensure_ascii=False)
with open('zhblogs-data.json', 'w') as f:
    f.write(data)

data = requests.get("https://github.com/timqian/chinese-independent-blogs/raw/master/blogs-original.csv").content
with open('timqiam-independent-blogs-list.csv', 'bw') as f:
    f.write(data)

data = requests.get("https://github.com/qianguyihao/blog-list/raw/main/README.md").content
with open('qianguyihao-blog-list.md', 'bw') as f:
    f.write(data)

data = requests.get("https://github.com/travellings-link/travellings/raw/master/member.md").content
with open('travellings-member-list.md', 'bw') as f:
    f.write(data)

data = requests.get("https://github.com/alaskasquirrel/Chinese-Podcasts/raw/master/README.md").content
with open('alaskasquirrel-podcasts-list.md', 'bw') as f:
    f.write(data)

data = requests.get("https://github.com/tuna/blogroll/raw/master/README.md").content
with open('tuna-blogroll.md', 'bw') as f:
    f.write(data)

data = requests.get("https://box.othing.xyz/realtime.opml.xml").content
with open('saveweb-rsslist-daily.opml.xml', 'bw') as f:
    f.write(data)
