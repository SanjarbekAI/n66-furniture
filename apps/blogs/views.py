from django.views.generic import TemplateView


class BlogsListView(TemplateView):
    template_name = 'blogs/blogs-list.html'
