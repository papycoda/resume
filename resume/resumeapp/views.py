from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    #basic template for the landing page
    return render(request, 'index.html')

    
def contact_view(request):
    # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        Phone:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
        send_mail('You got a mail!', message, '', ['opeyemi655@gmail.com']) 
        
    return render(request, 'index.html', {})
