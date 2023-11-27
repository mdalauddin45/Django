from django.shortcuts import render

# Create your views here.

def home(request):
    d = {
        'author': 'Rahim', 'age': 5,
        'list': [ 1,32,3,4,5,6,7,8,9,10,11,12,13,14],
        'courses': [
            {
                'id': 1,
                'name': "python",
                'fee': 5000
            },
            {
                'id': 2,
                'name': "C++",
                'fee': 500
            },
            {
                'id': 3,
                'name': "django",
                'fee': 2500
            },
            
            
        ]
    }
    return render(request, 'home.html',d)