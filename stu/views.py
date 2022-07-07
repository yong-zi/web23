from django.shortcuts import render
from django.views import View
from stu.models import *
from django.core import serializers
from django.http import JsonResponse

class CityView(View):
    def get(self, request): # 先渲染页面，用get方法

        return render(request,'city.html')


def getInfo(request):
    # 获取父id
    pid1 = request.GET.get('pid',-1) # 获取页面传进来的pid
    pid1 = int(pid1)                  # 对pid进行转型

    cityList = City.objects.filter(pid = pid1)
    jcityList = serializers.serialize('json', cityList) # 将cityList转换为Json格式数据

    return JsonResponse({'jcityList':jcityList})


