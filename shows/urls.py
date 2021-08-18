from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('network/', views.network),
    path('network/<id>', views.tvinfo),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<id>', views.id),
    path('shows/<id>/edit', views.edit),
    path('shows/<id>/update', views.update),
    path('shows/<id>/destroy', views.destroy),
]
