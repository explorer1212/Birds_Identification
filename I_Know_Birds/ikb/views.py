# ikb/views.py
# Create your views here.

from django.shortcuts import render
from .models import User
from .forms import AddForm

from keras.models import load_model
# from keras.models import Model
import keras
import numpy as np

# 读取Classes.txt文件，其中保存着序号对应的鸟类名字
bird_kinds_txt_path = 'media/classes.txt'
bird_kinds = {}  # 以字典的形式储存，序号(int)对应名字(str)
bird_kinds_openfile = open(bird_kinds_txt_path, 'r')
bird_kinds_data = bird_kinds_openfile.readlines()
bird_kinds_openfile.close()
for num_name in bird_kinds_data:
    num_name = num_name.split('.')  # Classes.txt 中鸟类名字以 num.name 形式储存
    num_name[1] = num_name[1].replace('\n', '')  # 删除结尾的换行符\n
    bird_kinds[int(num_name[0])] = num_name[1]


def ikb_index(request):
    user = 0
    bird_name = ''
    af = AddForm()
    # 判断是否为 post 方法提交
    if request.method == "POST":
        # POST时也就是有图片上传，此时需要进行鸟的识别
        af = AddForm(request.POST, request.FILES)
        # 判断表单值是否合法
        if af.is_valid():
            # name = af.cleaned_data['name']
            bird_img = af.cleaned_data['Bird_Img']
            user = User(headimg=bird_img)
            user.save()
            bird_img_path = 'media/img/' + bird_img.name

            # 鸟类识别部分，调用模型识别鸟
            model_path = "media/bvgg16.hdf5"
            model = load_model(model_path)
            model.summary()
            # for i in model.layers:
            #     print(i.name)
            img_path = bird_img_path
            test_img = keras.preprocessing.image.load_img(img_path, target_size=(224, 224, 3))
            test_img = keras.preprocessing.image.img_to_array(test_img)
            test_img = test_img
            test_img = np.expand_dims(test_img, 0)
            pred = model.predict(test_img)
            # result = max(pred[0])
            count = pred.argmax()

            # count即识别出的鸟类序号，在字典中找名字
            if count == 0 or count > 200:
                bird_name = '识别失败'
            else:
                bird_name = bird_kinds[count]

    context = {'site_name': 'I Know Birds 鸟类识别平台',
               'github_url': 'https://github.com/MakeItPossible-MJT/Birds_Identification',
               'copyright': 'I Know Birds 鸟类识别平台 - 软件工程第五小组',
               "af": af,
               "user": user,
               "bird_name": bird_name}

    return render(request, 'ikb/index.html', context)
