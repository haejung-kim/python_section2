# urlopen을 사용해서 저장  , open/write함수를 사용해서 저장

import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgURL="https://i.ytimg.com/vi/wEkWR-6aOcg/hqdefault.jpg"
htmlURL="http://google.com"

savePath1 = "d:/test1.jpg"
savePath2 = "d:/index.html"

f = dw.urlopen(imgURL).read()
#  memory에 read해옴 (url에서 가져와서 ) ,HDD에 쓰지는 않음

f2 = dw.urlopen(htmlURL).read()


saveFile1=open(savePath1,'wb')
# w(wtire), b(binary), 파일 생성을 위해서 open함수 사용
saveFile1.write(f)
saveFile1.close

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)
 # With 사용 -> 간격하게 3-> 2줄로 간격하게 가능  , as(alias) , 자동으로 close 되면 with를 벗어나면 자동으로 resource가 반납됨


print("다운로드 완료")
