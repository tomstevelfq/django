import json
from django.shortcuts import render,HttpResponse
from .models import User
#测试json
def save(stri,name):
    with open("data/"+name+".txt","w",encoding='utf-8') as f:
        f.write(stri)
        f.close()
        print("写入成功")
def index(request):
    return render(request,'index.html')
def TestJson(request):#接收前端的json数据
    print(request.method)
    str=request.body.decode()
    obj=json.loads(str)#接收json字符串
    #print(len(request.body.decode()))#存储
    print(obj['name'])
    save(str,obj['name'])
    return (HttpResponse("hello"))

def reJson(request):#向前端返回数据
    name=request.POST.get('name')
    print(name,request.method)
    f=open("data/"+name+".txt","r",encoding='utf-8')
    return(HttpResponse(f.read()))

def reg(request):
    mes=json.loads(request.body.decode())
    username=mes['username']
    passwd=mes['passwd']
    if(len(User.objects.filter(name=username))>0):
        return(HttpResponse('no'))
    user=User(name=username,passwd=passwd)
    user.save()
    return(HttpResponse('yes'))

