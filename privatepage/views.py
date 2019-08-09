from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class PrivatePageView(TemplateView):
    template_name = 'privatepage.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return self.render_to_response(ctx)