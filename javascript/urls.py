from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'javascript.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^all_pokemon/$', 'pokemon.views.all_pokemon', name='all_pokemon'),

    url(r'^admin/', include(admin.site.urls)),
)
