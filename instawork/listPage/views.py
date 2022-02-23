from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.template import loader
from .models import Member

def index(request):
    member_list = Member.objects.order_by('id')
    template = loader.get_template('listPage/index.html')
    context = {
        'member_list': member_list
    }
    return HttpResponse(template.render(context, request))