from django.http import HttpResponse


def index(request):
    print('python test')
    return HttpResponse('Hello')


def login(request):
    print('这是登录')
    return HttpResponse()

def register(requests):
    print('这是注册函数')
    return HttpResponse('注册成功')

