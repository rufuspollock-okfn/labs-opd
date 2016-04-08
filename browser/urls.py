from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'browser'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="browser/home.html")),
    url(r'^home$', TemplateView.as_view(template_name="browser/home.html"), name='home'),
    url(r'^download$', TemplateView.as_view(template_name="browser/download.html"), name='download'),
    url(r'^nutrition$', TemplateView.as_view(template_name="browser/nutrition_us.html"), name='nutrition'),
    url(r'^search$', views.search_gtin, name='search'),
    url(r'^brand/list-(?P<page_id>[a-z0-9]+)$', views.ViewBrandList.as_view(), name='brand_list'),
    url(r'^brand/(?P<bsin>[a-zA-Z0-9]+)$', views.ViewBsin.as_view(), name='bsin'),
    url(r'^gtin/(?P<pk>[0-9]+)$', views.ViewGtin.as_view(), name='gtin'),
    url(r'^owner/list$', views.ViewOwnerList.as_view(), name='owner_list'),
    url(r'^owner/(?P<owner>[a-zA-Z0-9]+)$', views.ViewOwner.as_view(), name='owner'),
]
