from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests,json

# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'interface/index.html')

    elif request.method == 'POST':
        try:
            url = request.POST.get('url')
            request_url = requests.get(url)
            request_text = json.loads(request_url.text)
            print(request_url)
            print(request_text)
            print(type(request_text))
            return render(request, 'interface/index.html',
                          context={
                              'interface_url': request_url,
                              'interface_text': request_text,
                          })
        except requests.RequestException as e:
            print(e)
            return render(request, 'interface/index.html',
                          context={
                              'error_null': 'url不可为空或输入错误'
                          })
    else:
        return HttpResponse('提交失败')
