import os
from celery import Celery
from django.conf import settings
import configurations

os.environ.setdefault(
  "DJANGO_SETTINGS_MODULE",
  "course4_proj.settings"
)
os.environ.setdefault(
  "DJANGO_CONFIGURATION",
  "Dev"
)

configurations.setup()

app = Celery("course4_proj")
#namespace="CELERY" to let celery knows the prefix of the settings in the settings.py file
app.config_from_object(
  "django.conf:settings", 
  namespace="CELERY"
  
)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)