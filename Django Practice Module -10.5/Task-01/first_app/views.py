from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    d = {
        'author': 'Rahim', 'age': 10,'address': 'i’m Jai',
        'list': [ 1,32,3,4,5,6,7,8,9,10,11,12,13,14],
        'lst': ['python', 'is', 'fun'],
        'string': 'String with spaces',
        'date': datetime.datetime.now(),
        'time': datetime.datetime.now(),
        'blog_date': '1 June 2006',
        'comment_date': '08:00 on 1 June 2006',
        'empty': "the empty string",
        'divisibleby': 21,
        'size': 123456789,
        'name': 'My Name is Jai',
        'title': 'my FIRST post',
        'hello': 'Jai is a slug',
        'number': [
            'one',
            'two',
            'three',
        ],
        'dictsort':[
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
                    ],
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
    return render(request,'home.html',d)

def earthlyblog(request):
    blog = {
        'author': 'rahim', 'age': 10,'address': 'i’m Jai',
        'list': ['a', 'b', 'c'],
        'lst': ['python', 'is', 'fun'],
        'lists': [1,2,3],
        'date': datetime.datetime.now(),
        'empty': "the empty string",
        'string': 'String with spaces',
        'time': datetime.datetime.now(),
        'course': 'django',
        'published':'10 AM on 1 January 2023',
        'joe': 'Joseph is a developer',
        'blog_date': '1 June 2006',
        'comment_date': '08:00 on 1 June 2006',
        'divisibleby': 21,
        'size': 123456789,
        'name': 'My Name is Jai',
        'title': 'my FIRST post',
        'hello': 'Jai is a slug',
        'number': [
            'one',
            'two',
            'three',
        ],
        'dictsort':[
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
                    ],
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
    return render(request,'earthlyblog.html',blog)