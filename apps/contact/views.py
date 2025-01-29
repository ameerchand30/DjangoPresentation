from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        messages.success(request, 'Message sent successfully!')
        return redirect('contact')
    return render(request, 'pages/contact.html')
def contact_list(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'pages/contact_list.html', {'contacts': contacts})
def contact_edit(request, val):
    contact = Contact.objects.get(pk=val)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.subject = request.POST['subject']
        contact.message = request.POST['message']
        contact.save()
        messages.success(request, 'Contact updated successfully!')
        return redirect('contact_list')
    # return render(request, 'pages/contact_edit.html', {'contact': contact})
    return render(request, 'pages/contact.html', {'contact': contact})
def contact_delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    messages.success(request, 'Contact deleted successfully!')
    return redirect('contact_list')