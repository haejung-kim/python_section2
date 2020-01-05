# BeautifulSoup,    next_sibling , previous_sibling(중간에 추가, 삭제될때 사용 )
# -> 단점 html 파일 구조가 바뀔때 문제가 발생함

import sys
import io
from bs4 import BeautifulSoup as bs
# beautifulsoup BS대문자임에 주의(실수함)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html>
<body>
<h1> h1</h1>
<p>p1</p>
<p>p2</p>
</body>
</html>
"""

soup = bs(html,"html.parser")
# print('soup',type(soup))

h1 = soup.html.body.h1
print('h1',h1)
# /html파일에서 html -> body > h1 tag 방향으로  (계층구조상)
#  h1 <h1> h1</h1>- >이렇게 가져옴   ->tag안에 있는 실제 data를 가져오려면 h1.string을 해야함

p1 = soup.html.body.p
print('p1',p1)
# /html파일에서 html -> body > p1 tag 방향으로  (계층구조상)
# p1 <p>p1</p>

p2 = p1.next_sibling.next_sibling
print('p2',p2)
# 아무것도 이상하게 안나타남
# Enter를 쳐서 줄바꿈되어서, 그래서 next_sibling을 1번더 필요로함


p3 = p1.previous_sibling.previous_sibling
# p2 = p1.next_sibling.next_sibling  (2번이동하면 앞으로 가게 h1으로 가게됨ㄴ)
print('p3',p3)
# p3 <h1> h1</h1>

print("h1>>",h1.string)
print("p1>>",p1.string)
print("p2>>",p2.string)
