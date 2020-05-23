from django.conf.urls import url

from .views import ListCompany, ListProduct, CompanyDetail, ProductDetail

urlpatterns = [
    url(r'^$', ListProduct.as_view(), name='list-product'),
    url(r'^(?P<pid>[\d]+)$', ProductDetail),
    url(r'^company$', ListCompany.as_view(), name='list-company'),
    url(r'^company/(?P<cid>[\d]+)$', CompanyDetail.as_view())
]
