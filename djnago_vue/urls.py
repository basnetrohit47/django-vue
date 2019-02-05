from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'djnago_vue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
  url(r'^$', TemplateView.as_view(template_name='index.html')),

  url(r'^api_example', include('api_example.urls')),

]
