from django.urls import path

from todo.views import TestView

urlpatterns = [
    path('test', TestView.as_view(), name='test')
]
