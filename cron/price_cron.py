import os
import sys
import django
import requests


def get_external_petrol_price():
    from store.models import Price
    updated_ids = []
    url = ''
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
    else:
        json_data = response.json()
        for data in json_data:
            for price in data['prices']:
                price_objects_updated = Price.objects.update_or_create(petrol_station_id=data['id'],
                                                                       name=price['name'],
                                                                       defaults={'name': price['name'],
                                                                                 'cost': price['cost'],
                                                                                 'currency': price['currency']})
                updated_ids.append(price_objects_updated[0].id)
        Price.objects.exclude(id__in=updated_ids).delete()


if __name__ == "__main__":
    sys.path.append(os.getcwd().rsplit("/", 1)[0])
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'tatneftazs.settings')
    django.setup()
    get_external_petrol_price()
