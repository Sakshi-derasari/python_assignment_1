from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.conf import settings
import os
import razorpay
from django.views.decorators.csrf import csrf_exempt

# ADD PRODUCT
def add_to_cart(request):
    if request.method == "POST":
        data = request.POST

        img = None
        if request.FILES:
            img = request.FILES['img']

        Add_to_cart.objects.create(
            product_name=data["product_name"],
            product_discription=data["product_discription"],
            product_price=data["product_price"],
            product_discount=data["product_discount"],
            qty=data["qty"],
            img=img
        )

        return redirect("cart")

    return render(request, "add_to_cart.html")


# CART PAGE
def cart(request):
    cart = Add_to_cart.objects.all()
    total = sum(i.totale_price for i in cart)

    return render(request, "cart.html", {
        "cart": cart,
        "total": total
    })


# DELETE
def delete(request):
    did = request.GET.get("did")
    Add_to_cart.objects.filter(id=did).delete()
    return redirect("cart")


# UPDATE
def update(request):
    uid = request.GET.get("uid")
    c = Add_to_cart.objects.get(id=uid)

    if request.method == "POST":
        data = request.POST

        c.product_name = data["product_name"]
        c.product_discription = data["product_discription"]
        c.product_price = data["product_price"]
        c.product_discount = data["product_discount"]
        c.qty = data["qty"]

        if request.FILES:
            if c.img:
                os.remove(c.img.path)
            c.img = request.FILES['img']

        c.save()
        return redirect("cart")

    return render(request, "add_to_cart.html", {"c": c})

def payment(request):
    amt = request.GET.get('amt')

    # Convert safely
    amt = int(Decimal(amt))   # ✅ FIX

    client = razorpay.Client(
        auth=("rzp_test_SZhfnU4R2fx5Zn", "CvEWnX4PeEaJo4ovQ1NIuL9S")
    )

    data = {
        "amount": amt * 100,
        "currency": "INR",
        "receipt": "order_rcptid_11"
    }

    order = client.order.create(data=data)

    return render(request, "payment.html", {
        "order_id": order['id'],
        "amount": amt,
        "key": "rzp_test_SZhfnU4R2fx5Zn"
    })

@csrf_exempt
def success(request):
    return HttpResponse("Payment Successful ✅")