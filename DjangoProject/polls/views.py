#-*- coding:utf-8 -*-

from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext,loader

from .models import Question,Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request,{
        'latest_question_list':latest_question_list,
    })
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
        question = Question.objects.get(pk =question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})
def results(request,question_id):
    result = get_object_or_404(Question,pk = question_id)
    return HttpResponse("you are looking at the results of question %s"%question_id)
def votes(request,question_id):
    return HttpResponse("you are looking at the votes of question %s"%question_id)
