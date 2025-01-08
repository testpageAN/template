from django.urls import path

from app.instrument import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("instruments", views.instruments, name="instruments-page"),
    # path("instrument/<int:id>"),
    path("instruments/<slug>", views.instrument_detail, name="instrument-detail-page"),
]
