import logging
# from djangoProject.logger import logger
from django.test import TestCase

# Create your tests here.
from django.utils import log
import logging
log = logging.getLogger('django.request')
def some_view():
    log.info('123123')
some_view()