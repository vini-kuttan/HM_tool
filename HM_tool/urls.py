from django.conf.urls import patterns, include, url

import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

controller =views.Controller()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HM_tool.views.home', name='home'),
    # url(r'^HM_tool/', include('HM_tool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', controller.login_form),
    url(r'^authentication/$',controller.authentication),
)
