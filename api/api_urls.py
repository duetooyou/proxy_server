from django.urls import path
from api.views import PetrolView

urlpatterns = [
    path('stations/', PetrolView.as_view())
]
