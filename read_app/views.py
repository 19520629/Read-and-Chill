from django.shortcuts import render, HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from .models import Sach
# Create your views here.
def home(request):
    recommended_book=Sach.objects.all()
    context={"titles":recommended_book[0:10]}
    return render(request, 'index.html', context)


def register(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'dangki.html', {'form':form})


def book_page(request):
    recommended_book = Sach.objects.all()
    context = {"titles": recommended_book}
    return render(request, 'book-page.html', context)

def readbook(request, slug):
    book = Sach.objects.get(slug=slug)
    return render(request, 'read-book.html', {})

def introbook(request, slug):
    book = Sach.objects.get(slug=slug)
    return render(request, 'intro-book.html', {'book_preview':book})
