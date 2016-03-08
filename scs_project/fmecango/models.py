from django.db import models

# Create your models here.
class Component(models.Model):
  name = CharField()
  function = CharField()

class Mode(models.Model):
  name = CharField()
  cause = CharField()
  effect= CharField()
  severity= IntegerField()
  occurence= IntegerField()
  detection= IntegerField()
  notes= CharField()
  
  component = ForeignKey(Component'''add lookback''')