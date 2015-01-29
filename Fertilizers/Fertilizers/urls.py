from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Fertilizers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', 'Products.views.login'),
    url(r'^sign_up/','Products.views.sign_up'),
    url(r'^sign_up_user/','Products.views.sign_up_user'),
    url(r'^test_login/','Products.views.test_login'),
    url(r'^stock_details/','Products.views.stock_details'),
    url(r'^addstock/','Products.views.add_stock'),
    url(r'^insert/','Products.views.insert_stock'),

    url(r'^admin/', include(admin.site.urls)),
)
