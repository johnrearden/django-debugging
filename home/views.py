from django.shortcuts import render
from django.views import View
from .forms import PersonForm


class HomeView(View):
    def get(self, request):
        form = PersonForm()
        context = {
            'form': form,
        }
        return render(request, 'home/home.html', {context})
