from django.urls import path

from apps.blogs.views import BlogsListView

app_name = 'products'

urlpatterns = [
    path('', BlogsListView.as_view(), name='blogs')
]
