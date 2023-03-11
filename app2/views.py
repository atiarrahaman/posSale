from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Product ,ProductInput,ProductInputCart,PosSale,CheckOut
from .forms import ProductAddForm ,ProductInputForm,PosSaleForm
# Create your views here.


def Home(request):
    context={'home':'active'}
    return render(request,'dashboard.html',context)

def ProductInputs(request):
    pd=ProductInput.objects.all()
    
   
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

# def ProductInputCartShow(request):
#     item_id=request.GET.get('item_id')
#     item=ProductInput.objects.get(id=item_id)
    
#     ProductInputCart(item=item).save()
#     return redirect('productinput')



def ProductList(request):
    product=Product.objects.all()
    if request.method== 'POST':
        fm=ProductAddForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=ProductAddForm()
    else:
        fm=ProductAddForm()

    context={'pd':product,'form':fm,'productlist':'active'}
    return render(request,'productlist.html',context)


def Pos(request):
    posdata=PosSale.objects.all()
    if request.method== 'POST':
        fm=PosSaleForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=PosSaleForm()
    else:
        fm=PosSaleForm()
    
    gross_total=0.0
    vat=0.0
    total=0.0
    posamount=[p for p in PosSale.objects.all()]
    if posamount:
        for p in posamount:
            temp=(p.qty*p.item.price)
            gross_total+=temp
            vat=(gross_total*15/100)
            total+=gross_total+vat
            

            

    context={
        'form':fm,'posdata':posdata,
        'gross_total':gross_total,
        'vat':vat,'total':total,
        'pos':'active'
        }
    return render(request,'pos.html',context)

def PostDelete(request,id):
    dl=PosSale.objects.get(id=id)
    dl.delete()
    return redirect('pos')

def Sale(request):
    sale=CheckOut.objects.all()
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
    return redirect('sale')
