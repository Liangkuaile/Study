#注册
import os
os.chdir('E:\学习资料\python')
f=open('user.txt','a+')
f.seek(0)  #移到开头
user=eval(f.read())
i=0
while i<3:
    i+=1
    username=input('please input the regist user name').strip()
    password=input('please input the regist password').strip()
    spassword=input('please ensure you password ').strip()
    if len(username)==0:
        print("the username is empty")
        continue
    elif len(password)==0:
        print("the password is empty")
        continue
    elif len(spassword)==0:
        print("the spassword is empty")
        continue
    elif spassword!=password:
        print("the password is not same as the spassword")
        continue
    if username in user:
        print("the username has had")
        continue
    print("success to register")
    user[username]={'password':password}
    f.seek(0)
    f.truncate()    #清除原先的文本
    f.write(str(user))   #写入全部文本
    break
else:
    print("regist lose")
f.close()
#登陆
r=open('user.txt','r')
r.seek(0)  #移到开头
user=eval(r.read())
j=0
while j<3:
    j+=1
    username=input("please input the username")
    password=input("please input the password")
    if len(username)==0:
        print("the username can not be empty")
        continue
    elif len(password)==0:
        print("the password can not be empty")
        continue
    elif username not in user:
        print("your user name is not exist")
        continue
    elif password!=user[username]['password']:
        print("the password is error")
        continue
    print("success to log in")
    break
else:
    print("too many wrong password")
f.close()