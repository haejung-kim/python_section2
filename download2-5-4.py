# BeautifulSoup,   Tag selector 해서 접근 >
#  일반적으로 CSS class ,id는 거의 안바꾸기게에, 이방법이 더 안전함

import sys
import io
from bs4 import BeautifulSoup as bs

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html>
<body>
<div id="main">
<h1>강의목록</h1>
<ul class="lecs">
<li>Java 초고수 되기</li>
<li>파이썬 초고수 되기</li>
<li>파이썬 머신러닝  되기</li>
<li>안드로디으 블루투스</li>
</ul>
</div>
</body>
</html>
"""

soup = bs(html,"html.parser")

# H1 tag의 강의목록을 가져와 보기  tag#id 중에 하위가 h1)
#  tag#id
h1 = soup.select("div#main > h1")

for x in h1:
    print(x.string)

# 1개일때는 select one
h1 = soup.select_one("div#main > h1")
print(h1.string)

# tag#id ,      tag.class
# select -> list
list_li=soup.select("div#main > ul.lecs >li")
for li in list_li:
    print(li.string)

#    tag#id -> #id(tag부분 삭제가능)      tag.class -> .class (tag 부분 삭제 가능)
# div, ul tag를 없애고 id와 class값만 표시
list_li=soup.select("#main > .lecs >li")
for li in list_li:
    print(li.string)
