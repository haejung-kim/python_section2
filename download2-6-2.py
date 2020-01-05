# 다양한 방법을 통한 예제
# select_one, select
# find, find_all

from bs4 import BeautifulSoup
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# food-list.html 파일열기  (한글이니 안전하게 utf-8 )

fp=open("food-list.html", encoding="utf-8")

soup=BeautifulSoup(fp, "html.parser")

# li의 자식중 몇번째를 선택, nth-of-type(몇번째 자식 ) t????실패
# print("1", soup.select_one("li:nth-of-type(8)").string)


#   > (자식선택자)   nth-of-type(몇번째 자식 )
print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)

#3    #-> id(ac-list)중에
# select -> 배열이라서 .string으로 불러오면 안됨 [0].string
print("3", soup.select ("#ac-list > li[data-lo='cn']")[0].string)

# ex4  #-> id(ac-list)중에
 # -> alcohol high (띠워서 Html에서 그렇더라도) -> 여기서는alcohol.high로 표현
print("3", soup.select ("#ac-list > li.alcohol.high")[0].string)


#ex5) dictionary
param={"data-lo": "cn", "class":"alcohol"}
print("5", soup.find("li",param).string)

print("6", soup.find(id="ac-list").find("li",param).string)


# ex6) 바로 find_all로 하기
for ac in soup.find_all("li") :
    if ac['data-lo'] == 'us' :
        print('data-lo == us', ac.string)
