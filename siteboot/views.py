from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req, 'index.html')

def chokolate(req, id):
    id = int(id)
    name = ''
    img = ''
    text = ''
    if id == 0:
        name = 'Snickers'
        img = 'img/snickers.jpg'
        text = 'Не тормози - сникерсни'
    elif id == 1:
        name = 'Mars'
        img = 'img/mars.jpg'
        text = 'Не тот Марс, другой Марс'
    elif id == 2:
        name = 'Nuts'
        img = 'img/nuts.jpg'
        text = 'Гора орехов'
    data = {'id': id, 'name': name, 'img': img, 'text': text}
    return render(req, 'prochoko.html', context=data)