
from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

app_name = "sethub"

urlpatterns = [
    path("", views.index, name="index"),
    path("catalog/<int:cat_id>/", views.catalog, name="catalog"),
    path("catalog/<slug:cat_slug>/", views.catalog_by_slug, name="catalog_by_slug"),
    path("archive/<year4:year>/", views.archive, name="archive"),
]