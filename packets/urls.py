from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('chapter/<int:pk>', views.ChapterView.as_view(), name='chapter-view'),
    path('chapter/', RedirectView.as_view(url='/')),
]
