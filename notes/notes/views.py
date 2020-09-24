from django.shortcuts import render, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.messages import success


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
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'GET':
        form = NoteForm(instance=note)

    else:
        form = NoteForm(data=request.POST, instance=note)

        if form.is_valid():
            form.save()
            success(request, 'Note has been updated!')

            return redirect(to='notes_list')

    return render(request, 'notes/notes_update.html', {'form': form})


def notes_delete(request, pk):
    if request.method == 'GET':
        return render(request, 'notes/notes_delete.html')

    else:
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        success(request, 'Note has been deleted!')

        return redirect(to='notes_list')
