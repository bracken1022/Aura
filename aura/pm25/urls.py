
from django.conf.urls import url
from django.views.generic import TemplateView

from pm25.api.pm_data_show import data_show, data_show_cities


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html') ),
    url(r'^api/dataShow$', data_show, name='dataShow'),
    url(r'^api/dataShow/cities$', data_show_cities, name='dataShowCities'),
]
