import os, sys
sys.path.append('/home/pankaj/workspace/sahyog')
sys.path.append('/home/pankaj/workspace/sahyog/website')

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
