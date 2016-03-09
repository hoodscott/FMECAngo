from fmecango.models import *
from django.forms import ModelForm

class TableForm(ModelForm):
  class Meta:
    model = Table
    fields = '__all__'
    exclude = ['slug']

class ComponentForm(ModelForm):
  class Meta:
    model = Component
    fields = '__all__'
    exclude = ['table']

class FailureModeForm(ModelForm):
  class Meta:
    model = FailureMode
    fields = '__all__'
    #exclude = ['component']