from django.urls import path

from common.views import browse_category, LandingView, BrowseView, checkout, orders_details, accept_order, \
    dismiss_order, SearchResultsView

urlpatterns = [
    path('', BrowseView.as_view(), name='browse'),
    path('about_us/', LandingView.as_view(), name='landing'),
    path('category/<str:category>', browse_category, name='browse category'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders_details, name='orders'),
    path('accept_order/<int:pk>', accept_order, name='accept order'),
    path('dismiss_order/<int:pk>', dismiss_order, name='dismiss order'),
    path('search/', SearchResultsView.as_view(), name='search results')

]
