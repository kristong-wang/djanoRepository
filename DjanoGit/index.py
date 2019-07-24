from django.http import HttpResponse


def index(request):
    print('python test')
    return HttpResponse('Hello')