from django.urls import path

from tag.views import TagListView

urlpatterns = [
    path('list', TagListView.as_view(), name='tag-list')
]
