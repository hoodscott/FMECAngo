from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Table(models.Model):
  name = models.CharField(max_length=128)
  diagram = models.ImageField(null=True, blank=True)
  slug = models.SlugField()
  
  def save(self, *args, **kwargs):
    if not self.id:
        # Newly created object, so set slug
        self.slug = slugify(self.name)

    super(Table, self).save(*args, **kwargs)
  
  def __unicode__(self):
    return self.name

class Component(models.Model):
  name = models.CharField(max_length=128)
  function = models.CharField(max_length=128)
  table = models.ForeignKey(Table)
  
  def __unicode__(self):
    return self.name

class FailureMode(models.Model):
  name = models.CharField(max_length=128)
  cause = models.CharField(max_length=128)
  effect= models.CharField(max_length=128)
  severity= models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
  occurence= models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
  detection= models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
  risk = models.IntegerField()
  notes= models.CharField(max_length=128, null=True, blank=True)
  
  component = models.ForeignKey(Component)
  
  def save(self, *args, **kwargs):
    if not self.id:
      # Newly created object, so set risk as per calculation
      self.risk = self.severity + self.occurence + self.detection

    super(FailureMode, self).save(*args, **kwargs)
  
  def __unicode__(self):
    return self.name