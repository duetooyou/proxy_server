import os
import sys
from io import BytesIO
import django
import requests


def delete_current_services(api_data):
    from store.models import PetrolStore, Service
    current_services = list(PetrolStore.objects.get(id=api_data['id']).services.values_list('name', flat=True))
    for service in current_services:
        if service not in api_data['services']:
            service_object = Service.objects.get(name=service)
            service_object.petrols.remove(api_data['id'])


def get_external_image(urls, petrol_station_id):
    from django.core import files
    from store.models import Image, PetrolStore

    Image.objects.all().delete()
    for image_url in urls:
        response = requests.get(image_url, stream=True)
        if response.status_code != requests.codes.ok:
            buffer = BytesIO()
            buffer.write(response.content)
            file_name = image_url.split("/")[-1]
            image = Image()
            image.petrol_station = PetrolStore.objects.get(id=petrol_station_id)
            image.file.save(file_name, files.File(buffer))


def get_station_external_data():
    from store.models import Image, PetrolStore, Service
    api_ids_list = []
    url = ''
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
    else:
        json_data = response.json()
        for data in json_data:
            print(data)
            api_ids_list.append(data['id'])
            if PetrolStore.objects.filter(id=data['id']).exists():
                PetrolStore.objects.filter(id=data['id']).update(coordinate=data['coordinates'],
                                                                 number=data['number'],
                                                                 address=data['address'])
            else:
                PetrolStore.objects.create(id=data['id'],
                                           coordinate=data['coordinates'],
                                           number=data['number'],
                                           address=data['address'])
            if data['services']:
                for _name in data['services']:
                    delete_current_services(api_data=data)
                    if Service.objects.filter(name=_name).exists():
                        service_object = Service.objects.get(name=_name)
                        service_object.petrols.add(data['id'])
                    else:
                        service_object = Service.objects.create(name=_name)
                        service_object.petrols.add(data['id'])
            else:
                PetrolStore.objects.get(id=data['id']).services.clear()
            if data['urls']:
                get_external_image(data['urls'], data['id'])
        ids_diff = set(i.id for i in PetrolStore.objects.iterator()) - set(api_ids_list)
        PetrolStore.objects.filter(id__in=ids_diff).delete()


if __name__ == "__main__":
    sys.path.append(os.getcwd().rsplit("/", 1)[0])
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'tatneftazs.settings')
    django.setup()
    get_station_external_data()
