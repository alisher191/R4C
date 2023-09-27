from django.urls import path

from .views import AddRobotView, RobotsListView

app_name = 'robots'

urlpatterns = [
    path('add/', AddRobotView.as_view(), name="add-robot"),
    path('list/', RobotsListView.as_view(), name="list-robot"),
]