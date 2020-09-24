from django.shortcuts import render, get_object_or_404
from .models import Note
from .forms import NoteForm


def notes_list(request):
    notes = Note.objects.all()
    return render(request, "notes/notes_list.html", {"notes": notes})


def note_details(request, pk):
    note = get_object_or_404(Note, pk=pk)

    return render(request, "notes/note_details.html", {"note": note})


def notes_create(request):
    if request.method == "GET":
        form = None

    else:
        form = None

    return render(request, "notes/notes_create.html", {"form": form})


def notes_update(request, pk):
    # needs to update the updated_at variable/column (that I need to create)
    pass


def notes_delete(request, pk):
    pass
