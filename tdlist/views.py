from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators  import login_required  
from .forms import SignUpForm, BusinessForm
from .models import Business


def index_page(request):
    title = Business.objects.all()
    if request.method =='POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            new_business = form.cleaned_data.get('title')
            Business.objects.create(title = new_business)
            return redirect('index_page')
    form = BusinessForm()
    return render(request, 'first.html', {'title':title, 'form':form})

def business_detail(request, pk):
    business = get_object_or_404(Business, pk=pk)
    return render(request, 'business_detail.html', {'business': business})

def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index_page')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def update(request, pk):
    business = get_object_or_404(Business, pk=pk)
    if request.method =='POST':
        form = BusinessForm(request.POST, instance=business)
        if form.is_valid():
            new_business = form.save()
            return redirect('index_page')
    else:
        form = BusinessForm(instance=business)

    return render(request, 'update_business.html', {'form': form})

@login_required
def business_delete(request, pk):
    business = Business.objects.get(pk=pk)
    if request.method == 'POST':
        business.delete()
        return redirect('index_page')
    return render(request, 'business_delete.html', {'business':business})
