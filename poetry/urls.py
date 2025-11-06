from django.urls import path
from . import views

urlpatterns = [
    # create
    path("new/", views.PoemCreateView.as_view(), name="poem_create"),
    # read
    path("", views.PoemListView.as_view(), name="poem_list"),
    path("<int:pk>/", views.PoemDetailView.as_view(), name="poem_detail"),
    # update
    path("<int:pk>/edit/", views.PoemUpdateView.as_view(), name="poem_edit"),
    # delete
    path("<int:pk>/delete/", views.PoemDeleteView.as_view(), name="poem_delete"),
]
