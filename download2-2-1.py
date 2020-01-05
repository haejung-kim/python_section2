# urlretrieve를 사용해서 파일로 저장

import sys
import io
import urllib.request as dw




sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgURL="https://i.ytimg.com/vi/wEkWR-6aOcg/hqdefault.jpg"
htmlURL="http://google.com"

savePath1 = "d:/test1.jpg"
savePath2 = "d:/index.html"


dw.urlretrieve(imgURL,savePath1)
dw.urlretrieve(htmlURL,savePath2)

print("다운로드 완료")
