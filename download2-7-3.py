#  인프런 사이트 추천강좌  (Site가 개편되었음 )
# bootstrap으로 만들었음
# https://www.inflearn.com/추천-강좌  -> 주소 이름이 한글임



from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import urllib.parse as rep     # 제목 한글 때문에 필요


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# url을 2부분으로 나우서 정리함
base = "https://www.inflearn.com/추천-강좌"
quote=rep.quote_plus("추천-강좌")
print(quote)

url = base + quote

res = req.urlopen(url).read().decode('euc-kr','replace').encode('utf-8','replace')
soup = BeautifulSoup(res, "html.parser")




recommend = soup.select("ul.slides")[0]

for e in recommend:
    print(e.select_one("h4.block_titile > a").string)



for i,e in enumerate(recommend,1):
    print(i, e.select_one("h4.block_titile > a").string)
