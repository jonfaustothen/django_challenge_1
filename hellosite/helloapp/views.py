from django.shortcuts import render
from django.views import View

# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        return render(request=request, template_name='hello_world.html')

class HelloNameView(View):
    def get(self, request, name='world'):
        context = {'name': name}
        return render(request=request, template_name='hello_name.html', context = context)

class HelloGoodbyeView(View):
    def get(self, request):
        return render(request=request, template_name='goodbye.html')
        