shuxiang='猴鸡狗猪鼠牛虎兔龙蛇马羊'
yuefen=((1,19),(2,18),(3,20),(4,19),(5,20),(6,21),(7,22),(8,22),(9,22),(10,23),(11,22),(12,21))
xingzuo=("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天平座","天蝎座","射手座")
year = int(input('year年: \n'))
a= (shuxiang[year % 12])
print('你是属' + a + '的呦')
month = int(input('month月: \n'))
day = int(input('day日\n'))
b=filter(lambda x:x <= (month,day),(yuefen))
c=len(list(b))
print('星座是' + xingzuo[c])
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 <month < 12:
    sum =months[month -1]
else:
    print('err')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 !=0)):
    leap = 1
if (leap ==1 )and(month > 2):
    sum += 1
print ("你距离过生日还有"+str(sum)+"天！")