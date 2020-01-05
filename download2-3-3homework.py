import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgURL="https://ssl.pstatic.net/tveta/libs/1255/1255598/5073cd72179dae7dd40a_20190918183344631.jpg"
htmlURL="https://tvetamovie.pstatic.net/libs/1247/1247997/cb2d5a26f715368d6fc5_20190911120707402.mp4-pBASE-v0-f91352-20190911120732085.mp4"
#  URL 주소만 변경


savePath1 = "d:/naver01.jpg"
savePath2 = "d:/index.mp4"
# 동영상일때 .mp4로 변경함

dw.urlretrieve(imgURL,savePath1)
dw.urlretrieve(htmlURL,savePath2)

print("다운로드 완료")
