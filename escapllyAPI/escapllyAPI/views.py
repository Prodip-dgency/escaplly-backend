from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return HttpResponse("<h1>This is home page</h1>")


class HomeView(TemplateView):
    template_name = 'index.html'