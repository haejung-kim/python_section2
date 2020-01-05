import sys
import io
import urllib.request as req

from urllib.parse import urlparse
# urllib.parse (packag) 중에서 urlparse를 가져옴

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com"
mem = req.urlopen(url)

print(type(mem))
# 자료형(type)  tuple, dictory를 아래같이 확인도 가능함
# print(type({}))
# print(type([]))
# print(type(()))

#print("geturl",mem.geturl())
print("status",mem.status)
print("headers",mem.getheaders())
print("info",mem.info())
print("code",mem.getcode())
print("read",mem.read())
print("read",mem.read(50))
print("read",mem.read(50).decode("utf-8"))

# method를 통해서 정보를 확인하기
# geturl(url정보를 가져옴), status(200:success , 403,404, 500)
# mem.read -> memory에 적재된 html code를 보여줌
# read(50) -> 50개만 가져옴
# read할때 decode 함수 같이 사용 함 (글가가 깨어질때 같이 사용하기)  -> 이방법대로 하면 문자열 너무 클때는 decoding할때 error 날수 있다.


print(urlparse("http://www.encar.com"))
print(urlparse("http://www.encar.com?test=test"))
# urlparse를 사용했을때
# 결과  --> ParseResult(scheme='http', netloc='www.encar.com', path='', params='', query='', fragment='')
# 결과 (?test=test)를 주었을때 --> ㄴParseResult(scheme='http', netloc='www.encar.com', path='', params='', query='test=test', fragment='')
