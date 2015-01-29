from django.shortcuts import render,HttpResponse,render_to_response
from Products.models import Login,Customer,Stock_details
#from Products.forms import PostForm

def login(request):
	return render(request,'login.html')
def test_login(request):
	uname=request.GET['uname']
	pwd=request.GET['pwd']
	try:
		obj= Login.objects.get(username=uname)
	except:
		return HttpResponse("user not available")
	if obj:
		if obj.password==pwd:
			return render(request,'details.html')

			#return HttpResponse("Login successfull")
		else:
			return HttpResponse("incorrect password")

def sign_up(request):
	return render(request,'sign_up.html')
def sign_up_user(request):
	if request.method=="POST":
		Login_Name=request.POST['login']
		try:
			obj=customers.objects.get(Login_Name=login)
		except:
			obj=None
			if not obj:
				if request.POST['pwd1']==request.POST['pwd2']:
					obj=Customer(Login_Name=request.POST['login'],Full_Name=request.POST['full_name'],Password=request.POST['pwd1'],Phone_Number=request.POST['phone_number'] )
					obj.save()
					obj=Login(username=request.POST['login'],password=request.POST['pwd1'])
					obj.save()
					return render(request,'login.html')
				else:
					return HttpResponse("Password doesn't match")
			else:
				return HttpResponse("user already exist")
def stock_details(request):
	#stock_obj=Stock_details.objects.all()
	#Data={  'product_name':stock_obj.Product_name,
			#'manf_date':Fligth_obj.Manfacturing_date,
			#'net_weigth':Fligth_obj.Net_weigth,
			#'price':Fligth_obj.Price,
			#'quantity':Fligth_obj.Quantity,
			#'remarks':Fligth_obj.Remarks,
			#}
	return render(request,'stock_details.html')
def add_stock(request):
	Total=request.GET.get('stock')
	No_of_items=range(int(Total))
	return render_to_response('add_blocks.html',{'block':No_of_items})
#def insert_stock(request):
#	item=request.GET.get('product_name')
#	return item
#	return HttpResponse("Stock")






# Create your views here.
