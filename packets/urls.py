from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('chapter/<int:pk>', views.ChapterView.as_view(), name='chapter-view'),
    path('other/<int:pk>', views.OtherView.as_view(), name='other-view'),
    path('chapter/', RedirectView.as_view(url='/')),
    path('other/', RedirectView.as_view(url='/')),
    path('dev-notes/', views.DevView.as_view(), name='dev-view'),
    path('add-user/', views.AddUserView.as_view(), name='add-user-view'),
    path('add-video/', views.AddVideoView.as_view(), name='add-video-view'),
    path('advanced/', views.AdvancedView.as_view(), name='advanced-view'),

]
