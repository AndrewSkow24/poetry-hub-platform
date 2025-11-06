from django.views.generic import ListView, DetailView
from .models import Poem


# Create


# Read (list, detail)
class PoemListView(ListView):
    model = Poem
    context_object_name = "poems"
    ordering = "-created_at"


class PoemDetailView(DetailView):
    model = Poem
    context_object_name = "poem"


# Update

# Delete
