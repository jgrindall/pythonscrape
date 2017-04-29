from bs4 import BeautifulSoup
import requests
import urllib
import re

BLOCK_SIZE = 8192
LINK_RE = re.compile('http://open.live.bbc.co.uk/mediaselector/5/redir/version/2.0/mediaset/audio-nondrm-download-low/proto/http/vpid/(.*)\.mp3')
MAX_PAGE_NUM = 26
BASE_URL = 'http://www.bbc.co.uk/programmes/b006qykl/episodes/downloads';

def downloadMp3(url):
	print("   - " + url)
	file_name = "downloads/" + url.split('/')[-1]
	req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"}) 
	u = urllib.request.urlopen( req )
	f = open(file_name, 'wb')
	d = u.info()
	while True:
		buffer = u.read(BLOCK_SIZE)
		if not buffer:
			break
		f.write(buffer),
	f.close()

def downloadAllOnPage(num):
	url = BASE_URL
	if num >= 2:
		url += ("?page=" + num)
	print("page: " + url)
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "lxml")
	for link in soup.find_all('a'):
		url = link.get('href')
		if re.search(LINK_RE, url):
			downloadMp3(url)


for i in range(1, MAX_PAGE_NUM):
   downloadAllOnPage(i)
