import requests
import re
import os

r = requests.get('http://jw.hljit.edu.cn/CheckCode.aspx')


#获取链接括号值
codes = re.findall('\((.*?)\)', r.url)
if len(codes)>0 :
    print(codes[0])
    code = codes[0]
else :
    #考虑服务器问题，或者超时，解决方案：可以重试
    print("ERROR")

imgurl = 'http://jw.hljit.edu.cn/('+code+')/CheckCode.aspx'
print(imgurl)
pic = requests.get(imgurl)
with open('D:\\picture.jpg', 'wb') as file:
    file.write(pic.content)

#打开图片
os.system('start D:\\picture.jpg')    

#等待键入验证码
yzm = input("打开图片并键入验证码:")

xh = input("输入学号:")

mm = input("输入密码:")

loginurl = "http://jw.hljit.edu.cn/("+code+")/default2.aspx"

payload = {'__VIEWSTATE': 'dDwyODE2NTM0OTg7Oz4QCHzdbACmhpLxcAdbBMPGnnBr2g==', 'txtUserName': xh, 'TextBox2': mm, 'txtSecretCode': yzm, 'RadioButtonList1': "%D1%A7%C9%FA", 'Button1': '', 'lbLanguage': '', 'hidPdrs': '', 'hidsc': ''}  
header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ', 'Referer': loginurl,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}  

#禁止自动重定向
r = requests.post(loginurl, data=payload,allow_redirects=False)

if r.status_code == 302:
    print("登陆成功")
    #主页链接测试
    main_url = "http://jw.hljit.edu.cn/("+code+")/xs_main.aspx?xh="+xh
    r1 = requests.get(main_url)
    print("主页信息代码：",r1.text);
else :
    print("登陆失败")