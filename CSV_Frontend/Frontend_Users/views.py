from django.contrib.auth.forms import AuthenticationForm
from CSV_Backend.Schemas.models import Schema
from django.contrib.auth import login

from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View


class HomePageView(View):
    """ Render Home Page """

    @staticmethod
    def get(request):
        schemas = Schema.objects.all()
        return render(request, 'home.html', {'schemas': schemas})


class UserLoginView(View):
    """ Login with data """
    template_name = 'login/login.html'

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})
