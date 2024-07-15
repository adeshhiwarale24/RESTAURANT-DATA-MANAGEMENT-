from django.core.management.base import BaseCommand
from restoapp.models import resto,dish
import os
import pandas as pd
from django.conf import settings

class Command(BaseCommand):
    help = 'Import external csv file data into Django database'

    def handle(self, *args, **kwargs):
        data_dir=os.path.join(settings.BASE_DIR,'data')
        csv_filepath=os.path.join(data_dir,'restaurants_small.csv')
        df = pd.read_csv(csv_filepath)
        list_csv = [list(x) for x in df.values]
        for item in list_csv:
            resto.objects.create(
                rid=item[0],
                name=item[1],
                location=item[2],
                items=item[3],
                lat_long=item[4],
                full_details=item[5]
            )

        for item in list_csv:
            items=item[3]
            id=item[0]
            dict1=eval(items)
            for k,v in dict1.items():
                dish.objects.create(
                    did=id,
                    dish=k,
                    mrp=v )



