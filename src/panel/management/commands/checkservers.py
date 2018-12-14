from django.core.management.base import BaseCommand, CommandError
from panel.actions import *



class Command(BaseCommand):
    help = 'Displays current time'
    
    def handle(self, *args, **kwargs):
        checkservers()
        
