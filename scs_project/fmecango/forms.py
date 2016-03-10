from fmecango.models import *
from django.forms import ModelForm

class TableForm(ModelForm):
  # add bootstrap class to each field
  def __init__(self, *args, **kwargs):
    super(TableForm, self).__init__(*args, **kwargs)
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'form-control'
  class Meta:
    model = Table
    fields = '__all__'
    exclude = ['slug']

class ComponentForm(ModelForm):
  # add bootstrap class to each field
  def __init__(self, *args, **kwargs):
    super(ComponentForm, self).__init__(*args, **kwargs)
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'form-control'
  class Meta:
    model = Component
    fields = '__all__'
    exclude = ['table']

class FailureModeForm(ModelForm):
  # add bootstrap class to each field
  def __init__(self, *args, **kwargs):
    super(FailureModeForm, self).__init__(*args, **kwargs)
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'form-control'
  class Meta:
    model = FailureMode
    fields = '__all__'
    exclude = ['risk']