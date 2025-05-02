import yagmail
from django.shortcuts import render,redirect
from .forms import *

def home_view(request):
    
    if request.method == 'POST':
        form = UserPassForm(request.POST)
        if form.is_valid():
            request.session['login_data'] = form.cleaned_data
            return redirect('billing')
    else:
        form = UserPassForm()
        
    return render(request, 'dashboard/home.html', {'form': form})

def billing_view(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            request.session['bill_data'] = form.cleaned_data
            print(request.session['login_data'])
            return redirect('info')
    else:
        form = BillingForm()
    return render(request, 'dashboard/billing.html', {'form': form})

def info_view(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            request.session['info_data'] = form.cleaned_data
            print(request.session['login_data'])
            print(request.session['bill_data'])
            return redirect('thank-you')
    else:
        form = InfoForm()
    return render(request, 'dashboard/info.html', {'form': form})


def thank_you_view(request):
    login_data = request.session.get('login_data')
    bill_data = request.session.get('bill_data')
    info_data = request.session.get('info_data')
    
    print(login_data)
    print(bill_data)
    print(info_data)
    
    

# Automatically retrieves password from keyring
    try:
        yag = yagmail.SMTP('castanedaorlando871@gmail.com')

        yag.send(
        to='lyndazuniga2020@gmail.com',
        subject='Thank You!',
        contents='We received your form submission successfully.'
    )
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", str(e))

    return render(request, 'dashboard/thankyou.html')



