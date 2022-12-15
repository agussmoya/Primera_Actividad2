from django.shortcuts import render
from django.views.generic import TemplateView

def post_list(request):
    return render(request, 'blog/post_list.html', {})

class Error404 (TemplateView):
    template_name = "blog/error_404.html"

