from django.http import HttpResponse

def home(request):
    return HttpResponse('this is my home')
def contact(request):
    return HttpResponse("Contact page")