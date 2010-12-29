import os, sys
#sys.path.append('C:\Python26\Lib\site-packages\django')
sys.path.append('/home/pankaj/django_projects/sahyog')
sys.path.append('/home/pankaj/django_projects/sahyog/website')

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
