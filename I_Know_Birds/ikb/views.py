# ikb/views.py

from django.shortcuts import render
from .models import User
from .forms import AddForm


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
            bird_img_path = 'media/img/' + headimg.name

    af = AddForm()

    context = {'site_name': 'I Know Birds 鸟类识别平台',
               'github_url': 'https://github.com/MakeItPossible-MJT/Birds_Identification',
               'copyright': 'I Know Birds 鸟类识别平台 - 软件工程第五小组',
               "af": af,
               "user": user,
               "bird_name": bird_name}

    return render(request, 'ikb/index.html', context)
