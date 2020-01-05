# BeautifulSoup,   Tag selector 해서 접근 >


import sys
import io
from bs4 import BeautifulSoup as bs
# beautifulsoup BS대문자임에 주의(실수함)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding ='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding ='utf-8')


html = """
<html>
<body>
<ul>
<li> <a href="http://www.naver.com">naver</a> </li>
<li> <a href="http://www.daum.net">daum</a> </li>
<li> <a href="http://www.google.com">google</a> </li>
<li> <a href="http://www.tistory.com">tistory</a> </li>
</ul>
</body>
</html>
"""

soup = bs(html,"html.parser")

links = soup.find_all("a")

for a in links:
    href = a.attrs['href']
    txt = a.string
    print('txt >>', txt ,'href >>', href)


abc = soup.find_all("a", string="naver")  # a tag 가져오면서 string daum
print(abc)
# 실수 .com">   naver</a> </li>   naver안에 공백등을 인식

links = soup.find_all("a", limit=2)  #->2개만 가져오기 (앞에 있을때 )
print(links)

links = soup.find_all(string=["naver","google"])
print(links)
