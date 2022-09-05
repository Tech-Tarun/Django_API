from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import CCBoard, CartItem, admin_login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCart(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        p_name = data.get('product_name')
        p_price = data.get('product_price')
        p_quantity = data.get('product_quantity')

        product_data = {
            'product_name': p_name,
            'product_price': p_price,
            'product_quantity': p_quantity,
        }
        cart_item = CartItem.objects.create(**product_data)
        data = {
            "message": f"New item added to Cart with id: {cart_item.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        items_count = CartItem.objects.count()
        items = CartItem.objects.all()
        items_data = []
        for item in items:
            items_data.append({'product_name': item.product_name,
                               'product_price': item.product_price,
                               'product_quantity': item.product_quantity,
                               })
        data = {'items': items_data,
                'count': items_count,
                }
        # return JsonResponse(data)
        return render(request, 'index.html', {'detail': data})


@method_decorator(csrf_exempt, name='dispatch')
class CC_Embosser(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        c_name = data.get('cust_name')
        c_add = data.get('add')
        c_mobile = data.get('mobile')
        c_number = data.get('card_no')
        c_limit = data.get('card_limit')
        c_expiry = data.get('card_expiry')
        c_email = data.get('email')

        CC_data = {
            'cust_name': c_name,
            'add':       c_add,
            'mobile':    c_mobile,
            'card_no':   c_number,
            'card_limit': c_limit,
            'card_expiry': c_expiry,
            'email':      c_email,
        }
        CC_item = CCBoard.objects.create(**CC_data)
        data = {
            "message": f"New item added to Cart with id: {CC_item.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        items_count = CCBoard.objects.count()
        items = CCBoard.objects.all()
        items_data = []
        for item in items:
            items_data.append({"cust_name": item.cust_name,
                               "add": item.add,
                               "mobile": item.mobile,
                               "card_no": item.card_no,
                               "card_limit": item.card_limit,
                               "card_expiry": item.card_expiry,
                               "email": item.email})
        data = {'items': items_data,
                'count': items_count,
                }
        return JsonResponse(data)


class CC_Embosser_fe(View):
    def post(self, request):
        if request.method == "POST":
            c_name = request.POST['name']
            c_add = request.POST['address']
            c_mobile = request.POST['phone']
            c_number = request.POST['card_no']
            c_limit = request.POST['card_lim']
            c_expiry = request.POST['card_exp']
            c_email = request.POST['email']

        CC_data = {
            'cust_name': c_name,
            'add':       c_add,
            'mobile':    c_mobile,
            'card_no':   c_number,
            'card_limit': c_limit,
            'card_expiry': c_expiry,
            'email':      c_email,
        }
        CC_item = CCBoard.objects.create(**CC_data)
        data = {
            "message": f"New item added to Cart with id: {CC_item.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        items_count = CCBoard.objects.count()
        items = CCBoard.objects.all()
        items_data = []
        for item in items:
            items_data.append({"cust_name": item.cust_name,
                               "add": item.add,
                               "mobile": item.mobile,
                               "card_no": item.card_no,
                               "card_limit": item.card_limit,
                               "card_expiry": item.card_expiry,
                               "email": item.email})
        data = {'items': items_data,
                'count': items_count,
                }
        return render(request, 'demo.html')


def admin_log(request):
    if request.method == 'POST':
        uname = request.POST['username']
        psw = request.POST['password']
        det = admin_login.objects.all()
        if (det[0].user_name) == uname and (det[0].pswrd) == psw:
            items_count = CCBoard.objects.count()
            items = CCBoard.objects.all()
            items_data = []
            for item in items:
                items_data.append({"cust_name": item.cust_name,
                                   "add": item.add,
                                   "mobile": item.mobile,
                                   "card_no": item.card_no,
                                   "card_limit": item.card_limit,
                                   "card_expiry": item.card_expiry,
                                   "email": item.email})
            data = {'items': items_data,
                    'count': items_count,
                    }
            # return JsonResponse(data)
            return render(request, 'admin_response.html', {'detail': items_data})
    else:
        return render(request, 'admin.html')


def customer_log(request):
    if request.method == 'POST':
        name = request.POST['username']
        card = request.POST['password']
        items = CCBoard.objects.all()
        items_data = []

        for item in items:
            if (item.cust_name) == name and str(item.card_no) == card:
                items_data.append({"cust_name": item.cust_name,
                                   "add": item.add,
                                   "mobile": item.mobile,
                                   "card_no": item.card_no,
                                   "card_limit": item.card_limit,
                                   "card_expiry": item.card_expiry,
                                   "email": item.email})
                # items_data.append(item.cust_name,
                #                    item.add,
                #                    item.mobile,
                #                    item.card_no,
                #                    item.card_limit,
                #                    item.card_expiry,
                #                    item.email)
        data = {'items': items_data,}
        # return render(request, 'customer1.html', {'detail': items_data})
        return render(request, 'customer_response.html', {'detail': items_data})
    else:
        return render(request, 'customer.html')


def cus_get(request,name,card):
    items = CCBoard.objects.all()
    items_data = []
    for item in items:
        if ((item.cust_name) == name) and (str(item.card_no) == card):
            print("Hello")
            items_data.append({"cust_name": item.cust_name,
                            "add": item.add,
                            "mobile": item.mobile,
                            "card_no": item.card_no,
                            "card_limit": item.card_limit,
                            "card_expiry": item.card_expiry,
                            "email": item.email})
    data = {'items': items_data,
            }
    return JsonResponse(data)
