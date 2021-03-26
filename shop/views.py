from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Contact, Orders
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import auth, messages
from django.conf import settings
# emailsiimport
from django.core.mail import send_mail
import smtplib
import ssl
from email.message import EmailMessage
# Create your views here.


def index(request):
    # if request.user.is_anonymous:
    #     return redirect("login")
    products = Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        allProds.append([prod, range(1, n)])
    params = {'allProds': allProds}
    # params = {'product': products}
    return render(request, 'index.html', params)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        print(name, email, subject, message)
        contact = Contact(name=name, email=email,
                          subject=subject, message=message)
        contact.save()
    return render(request, 'contact.html')


def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        # nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, n)])  # n
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query) < 4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'index.html', params)


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.Product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def productview(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'single-product.html', {'product': product[0]})


def Category(request):
    prod = Product.objects.all()
    return render(request, 'category.html', {'prods': prod})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address_1 = request.POST.get('address_1', '')
        address_2 = request.POST.get('address_2', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')
        order = Orders(items_json=items_json, name=name, last_name=last_name, email=email,
                       phone=phone, address_1=address_1, address_2=address_2, city=city, zip_code=zip_code)
        order.save()
        # sending an Email 1
        # subject = 'welcome to GFG world'
        # message = f'Hi {name}, thank you for for ordering'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [email]
        # send_mail(subject, message, email_from, recipient_list)

        # Another email 2
        # msg = EmailMessage()
        # msg.set_content("hi, {name}")
        # msg["Subject"] = "An Email Alert"
        # msg["From"] = "settings.EMAIL_HOST_USER"
        # msg["To"] = "{email}"

        # context = ssl.create_default_context()

        # with smtplib.SMTP("smtp.example.com", port=587) as smtp:
        #     smtp.starttls(context=context)
        #     smtp.login(msg["From"], "Red@.8686")
        #     smtp.send_message(msg)

        # email 3
        send_mail(
            'HI, {name}',
            'Here is the message.',
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False,
        )

        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank': thank, 'id': id})
    return render(request, 'checkout.html')


def signup(request):
    if request.method == "POST":
        # gettinng parameter
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Cn_password = request.POST['Cn_password']

        # checking error inputs
        if len(username) > 10:
            messages.error(request, "Username must be less than 10 characters")
            return redirect('login')

        if not username.isalnum():
            messages.error(
                request, "Username must conatins only letters and numbers")
            return redirect('login')

        if password != Cn_password:
            messages.warning(
                request, "Both Password didn't match !!")
            return redirect('login')

        # ceate thee user
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        messages.success(request, " your account has been succesfully creted")
    else:
        return HttpResponse('404-Not Found')

    return redirect('shop')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request, "Successfully logged in !!")
            return redirect("shop")
        else:
            # No backend authenticated the credentials
            messages.warning(request, "Invalid login,Please try again !!")
            return redirect('login')

    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    messages.success(request, 'You are logged out !!')
    return redirect("shop")


def cart(request):
    return render(request, 'cart.html')


def search1(request):
    return render(request, 'search.html')


def tracker(request):
    return render(request, 'tracking.html')
