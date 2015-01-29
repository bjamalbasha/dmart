from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Medical_Agency.views.home', name='home'),
    url(r'^home/', 'Medical_Agency.views.home1'),
    url(r'^login/', 'Medical_Agency.views.login'),
    url(r'^check_stock/', 'Medical_Agency.views.check_stock'),
    url(r'^check_dealers/', 'Medical_Agency.views.check_dealers'),
    url(r'^billing/', 'Medical_Agency.views.billing'),
    url(r'^check_prev_bills/', 'Medical_Agency.views.prev_billing'),
    url(r'^add_stock/', 'Medical_Agency.views.add_stock'),
    url(r'^add_stock_to_db', 'Medical_Agency.views.add_stock_to_db'),
    url(r'^check_item_wise/', 'Medical_Agency.views.check_item_wise_page'),
    url(r'^show_item_wise_stock/', 'Medical_Agency.views.show_item_wise'),
    url(r'^check_company_wise/',
        'Medical_Agency.views.check_company_wise_page'),
    url(r'^show_company_wise/', 'Medical_Agency.views.show_company_wise'),
    url(r'^check_batch_num_wise/',
        'Medical_Agency.views.check_batch_number_wise_page'),
    url(r'^show_batch_num_wise', 'Medical_Agency.views.show_batch_num_wise'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
