from django.urls import path

from common.views import BrowseView, LandingView

urlpatterns = [
    path('browse/', BrowseView.as_view(), name='browse'),
    path('', LandingView.as_view(), name='landing')
]
