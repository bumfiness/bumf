from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='bumf API')

urlpatterns = [
    url(regex=r'^auth/', view=include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/$', schema_view),
    url(regex='', view=include('bumf.api.urls', namespace='api')),
]
