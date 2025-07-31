from django.urls import path

from category.views import CategoryListView

urlpatterns = [
    path('list', CategoryListView.as_view(), name='category-list')
]
