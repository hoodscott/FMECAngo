from fmecango.models import *
from django.forms import ModelForm

class TableForm(ModelForm):
  class Meta:
    model = Table
    fields = '__all__'

class ComponentForm(ModelForm):
  class Meta:
    model = Component
    fields = '__all__'

class FailureModeForm(ModelForm):
  class Meta:
    model = FailureMode
    fields = '__all__'