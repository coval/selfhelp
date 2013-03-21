# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
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
    c['step_id'] = step_id
    form = FieldForm()
    # print(c)
    c['form'] = form.as_p()
    return render_to_response('step_display.html', c, context_instance=RequestContext(request) )


def post_redirect(request, step_id=0):

    if request.method == 'POST':
        print(request.POST)
        nextstep = request.POST['next_step']
        #for field in request.POST
        #    form_fields = request.POST['']

    return HttpResponseRedirect('/start/%s/'%int(nextstep))
