from django.urls import path

from apps.blogs.views import BlogsListView

app_name = 'orders'

urlpatterns = [
    path('', BlogsListView.as_view(), name='blogs')
]
