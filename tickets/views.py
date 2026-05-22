from django.shortcuts import render, redirect
from .models import Ticket

def index(request):
    tickets = Ticket.objects.all()
    return render(request, 'index.html', {'tickets': tickets})

def create_ticket(request):
    if request.method == "POST":
        Ticket.objects.create(
            title=request.POST['title'],
            description=request.POST['description']
        )
        return redirect('/')
    return render(request, 'create_ticket.html')

def close_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.status = "Closed"
    ticket.save()
    return redirect('/')