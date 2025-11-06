from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Poem


# Create
class PoemCreateView(CreateView):
    model = Poem
    fields = [
        "title",
        "body",
        "author",
    ]
    success_url = reverse_lazy("poem_list")


# Read (list, detail)
class PoemListView(ListView):
    model = Poem
    context_object_name = "poems"
    ordering = "-created_at"


class PoemDetailView(DetailView):
    model = Poem
    context_object_name = "poem"


# Update
class PoemUpdateView(UpdateView):
    model = Poem
    fields = [
        "title",
        "body",
        "author",
    ]


# Delete
class PoemDeleteView(DeleteView):
    model = Poem
    success_url = reverse_lazy("poem_list")
