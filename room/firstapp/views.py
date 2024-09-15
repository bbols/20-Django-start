# views.py
from django.shortcuts import render
from .forms import FirstForm
from .models import Room
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView):
    template_name = "firstapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = f'MESSAGE: Приветствую на сайте, просмотра моих домашних комнат!'
        return context

class RoomView(LoginRequiredMixin,ListView):

    template_name = "firstapp/room.html"
    model=Room
    context_object_name = 'room'
    paginate_by = 1

####TemplateView
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['room'] = Room.objects.all()
#        return context

    def get_queryset(self):
        #tag_name = self.kwargs.get('room',None)
        return Room.objects.prefetch_related("doors","windows","furniture").all()


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