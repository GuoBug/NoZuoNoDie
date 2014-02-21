import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), 'record'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'record.settings'

import sae
from record import wsgi


application = sae.create_wsgi_app(wsgi.application)