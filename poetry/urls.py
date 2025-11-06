from django.urls import path
from . import views

urlpatterns = [
    # create
    # read
    path("", views.PoemListView.as_view(), name="poem_list"),
    path("<int:pk>/", views.PoemDetailView.as_view(), name="poem_detail"),
    # update
    # delete
]
