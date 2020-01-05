#  daum Finace 사이트 실제로 해보니 안됨

from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.daum.net/"
res = req.urlopen(url).read()
res = req.urlopen(url).read().decode('euc-kr','replace').encode('utf-8','replace')
# 한글 깨짐으로 read()뒤에 decode ,encode 추가

print(soup)
# print(soup.prettify()) 좀더 보기 좋게 보여줌

# tag(ul).#id(top)
top = soup.select("ul#topMyListNo1 > li">

for e in top:
    print('e>>>',e)
    print('e>>>',e.find("a").string)


#  enumerate  -> 변수 i 추가해서 index 주기
for i,e in enumerate(top):
    print('e>>>',e)
    print(i,",",e.find("a").string)

# 시작 index를 1로 추가로 주기,  가격도 추가적으로 가져오기
for i,e in enumerate(top,1):
    print('e>>>',e)
    print(i,",",e.find("a").string, e.find("span".string ))
