from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from datetime import date
from django.utils.timezone import datetime
# Create your views here.
def Login(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request.POST,data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user= authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        fm=AuthenticationForm()
    context={'form':fm}
    return render(request,'login.html',context)

def Error(request):
    return render(request,'error.html')


def Logout(request):
  logout(request)
  return redirect('login')


def Home(request):
    if request.user.is_superuser:
        if request.method =='POST':
            cashfm=AddCashForm(request.POST)
            if cashfm.is_valid():
                cashfm.save()
                
                return redirect('home')

        else:
            cashfm=AddCashForm()

        # expenss
        if request.method =='POST':
            fm=AddExpenseMonyForm(request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('home')

        else:
            fm=AddExpenseMonyForm()

        expense_amount=0.0
        expense=[ p for p in AddExpenseMony.objects.all()]
        if expense:
            for expense in expense:
                expense_amount+=expense.Money

        # transctions
        if request.method =='POST':
            transfm=AddTrasctionsForm(request.POST)
            if transfm.is_valid():
                transfm.save()
                
                return redirect('home')

        else:
            transfm=AddTrasctionsForm()

        transction_amount=0.0
        
        transction=[ p for p in AddTrasctions.objects.all()]
        if transction:
            for transction in transction:
                transction_amount+=transction.money

    

    #buy products
        if request.method =='POST':
            buyfm=BuyProductForm(request.POST)
            if buyfm.is_valid():
                buyfm.save()
                
                return redirect('home')

        else:
            buyfm=BuyProductForm()
        
        buy_products=0.0

        buyproduct=[p for p in BuyProduct.objects.all()]
        if buyproduct:
            for buyproduct in buyproduct:
             buy_products+=buyproduct.money 


        #Cash AddCashForm
    

        add_cash=0.0

        addcash=[p for p in AddCash.objects.all()]
        if addcash:
            for addcash in addcash:
             add_cash+=addcash.add_money 


        total_amount=0.0
        cash=0.0
        sale=[p for p in CheckOut.objects.all()]
        if sale:
            for sale in sale:
                amount=(sale.qty*sale.item.price)
                vat=(amount*15/100)
                total=(amount+vat)
                cash+=(amount+vat)
                toatalcash=cash-expense_amount-transction_amount-buy_products+add_cash
                total_amount+=total
                
        today_sale=0.0
        today = datetime.today()
        todaysale=[p for p in CheckOut.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)]
        if todaysale:
            for todaysale in todaysale:
                amount=(todaysale.qty*todaysale.item.price)
                vat=(amount*15/100)
                total=(amount+vat)
                today_sale+=total
                
                    

        context={'home':'active',
                'total_amount':total_amount,
                'cash':toatalcash,
                'fm':fm,
                'expense_amount':expense_amount,
                'transfm':transfm,
                'transction_amount':transction_amount,
                'buyfm':buyfm,
                'buy_products':buy_products,
                'cashfm':cashfm,
                'today_sale':today_sale
                
                
                
                }
        return render(request,'dashboard.html',context)
    else:
        return redirect('error')


def ProductInputs(request):
    if request.user.is_superuser:
        pd=ProductInput.objects.all().order_by('-id')
        
    
        if request.method== 'POST':
            fm=ProductInputForm(request.POST)
            if fm.is_valid():
                fm.save()
                # totalqty=pdget.qty+fm.qty
                # totalqty.save()
                fm=ProductInputForm()
        else:
            fm=ProductInputForm()
        
        amount=0.0
        vat=0.0
        total=0.0
        produc=[p for p in ProductInput.objects.all()]
        if produc:
            for p in produc:
                tempamount=(p.price * p.qty)
                amount+=tempamount
                vat=( amount * 15 / 100)
                total=amount+vat
        
        context={'form':fm,'pd':pd,'total':total,'amount':amount,'vat':vat,'productinput':'active'}
        return render(request,'productinput.html',context)
    else:
        return redirect('error')
    
def ProductInputSuccess(request):
    if request.user.is_superuser:
        cart=ProductInput.objects.all()
        for c in cart:
            ProductInputCart(item=c.item_name,qty=c.qty).save()
            c.delete()
        return redirect('productinput')
    else:
        return redirect('error')



def ProductList(request):
    if request.user.is_superuser:
        product=Product.objects.all().order_by('-id')
        if request.method== 'POST':
            fm=ProductAddForm(request.POST)
            if fm.is_valid():
                fm.save()
                fm=ProductAddForm()
        else:
            fm=ProductAddForm()

        context={'pd':product,'form':fm,'productlist':'active'}
        return render(request,'productlist.html',context)
    else:
        return redirect('error')
    

def ProductEdit(request,pk):
    if request.user.is_superuser:
        if request.method=='POST':
            item=request.POST['item']
            price=request.POST['price']
            
            Product.objects.filter(id=pk).update(
                
                item_name=item,
                price=price
            
            )
        
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('error')

def Pos(request):
    if request.user.is_superuser:
        posdata=PosSale.objects.all().order_by('-id')
        if request.method== "POST":
            addform=AddCompanyNameForm(request.POST)
            if addform.is_valid():
                addform.save()
                return redirect('pos')
        else:
            addform=AddCompanyNameForm()
        
        if request.method== 'POST':
            fm=PosSaleForm(request.POST)
            if fm.is_valid():
                fm.save()
                fm=PosSaleForm()
                return redirect('pos')
        else:
            fm=PosSaleForm()

        gross_total=0.0
        vat=0.0
        total=0.0
        discount=0.0
        posamount=[p for p in PosSale.objects.all()]
        if posamount:
            for p in posamount:
                temp=(p.qty*p.item.price)
                gross_total+=temp
                vat=(gross_total*15/100)
                discount+=(p.Discount_price)
                total=gross_total+vat -discount
        context={
            'form':fm,'posdata':posdata,
            'gross_total':gross_total,
            'vat':vat,'total':total,
            'pos':'active',
            'discount':discount,
            'addform':addform
        }
        return render(request,'pos.html',context)
    else:
        return redirect('error')


def Edit(request,pk):
    if request.user.is_superuser:
        if request.method=='POST':
            qty=request.POST['qty']
            discount=request.POST['discount']
            PosSale.objects.filter(id=pk).update(qty=qty,Discount_price=discount)
        
        return redirect(request.META['HTTP_REFERER'])
    return redirect('error')



def PostDelete(request,id):
    if request.user.is_superuser:
        dl=PosSale.objects.get(id=id)
        dl.delete()
        return redirect('pos')
    else:
        return redirect('error')
    

def Sale(request):
    if request.user.is_superuser:
        sale=CheckOut.objects.all().order_by('-id')
        context={'sale':'active','sale':sale}
        return render(request,'sale.html',context)
    else:
        return redirect('error')


def Delete(request,id):
    dl=ProductInput.objects.get(id=id)
    dl.delete()
    return redirect('productinput')


def Checkout(request):
    if request.user.is_superuser:
        posdata=list(PosSale.objects.all().order_by('-id'))
        company=Client.objects.all().order_by('-id')
        
        
        gross_total=0.0
        vat=0.0
        total=0.0
        discount=0.0
        posamount=[p for p in PosSale.objects.all()]
        if posamount:
            for p in posamount:
                temp=(p.qty*p.item.price)
                gross_total+=temp
                vat=(gross_total*15/100)
                discount+=(p.Discount_price)
                total=gross_total+vat -discount
        context={
            'posdata':posdata,
            'gross_total':gross_total,
            'vat':vat,'total':total,
            'pos':'active',
            'discount':discount,
            'company':company,
        
            
            
        }
        for pos_obj in PosSale.objects.all():
            CheckOut(item=pos_obj.item,qty=pos_obj.qty,date=pos_obj.date).save()
            pos_obj.delete()

        return render(request,'invoice.html', context)
    else:
        return redirect('error')  



def Expense_data(request):
    if request.user.is_superuser:
        expensdata=AddExpenseMony.objects.all()
        context={'expensdata':expensdata}
        return render(request,'expense.html',context)
    return redirect('error')  



def Tansaction(request):
    if request.user.is_superuser:
        trans=AddTrasctions.objects.all()
        context={'trans':trans}
        return render(request,'transction.html',context)
    return redirect('error') 



def Cash(request):
    if request.user.is_superuser:
        cashdata=AddCash.objects.all()
        context={'cashdata':cashdata}
        return render(request,'cash.html',context)
    return redirect('error')


def BuyBroducts(request):
    if request.user.is_superuser:
        buy_product=BuyProduct.objects.all()
        context={'buy_product':buy_product}
        return render(request,'buyproducts.html',context)
    return redirect('error')

