from __future__ import print_function
import random
import time

from django.core.management.base import BaseCommand

from lights.models import LightSample


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            while True:
                print('Collecting a sample...')
                # TODO: Connect to an Arduino via PySerial and measure a sample.
                # Fake a data sample.
                state = random.choice([True, False])
                print('Fake Arduino is {}'.format('on' if state else 'off'))
                LightSample.objects.create(state=state)
                time.sleep(1)
        except KeyboardInterrupt:
            print('\nBye.')
