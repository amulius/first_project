from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from first_project import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'first_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'college_life.views.splash', name='splash'),
    url(r'^profile/$', 'college_life.views.profile', name='profile'),
    url(r'^stats/$', 'college_life.views.stats', name='stats'),
    url(r'^faq/$', 'college_life.views.faq', name='faq'),
    url(r'^map/$', 'college_life.views.map', name='map'),
    url(r'^zone/(?P<zone_id>\d+)/$', 'college_life.views.zone', name='zone'),
    url(r'^combat/$', 'college_life.views.combat_action', name='combat_test'),
    url(r'^win/$', 'college_life.views.combat_win', name='win'),
    url(r'^lose/$', 'college_life.views.combat_lose', name='lose'),
    url(r'^run/$', 'college_life.views.combat_run', name='run'),
    url(r'^dorm/$', 'college_life.views.dorm', name='dorm'),
    url(r'^bar/$', 'college_life.views.bar', name='bar'),
    # url(r'^movies/$', 'movie_mapper.views.movie_list', name='movie_list'),
    # url(r'^movies/search/$', 'movie_mapper.views.search_movie', name='search_movie'),
    # url(r'^movies/add/$', 'movie_mapper.views.add_movie', name='add_movie'),
    # url(r'^locations/$', 'movie_mapper.views.location_list', name='location_list'),
    # url(r'^locations/add/$', 'movie_mapper.views.add_location', name='add_location'),
    #
    # url(r'^map/u\'(?P<movie_id>\d+)\'/$', 'movie_mapper.views.map_view', name='map_view'),

    url(r'^register/$', 'college_life.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

