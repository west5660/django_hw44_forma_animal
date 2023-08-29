from django.shortcuts import render
from django.http import HttpResponse
from anketa.forms123 import*
# Create your views here.
def index(req):
    return render(req, 'index.html')
from anketa.forms123 import Nashaforma
from anketa.forms123 import Nashaforma2
def forma1(req):
    if req.method=='POST':
        name = req.POST.get('name')
        num = req.POST.get('num')
        output= '''<h1>Спасибо</h1> 
        <h2> Ваше имя -- {0} </h2>
        <h2> Ваше число -- {1} </h2>'''.format(name,num)
        return HttpResponse(output)
    else:
        anketa1=Nashaforma()
        data={'form':anketa1}
        return render(req,'forma.html',context=data)



def forma2(req):
    if req.method == 'POST':
        form = Nashaforma2(req.POST, req.FILES)
        name = req.POST.get('name')
        age = req.POST.get('age')
        poroda = req.POST.get('poroda')
        color = req.POST.get('color')
        food = req.POST.get('food')
        foto = req.FILES.get('foto')
        output = '''<h1>Спасибо</h1> 
           <h2> Ваше имя -- {0} </h2>
           <h2> Возраст -- {1} </h2>
           <h2>Порода -- {2}</h2>
           <h2>Цвет -- {3}</h2>
           <h2>Любимая еда -- {4}</h2>
           <h2>Фото --{5}</h2>'''.format(name, age, poroda, color, food, foto)
        context = {'name': name,'age': age,'poroda': poroda,'color': color,'food': food,'foto': foto,}
        return render(req, 'final.html', context)
    else:
        anketa1 = Nashaforma2()
        data = {'form': anketa1}
        return render(req, 'forma.html', context=data)

def forma3(req):
    if req.method == 'POST':
        k1=req.POST.get('k1')
        k2=req.POST.get('k2')
        k3=req.POST.get('k3')
        k4=req.POST.get('k4')
        k5=req.POST.get('k5')
        k6=req.POST.get('k6')
        k7=req.POST.get('k7')
        k8=req.POST.get('k8')
        k9=req.POST.get('k9')
        k10=req.POST.get('k10')


        print(k1,k2)
        output='''<h1>Спасибо</h1> 
           <h2> Число -- {0} </h2>
           <h2> Почта -- {1} </h2>
           <h2> Галочка -- {2} </h2>
           <h2> Проверка на человека -- {3} </h2>
           <h2> что то -- {4} </h2>
           <h2> айпи -- {5} </h2>
           <h2> файлы -- {6} </h2>
           <h2> картинки -- {7} </h2>
           <h2> каотинки -- {8} </h2>
           <h2> язык -- {9} </h2>'''.format(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10)
        return HttpResponse(output)
    else:
        anketa1=Nashaforma3
        data={'form':anketa1}
        return render(req, 'forma.html', context=data)

    pass
def upload(req):
    if req.method == 'POST':
        name=req.POST.get('name')
        img=req.FILES.get('img').read()
        file=open('anketa/static/upload/{0}.jpg'.format(name),'wb')
        file.write(img)
        fpath='upload/{0}.jpg'.format(name)
        data={'k1':name,'k2':fpath}
        return render(req,'endpage.html', context=data)
    else:
        anketa1 = uploadform()
        data = {'form': anketa1}
        return render(req, 'forma.html', context=data)



def page(req):
    if req.method == 'POST':
        k1 = req.POST.get('name')
        k2 = req.POST.get('poroda')
        k3 = req.POST.get('age')
        k4 = req.POST.get('color')
        k5 = req.POST.get('color1')
        k6 = req.POST.get('food')
        k7 = req.POST.get('email')
        k11 = req.POST.get('name1')
        k12 = req.FILES.get('img').read()
        file = open('anketa/static/upload/{0}.jpg'.format(k11), 'wb')
        file.write(k12)
        fpath = 'upload/{0}.jpg'.format(k11)
        k8 = req.POST.get('clas')
        k9 = req.POST.get('robo')
        k10 = req.POST.get('dannie')
        # output = '''<h1>Данные приняты</h1>
        #            <h2> Имя -- {0} </h2>
        #            <h2> Порода -- {1} </h2>
        #            <h2> Возраст -- {2} </h2>
        #            <h2> Цвет -- {3} </h2>
        #            <h2> Вторичный окрас -- {4} </h2>
        #            <h2> Любимая еда -- {5} </h2>
        #            <h2>Почта -- {6} </h2>
        #            <h2> Класс животного -- {7} </h2>
        #            <h2> Фото -- {8} </h2>
        #            <h2> Проверка на бота -- {9} </h2>
        #            <h2> Согласие на обработку данных -- {9} </h2>'''.format(k1, k2, k3, k4, k5, k6, k7, fpath, k9, k10)
        # return HttpResponse(output)
        data={'k1':k1,'k2':k2,'k3':k3,'k4':k4,'k5':k5,'k6':k6,'k7':k7,'k8':k8,'k9':k9,'k10':k10,'k11':k11,'k12':fpath}
        return render(req,'endpge2.html', context=data)
    else:
        anketa1 = pageform()
        data = {'form': anketa1}
        return render(req, 'formapage.html', context=data)
    pass

