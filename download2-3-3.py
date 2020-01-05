#  2-3-2에서 API변수에 site이름, values에 내용만 바꾸면 될것 같다.

import sys
import io
import urllib.request as req

from urllib.parse import urlencode


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


API="https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
# XML Site 주소로 수정

values = {
 'ctxCd':'1012'
}
#  앞에 내용을 변경함

print('before',values)

params = urlencode(values)
print('after',params)

url = API +  "?" + params

print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력",reqData)
