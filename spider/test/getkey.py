import urllib2

url = 'http://localhost/get_key.php?pwd=123'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
print response.read()