from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Product ,ProductInput,ProductInputCart,PosSale,CheckOut
from .forms import ProductAddForm ,ProductInputForm,PosSaleForm,AddCompanyNameForm
# Create your views here.


def Home(request):
    total_amount=0.0
    sale=[p for p in CheckOut.objects.all()]
    if sale:
        for sale in sale:
            amount=(sale.qty*sale.item.price)
            vat=(amount*15/100)
            total=(amount+vat)
            total_amount+=total
            
           


    context={'home':'active','total_amount':total_amount}
    return render(request,'dashboard.html',context)

def ProductInputs(request):
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

def ProductInputSuccess(request):
    cart=ProductInput.objects.all()
    for c in cart:
        ProductInputCart(item=c.item_name,qty=c.qty).save()
        c.delete()
    return redirect('productinput')



def ProductList(request):
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

def ProductEdit(request,pk):
    if request.method=='POST':
        item=request.POST['item']
        price=request.POST['price']
        
        Product.objects.filter(id=pk).update(
            
            item_name=item,
            price=price
           
        )
    
    return redirect(request.META['HTTP_REFERER'])

def Pos(request):
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


def Edit(request,pk):
    if request.method=='POST':
       qty=request.POST['qty']
       discount=request.POST['discount']
       PosSale.objects.filter(id=pk).update(qty=qty,Discount_price=discount)
    
    return redirect(request.META['HTTP_REFERER'])



def PostDelete(request,id):
    dl=PosSale.objects.get(id=id)
    dl.delete()
    return redirect('pos')

def Sale(request):
    sale=CheckOut.objects.all().order_by('-id')
    context={'sale':'active','sale':sale}
    return render(request,'sale.html',context)


def Delete(request,id):
    dl=ProductInput.objects.get(id=id)
    dl.delete()
    return redirect('productinput')


def Checkout(request):
    cart=PosSale.objects.all()
    for c  in cart:
        CheckOut(item=c.item,qty=c.qty).save()
        c.delete()
        return redirect('invoice')
    

def Invoice(request):
    check=Checkout.objects.filter(id=id)
    
    return render(request,'invoice.html')
