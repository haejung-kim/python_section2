# URLJOIN을 사용해서 절대경로는 묶어놓고, 상대경로쪽만 변경함

import sys
import io

from urllib.parse import urljoin
# urljoin 파악

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


baseURL="http://test.com/html/a.html"
print(">>",urljoin(baseURL,"b.html"))
print(">>",urljoin(baseURL,"sub/b.html"))
print(">>",urljoin(baseURL,"../index.html"))
print(">>",urljoin(baseURL,"../img/img.jpg"))

# >> http://test.com/html/b.html
# >> http://test.com/html/sub/b.html
# >> http://test.com/index.html     -> ..으로 1경로 위로 올라감
# >> http://test.com/img/img.jpg
