# views.py
from django.shortcuts import render
from .forms import FirstForm
def index_view(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'firstapp/index.html',context)

def form_view(request):
    if request.method == 'POST':
        form=FirstForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']

            return render(request, 'firstapp/form.html', {'name': name, 'email': email})
    else:
        form=FirstForm()
        context = {
            'message': 'Hello Form!',
            'form':form
        }
    return render(request, 'firstapp/form.html',context)