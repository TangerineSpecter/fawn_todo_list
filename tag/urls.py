from django.urls import path

from tag.views import TagListView

urlpatterns = [
    path('', TagListView.as_view(), name='tag-list')
]
