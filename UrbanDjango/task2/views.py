from django.shortcuts import render
from django.views import View


def func_template_view(request):
    return render(request, 'second_task/func_template.html')


class ClassTemplateView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')

