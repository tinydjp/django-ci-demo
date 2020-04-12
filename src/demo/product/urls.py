from django.conf.urls import url

from .views import ListCompany, ListProduct, CompanyDetail, ProductDetail

urlpatterns = [
    url(r'^$', ListProduct.as_view()),
    url(r'^(?P<pid>[\d]+)$', ProductDetail),
    url(r'^company$', ListCompany.as_view()),
    url(r'^company/(?P<cid>[\d]+)$', CompanyDetail.as_view())
]