from django.urls import path
from . import views
urlpatterns = [
path("",views.entryData ,name='entrydata'),
path("delete/<int:id>/",views.delete_data,name='delete_data'),
path("<int:id>/",views.Update_data,name='Update_data'),
]