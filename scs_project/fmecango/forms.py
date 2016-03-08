from fmecango.models import *

class ComponentForm(ModelForm):
  class Meta:
    model = Component
    fields = '__all__'

class ModeForm(ModelForm):
  class Meta:
    model = Mode
    fields = '__all__'