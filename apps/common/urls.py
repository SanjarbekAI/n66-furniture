from django.urls import path

from apps.common.views import HomeTemplateView

app_name = 'common'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home')
]
