# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import datetime
from dbflow.models import Field, Step, FieldForm, Answer, AnswerForm


def step_display(request, step_id=0):
    c = dict()
    now = datetime.datetime.now()
    if step_id:
        step = Step.objects.get(pk=step_id)
    	next_steps = Step.objects.filter(root=step)
    else:
        step=Step.objects.filter(root=None)
        next_steps = step

    fields = Field.objects.filter(step=step)
    
    c['next_steps'] = next_steps
    if getattr(step, "field", None):
    	c['fields'] = step.field.all()
    c['step'] = step
    form = FieldForm()
    # print(c)
    c['form'] = form.as_p()
    return render_to_response('step_display.html', c)


def post_redirect(request, step_id=0):


    return HttpResponseRedirect('/start/')
