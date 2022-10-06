from django.http import HttpResponse
from django.views.generic import TemplateView

def home(request):
    return HttpResponse("<h1>This is home page</h1>")

class HomeView(TemplateView):
    template_name = 'index.html'