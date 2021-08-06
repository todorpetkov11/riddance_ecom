from django.urls import path

from common.views import BrowseView, LandingView

urlpatterns = [
    path('', BrowseView.as_view(), name='browse'),
    path('about_us/', LandingView.as_view(), name='landing')
]
