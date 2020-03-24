from datetime import date,timedelta
from random import randint
#准备10个人姓名，然后为这10个人随机生成生日
def init_data(nameList):
    dic = {}.fromkeys(nameList)
    print("生成字典：",dic)
    for key in dic:
        year = randint(1990,1999)
        month = randint(1,12)
        day = randint(1,30)
        dic[key] = date(year,month,day)
    print("初始化数据后：",dic)
    return dic
#需求一：统计出那些人是夏季（6月-8月）出生的
def get_summer_person(dic):
    li = []
    for key in dic:
        if dic[key].month>=6 and dic[key].month<=8:
            li.append(key)
    return li
#需求二：最大的比最小的大多少天
def get_person_year_max(dic:dict):
    birthdayList = list(dic.values())   # 在字典中提取出生日
    birthdayList.sort()
    max_birthday = birthdayList[0] # 获取最大年龄
    for key in dic: # 遍历
        if dic[key] == max_birthday:
            return key

def get_person_year_min(dic: dict):
    birthdayList = list(dic.values())  # 在字典中提取出生日
    birthdayList.sort()
    min_birthday = birthdayList[-1] # 获取最小的年龄
    for key in dic: # 遍历
        if dic[key] == min_birthday:
            return key

def get_days(dic):
    birthdayList = list(dic.values())
    birthdayList.sort()
    old = birthdayList[0]
    young = birthdayList[-1]
    days = (young-old).days
    return days
#需求三：谁的生日最早，谁的生日最晚
def get_person_birth_max(dic:dict):
    person_birth = list(dic.values())   # 在字典中提取出生日
    for i in range(len(person_birth)):
        person_birth[i] = person_birth[i].replace(year=1990)
    person_birth.sort()
    print(person_birth)
    max_birthday = person_birth[-1] # 获取最大的生日
    for key in dic: # 遍历
        if dic[key].month == max_birthday.month and dic[key].day == max_birthday.day:
            return key
def get_person_birth_min(dic: dict):
    person_birth = list(dic.values())  # 在字典中提取出生日
    for i in range(len(person_birth)):
        person_birth[i] = person_birth[i].replace(year=1990)
    person_birth.sort()
    print(person_birth)
    min_birthday = person_birth[0] # 获取最小的生日
    for key in dic: # 遍历
        if dic[key].month == min_birthday.month and dic[key].day == min_birthday.day:
            return key

if __name__ == '__main__':
    list_name = ["赵一", "杨二", "张三", "李四", "王五", "赵六", "马七", "郑八", "刘九", "胡十"]
    data= init_data(list_name)
    #需求一：统计出那些人是夏季（6月-8月）出生的
    persons = get_summer_person(data)
    print("夏季出生:",persons)
    # 需求二：最大的比最小的大多少天max
    print("年龄最大：",get_person_year_max(data))
    print("年龄最小：",get_person_year_min(data))
    days = get_days(data)
    print("相差天数:",days)
    # 需求三：谁的生日最早，谁的生日最晚
    print("生日最早：",get_person_birth_min(data))
    print("生日最晚：",get_person_birth_max(data))
