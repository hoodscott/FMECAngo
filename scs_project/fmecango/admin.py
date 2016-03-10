from django.contrib import admin
from django.db.models import get_models, get_app

from models import *

admin.site.register(Component)
admin.site.register(Table)
admin.site.register(FailureMode)
