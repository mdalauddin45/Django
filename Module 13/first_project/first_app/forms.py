from django import forms
# widgets == field to html input 

class contactForm(forms.Form):
    name = forms.CharField(label="Full Name: ", initial="alauddin", help_text="Total length must be within 70 characters", required=False, widget=forms.Textarea(attrs={'id': 'text_area','class':'class1 class2','placeholder':'Enter Your name'}))
    file = forms.FileField(label="file")
    email = forms.EmailField(label="Email address")
    age = forms.IntegerField(label="Age")
    weight = forms.FloatField(label="Weight")
    balance = forms.DecimalField(label="Balance")
    checked = forms.BooleanField(label="Check")
    birthday = forms.DateField(label="Birthday",widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(label="Appointment",widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('S', 'smail'),('M', 'Medium'),('L', 'large')]
    ratting = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    meal = [('P', 'Pepperoni'),('M', 'Masrum'),('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=meal, label="Pizza",widget=forms.CheckboxSelectMultiple)