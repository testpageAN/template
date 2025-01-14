from django.urls import path
from . import views
# from .views import ListingDetailView

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    # path('<int:listing_id>', ListingDetailView.as_view(), name='listing'),
    path('search', views.search, name='search'),
]
