# ikb/views.py

from django.shortcuts import render
from .models import User
from .forms import AddForm

from keras.models import load_model
from keras.models import Model
import keras
import numpy as np

bird_kinds_txt = 'media/classes.txt'

f = open(bird_kinds_txt, 'r')
data = f.readlines()
f.close()

bird_kinds = {}

for i in data:
    i = i.split('.')
    i[1] = i[1].replace('\n', '')
    bird_kinds[int(i[0])] = i[1]


# Create your views here.
def add(request):
    user = 0
    bird_name = ''
    # 判断是否为 post 方法提交
    if request.method == "POST":
        af = AddForm(request.POST, request.FILES)
        # 判断表单值是否合法
        if af.is_valid():
            # name = af.cleaned_data['name']
            headimg = af.cleaned_data['headimg']
            # user = User(name=name, headimg=headimg)
            user = User(headimg=headimg)
            user.save()
            # bird_img_path = 'E:/Projects/SoftwareEngineering/Birds_Identification/I_Know_Birds/media/img/' + headimg.name
            bird_img_path = 'media/img/' + headimg.name

            # image_temp = Image.open(bird_img_path)

            filepath = "media/bvgg16.hdf5"
            model = load_model(filepath)
            model.summary()
            for i in model.layers:
                print(i.name)

            imgpath = bird_img_path
            test_img = keras.preprocessing.image.load_img(imgpath, target_size=(224, 224, 3))
            test_img = keras.preprocessing.image.img_to_array(test_img)
            test_img = test_img
            test_img = np.expand_dims(test_img, 0)
            pred = model.predict(test_img)
            result = max(pred[0])
            count = pred.argmax()
            print(result)
            print(count)

            bird_name = bird_kinds[count]

    af = AddForm()

    context = {'site_name': 'I Know Birds 鸟类识别平台',
               'github_url': 'https://github.com/MakeItPossible-MJT/Birds_Identification',
               'copyright': 'I Know Birds 鸟类识别平台 - 软件工程第五小组',
               "af": af,
               "user": user,
               "bird_name": bird_name}

    return render(request, 'ikb/index.html', context)
