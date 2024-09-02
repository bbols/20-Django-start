# views.py
from django.shortcuts import render
from .forms import FirstForm
from .models import Room
from django.views.generic import TemplateView
from django.views.generic import FormView

class IndexView(TemplateView):
    template_name = "firstapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello World!'
        return context

class RoomView(TemplateView):
    template_name = "firstapp/room.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = Room.objects.all()
        return context

class FormViewCBV(FormView):
    template_name = "firstapp/form.html"
    form_class = FirstForm
    success_url = '/form/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        context= self.get_context_data(form=form,name=name,email=email)
#legacy code fbv
"""
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
"""