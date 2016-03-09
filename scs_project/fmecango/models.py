from django.db import models

class Table(models.Model):
  name = models.CharField(max_length=128)
  slug = models.SlugField()
  
  def save(self, *args, **kwargs):
    if not self.id:
        # Newly created object, so set slug
        self.slug = slugify(self.name)

    super(Table, self).save(*args, **kwargs)

class Component(models.Model):
  name = models.CharField(max_length=128)
  function = models.CharField(max_length=128)
  table = models.ForeignKey(Table)

class FailureMode(models.Model):
  name = models.CharField(max_length=128)
  cause = models.CharField(max_length=128)
  effect= models.CharField(max_length=128)
  severity= models.IntegerField()
  occurence= models.IntegerField()
  detection= models.IntegerField()
  notes= models.CharField(max_length=128)
  
  component = models.ForeignKey(Component)