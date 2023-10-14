from django.urls import path
from .views import CarListByOwner,CarList,CarListCreate,CarDestroyView

urlpatterns = [
    path('all_cars/', CarList.as_view()),
    path('cars/owner/<uuid:owner_id>/', CarListByOwner.as_view(), name='cars_by_owner'),
    path('create/',CarListCreate.as_view(),name='CreateList'),
]
