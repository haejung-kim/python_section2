from shutil import copyfile
from os import listdir, makedirs
from os.path import isdir

# listdir -> os.path에서 가져옴 -> 경로안에 모든파일을 List로 반환
# makedirs(폴더 생성)
# isdir(폴더가 이미 존재하는지 확인)
# copyfile -> 파일 복사
# TEST_2017-04-03_10-23-43  --> 2017폴더안에 -> 4월 폴더 -> 3일폴더 이런식정리

orig_dir = "D:/Python/scandata/"
out_dir  = "D:/Python/organized/"

file_list = listdir(orig_dir)

for f_name in file_list:
    f_date = f_name[5:-4]
    f_date = f_date.split('_')
    f_date = f_date[0]
    f_date = f_date.split('-')

    year  = f_date[0]
    month = f_date[1]
    day   = f_date[2]

    target_dir = out_dir + year + "/" + month + "/" + day
    if not isdir(target_dir):
        makedirs(target_dir)

    copyfile(orig_dir+f_name, target_dir+ "/" + f_name)
    print(orig_dir+f_name + " => " + target_dir+ "/" + f_name)
