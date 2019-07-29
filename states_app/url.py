from django.urls import path

from states_app.views import *


app_name = 'states_app'

urlpatterns = [
    path('', Municipality.as_view(), name='municipality'),
    path('/municipaly/show', Municipality.get_municipality, name='municipality_show'),
    path('/municipaly/show/<int:pk>/', Municipality.get_edit, name='municipality_get_edit'),
    path('/municipaly/update/$', Municipality.update, name='municipality_update'),
    path('/municipaly/delete/<int:pk>/', Municipality.delete, name='municipality_delete'),


    path('/states', Region.as_view(), name='states'),
    path('/states/show', Region.get_region, name='state_show'),
    path('/states/show/<int:pk>/', Region.get_edit, name='state_get_edit'),
    path('/states/update/$', Region.update, name='state_update'),
    path('/states/delete/<int:pk>/', Region.delete, name='state_delete'),


]