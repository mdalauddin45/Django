from django.shortcuts import render
from category.models import Category
from card.models import Card
# Create your views here.
def home(request,category_slug=None):
    cards = Card.objects.all()
    if category_slug is not None:
        category = Category.objects.filter(slug=category_slug).first()
        if category:
            cards = Card.objects.filter(brand=category)
    categories = Category.objects.all()
    return render(request,'home.html',{'categories':categories, 'cards':cards})
