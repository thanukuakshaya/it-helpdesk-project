from django.shortcuts import render, redirect
from .models import Ticket
from django.http import HttpResponse

def index(request):
    tickets = Ticket.objects.all()
    return render(request, 'index.html', {'tickets': tickets})

def create_ticket(request):
    if request.method == "POST":
        Ticket.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            status="New"   # default status
        )
        return redirect('/')
    return render(request, 'create_ticket.html')

def close_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.status = "Closed"
    ticket.save()
    return redirect('/')

def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)

    if request.method == "POST":
        ticket.status = request.POST['status']
        ticket.save()
        return redirect('/')

    return render(request, 'ticket_detail.html', {'ticket': ticket})

def health(request):
    return HttpResponse("OK")