from django.http import HttpResponse


def index(request):
    print('python test')
    return HttpResponse('Hello')

def register(requests):
    print('这是注册函数')
    return HttpResponse('注册成功')