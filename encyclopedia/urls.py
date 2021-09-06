from django.urls import path

from . import views
from . import util

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search_encyclopedia, name="search"),
    path("create_page", views.createpage, name="create_page"),
    path("wiki/<str:title>", views.show_page, name="get_page"),

]

