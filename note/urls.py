from django.urls import path
from . import views
urlpatterns = [
    path('note',views.index,name='listN'),
    path('update_note/<str:pk>/',views.updateNote,name='update_Note'),
    path('delete_note/<str:pk>/',views.deleteNote,name='delete_Note')

    ]
