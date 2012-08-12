from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'trishaatt.views.test'),
    url(r'^login', 'trishaatt.views.login'),
    url(r'^ajax/test/', 'trishaatt.ajax.test'),
    url(r'^signup', 'trishaatt.views.signup')
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
