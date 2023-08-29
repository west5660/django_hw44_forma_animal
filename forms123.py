from django import forms
from colorfield.fields import ColorField

class Nashaforma(forms.Form):
    name=forms.CharField(label='Ваше имя')
    num=forms.IntegerField(label='Номер', required=False, max_value=100, initial=12,help_text='werwer')

class Nashaforma2(forms.Form):
    name = forms.CharField(label='Имя животного')
    age = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))
    poroda = forms.CharField(label='Порода')
    color = forms.CharField(label='Цвет', widget=forms.TextInput(attrs={'type': 'color'}))
    food = forms.CharField(label='Любимая еда')
    foto = forms.ImageField(label='Изображение животного')

class Nashaforma3(forms.Form):
    k1=forms.DecimalField(label='десятичнык числа')
    k2=forms.EmailField(label='проверяет чтобы собака была в почте')
    k3=forms.BooleanField(label='галочка для отправки',required=False)
    k4=forms.NullBooleanField(label='Вычеловек')
    k5=forms.URLField(label='адрес в инете', help_text='http://www.el.ru')
    k6=forms.GenericIPAddressField(label='ip adress',required=False)
    k7=forms.FilePathField(label='выбери файл', path='C:\\Python39', allow_folders=True, match='.*\.txt')
    k8=forms.ImageField(label='картинка')
    k9=forms.FileField(label='Файл')
    vibor=((2,'En'),(1,'Ru'),(3,'Fr'))
    k10=forms.TypedChoiceField(label='выбор', choices=vibor)
    pass

class uploadform(forms.Form):
    name=forms.CharField()
    img=forms.ImageField()

class pageform(forms.Form):
    name = forms.CharField(label='Имя животного')
    poroda = forms.CharField(label='Порода')
    age = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))
    color = forms.CharField(label='Цвет основной', widget=forms.TextInput(attrs={'type': 'color'}))
    color1 = forms.CharField(label='Вторичный окрас')
    food = forms.CharField(label='Любимая еда')
    email = forms.EmailField(label='Почта')
    vibor = (('Ракообразные', 'Ракообразные'), ('Млекопитающие', 'Млекопитающие'), ('Земноводные', 'Земноводные'),('Рыбы','Рыбы'),('Птицы','Птицы'))
    clas = forms.TypedChoiceField(label='Выберите класс животного', choices=vibor)
    name1=forms.CharField(label='Подпись фото')
    img = forms.ImageField(label='Загрузите фото')
    robo = forms.NullBooleanField(label='Вы не робот?')
    dannie = forms.BooleanField(label='Согласие на обработку и хранение данных', required=False)
    aa=forms.NullBooleanField()
