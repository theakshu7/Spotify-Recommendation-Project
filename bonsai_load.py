
from elasticsearch import Elasticsearch, helpers
import os
import json
import re

bonsai = 'https://a1tcqyknxy:rgnppwn3xr@team-apple-music-1100815724.us-east-1.bonsaisearch.net:443'


auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')

# optional port
match = re.search('(:\d+)', host)
if match:
  p = match.group(0)
  host = host.replace(p, '')
  port = int(p.split(':')[1])
else:
  port=443

# Connect to cluster over SSL using auth for best security:
es_header = [{
 'host': host,
 'port': port,
 'use_ssl': True,
 'http_auth': (auth[0],auth[1])
}]

# Instantiate the new Elasticsearch connection:
es = Elasticsearch(es_header)

#print(es.indices.get(index="index1*"))
docs = None
with open("data\\spotify_songs_genre.json", encoding="utf8") as file:
    docs = json.loads(file.read())
    helpers.bulk(es, docs)

#print(json.dumps(docs,indent=2))
