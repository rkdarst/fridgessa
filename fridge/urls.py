from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fridgessa.views.home', name='home'),
    # url(r'^fridgessa/', include('fridgessa.foo.urls')),

    url(r'^inventory/$', views.inventory),
    url(r'^complete/item$', views.complete_item),
)
