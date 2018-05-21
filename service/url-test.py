from urllib.parse import urlparse, parse_qs

url = 'mongodb://localhost:5000/test?_updated=lastModified&since=2018-01-01'

o = urlparse(url)

print(o)

q = o.query  # get the query
qs = parse_qs(q)

print('query as dict: ', qs)

updated = qs['_updated'][0]
since = qs['since'][0]

print('updated prop: ', updated)
print('since: ', since)
