from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .models import Robot
from .forms import RobotForm

class RobotsListView(ListView):
    model = Robot
    template_name = 'robots.html'
    context_object_name = 'robots'


class AddRobotView(CreateView):
    model = Robot
    form_class = RobotForm
    template_name = 'add_robot.html'
    success_url = reverse_lazy('robots:list-robot')
