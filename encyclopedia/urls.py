from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new_page", views.new_page, name="new_page"),
    path('new_page/<str:message>/<str:category>/', views.new_page, name='new_page_with_message'),
    path("edit_page/<str:title>", views.edit_page, name="edit_page"),
    path('random_page', views.random_page, name='random_page'),
    path("wiki/<str:title>", views.entry, name="entry")
]
