from django.shortcuts import render,redirect


from .models import *
from .forms import *
# Create your views here.
def index(request):
    note=Note.objects.all()
    form=NoteForm()

    if request.method =='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/note')
    content={'note':note,'form':form}
    return render(request,'note/list.html',content)


def updateNote(request,pk):

    note=Note.objects.get(id=pk)
    form=NoteForm(instance=note)

    if request.method =='POST':
        form=NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('/note')

    context={'form':form}
    return render(request,'note/update_Note.html',context)

def deleteNote(request,pk):

    item=Note.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        return redirect('/note')

    context={'item':item}
    return render(request,'note/delete_Note.html',context)

