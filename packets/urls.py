from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('chapter/<int:pk>', views.ChapterView.as_view(), name='chapter-view'),
]
