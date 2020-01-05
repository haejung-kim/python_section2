#  다음 실시간 10개 가져오기
from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/"

res = req.urlopen(url).read().decode('euc-kr','replace').encode('utf-8','replace')
soup = BeautifulSoup(res, "html.parser")

real = soup.select("div.hotissue_builtin")
print(real)

print()
print()
print()
real10 = soup.select("div.hotissue_builtin > li")

print(real10)
