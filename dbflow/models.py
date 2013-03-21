from django.db import models
from django.forms import ModelForm
# Create your models here.


class Field(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True)
    field_type = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class Step(models.Model):
    root = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=3250, blank=True)
    field = models.ManyToManyField(Field, blank=True, verbose_name="field in form")
    request_url = models.CharField(max_length=250, blank=True)
    
    #instrument = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Answer(models.Model):
    # user
    field = models.ForeignKey(Field, verbose_name="field in form")
    answer = models.CharField(max_length=250)


class FieldForm(ModelForm):
    class Meta:
        model = Field

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
