import sae
from assetm import wsgi

application = sae.create_wsgi_app(wsgi.application)
