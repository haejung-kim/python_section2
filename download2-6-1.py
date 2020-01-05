# 정규 표현식  inport re
 #일반적으로 CSs selector를 많이 사용함, 정규 표현식 잘 사용안함 

import sys
import io
from bs4 import BeautifulSoup
import re # regex

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html> <body>
<ul>
    <li> <a id="naver" href="http://www.naver.com">naver</a></li>
    <li> <a href="http://www.daum.net">daum</a></li>
    <li> <a href="http://www.daum.com">daum</a></li>
    <li> <a href="http://www.google.com">google</a></li>
    <li> <a href="http://www.tistory.com.com">tistory</a></li>
</ul>
</body>
</html>
"""
soup = BeautifulSoup(html,'html.parser')

# naver 가져오는 방법 1 : a TAG에서
# test = soup.find('a',string="naver")
# print(test.string)

#  naver 가져오는 방법 2  (id가 naver 가져옴 )
# print(soup.find(id="naver").string)


# 방법3 (정규 표현식을 통해 가져옴 )
# li 5개 의 값을 가져오기  (hrer가 http로 시작하는 )
# re.compile 안에 내용 써주면 된다 (raw dat)
# http로 시작  , ex2: daum 포함
li=soup.find_all(href=re.compile(r"^http://"))
li2=soup.find_all(href=re.compile("daum"))

for e in li:
    print(e.attrs['href'])

print()
print("example2")
for e in li2:
    print(e.attrs['href'])
