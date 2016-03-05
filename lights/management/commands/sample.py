from __future__ import print_function
import time

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            while True:
                print('Collecting a sample...')
                # TODO: Connect to an Arduino via PySerial and measure a sample.
                time.sleep(1)
        except KeyboardInterrupt:
            print('\nBye.')
