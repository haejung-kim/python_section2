#  네이버 금융 TOP 10개 가져오기   (국내증시 상한가 top 10 )
# table 로 되어 있음

from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/sise/"
res = req.urlopen(url).read().decode('euc-kr','replace').encode('utf-8','replace')
soup = BeautifulSoup(res, "html.parser")


#  tag를 생략하고 id로 바로 찾음  , table 아래에 tbody 부분을 건너뛰고 바로 tr
top10 = soup.select("#siselist_tab_0 > tr ")

#  a tag가 들어간것에 종목(이름)이 존재해서 a tag로 filter
# for e in top10:
    # print(e.find("a"))

# for e in top10:
    # print(e.select_one(".tltle").string)

# None 있는 것을 제외해야 되어서  위의 결과 이용헤서 if문 활용
for e in top10:
    if e.find("a") is not None:
        print(e.select_one(".tltle").string)
