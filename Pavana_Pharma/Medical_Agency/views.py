from django.shortcuts import render, render_to_response
from Medical_Agency.models import Login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from Medical_Agency.models import ComplteStockDetails
#from django.core.context_processors import csrf
# Create your views here.


def home(request):
    return render(request, 'home.html')


def home1(request):
    return render(request, 'login1.html')


def login(request):
    try:
        print request.GET['user']
        login_obj = Login.objects.get(username=request.GET['user'])
        if login_obj.password == request.GET['pwd']:
            return render_to_response(
                'login.html', {'username': request.GET['user'].upper()})

        else:
            return HttpResponse('Password is not matched, Please try again')
    except Exception as e:
        print str(e)
        return HttpResponse('Username is not available')


def check_stock(request):
    obj = ComplteStockDetails.objects.all()
    return render_to_response('show_stock.html', {'data': obj})
    #TODO: Write a function to show the detailed records of all the products.


def check_dealers(request):
    pass
    #TODO: Write a function to show the complete details of all the deaslers.


def billing(request):
    pass
    #TODO : Write a function to do the billing for the selected items.


def prev_billing(request):
    pass
    #TODO: Write a function to show all the previous billings.


def add_stock(request):
    return render_to_response(
        'add_stock.html',
        {'no_of_items': range(int(request.GET['items']))},
        context_instance=RequestContext(request))


@csrf_protect
def add_stock_to_db(request):
    import pdb
    pdb.set_trace()
    dictionary = dict(request.POST.viewitems())

    for i in range(len(dictionary.values()[0])):
        try:
            data = ComplteStockDetails.objects.get(
                batch_num=dictionary.values()[1][i])

        except:
            data = None

        if not data:
            obj = ComplteStockDetails(
                batch_num=dictionary.values()[1][i],
                item_name=dictionary.values()[0][i],
                company=dictionary.values()[2][i],
                price_per_unit=dictionary.values()[3][i],
                manf_data=dictionary.values()[5][i],
                exp_data=dictionary.values()[6][i],
                quantity=dictionary.values()[8][i],
                comments=dictionary.values()[4][i])
            obj.save()
        else:
            if data.item_name == dictionary.values()[0][i]:
                data.quantity = data.quantity + dictionary.values()[8][i]
                data.save()
            else:
                return HttpResponse("Item Name is not matched")

    return HttpResponse('Success')


def check_item_wise_page(request):
    return render(request, 'check_stock_item_wise.html')


def show_item_wise(request):
    obj = ComplteStockDetails.objects.get(item_name=request.GET.get(
        'check_item_name'))
    return render_to_response(
        'conditioned_stock.html', {'data': [obj], 'search': 'ITEM NAME'})


def check_company_wise_page(request):
    return render(request, 'check_stock_company_wise.html')


def show_company_wise(request):
    obj = ComplteStockDetails.objects.filter(company=request.GET.get(
        'check_company_name'))
    return render_to_response(
        'conditioned_stock.html', {'data': obj, 'search': 'COMPANY NAME'})


def check_batch_number_wise_page(request):
    return render(request, 'check_stock_batch_wise.html')


def show_batch_num_wise(request):
    obj = ComplteStockDetails.objects.get(batch_num=int(request.GET.get(
        'check_batch_num')))
    return render_to_response(
        'conditioned_stock.html', {'data': [obj], 'search': 'BATCH NUMBER'})
