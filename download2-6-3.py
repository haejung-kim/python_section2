# 함수정의

from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# food-list.html 파일열기  (한글이니 안전하게 utf-8 )
fp=open("cars.html", encoding="utf-8")

soup=BeautifulSoup(fp, "html.parser")

# ﻿<ul id="cars">
  # <li id="ge">Genesis</li>
  # <li id="av">Avante</li>
  # <li id="so">Sonata</li>
  # <li id="gr">Grandeur</li>
  # <li id="tu">Tucson</li>z
# </ul>


#  selector 입력받고 - 바로  호출 하는 함수 이용
def car_func(selector):
    print("car_func", soup.select_one(selector).string)

car_func("#gr")
car_func("li#gr")
car_func("ul>li#gr")
car_func("#cars #gr")
car_func("#cars > #gr")
car_func("li[id='gr']")

print(soup.select("li")[3].string)

print("car_func", soup.find_all("li")[3].string)


#  람다식  -> 코드를 간결하게 함
# 함수 이름 =  lambda 인자 : 표현식

car_lambda = lambda selector : print("car_lambda", soup.select_one(selector).string)
car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul>li#gr")
car_lambda("#cars #gr")
car_lambda("#cars > #gr")
car_lambda("li[id='gr']")
