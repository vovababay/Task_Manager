from django.shortcuts import render
from django.http import HttpResponse
from board.models import *


def home(request):
    columns = Column.objects.all()
    context = {'title': 'Доска', 'columns': columns}
    return render(request, "board/note.html",context)
