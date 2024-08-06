from django.shortcuts import render, redirect, get_object_or_404
from . models import ImageModel, Category
from .forms import ImageForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm


# Create your views here.
def home_view(request):
    key = ImageModel.objects.filter(is_delete=False)
    return render(request,'products/index.html',{'value':key})

def products_Details(request, pk):
    product = get_object_or_404(ImageModel, reference_id=pk)
    return render(request, 'products/details.html', {'product': product})

# Admin Controling views
@login_required
def category_post(request):
    category = Category.objects.filter(category=category,created_by=current_user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = CategoryForm()
    return render(request, 'adminpages/category_post.html', {'form': form})

@login_required
def post_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.created_by = request.user  # Set the user who is creating this entry
            image.save()
            return redirect('images')
    else:
        form = ImageForm()
    return render(request, 'adminpages/product_post.html', {'form': form})

"""
Products filter Softdelete and filter login Current_user
"""
@login_required
def products(request):
    current_user = request.user  # Get the current user from the request
    key = ImageModel.objects.filter(is_delete=False, created_by=current_user)
    context = {'images': key}
    return render(request, 'adminpages/imglist.html', context)


@login_required
def edit_item(request, pk):
    # Fetch the product by reference_id (UUID)
    product = get_object_or_404(ImageModel, reference_id=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('images')  # Redirect to a detail view or any other page
    else:
        form = ImageForm(instance=product)
    return render(request, 'adminpages/edit.html', {'form': form})


@login_required
def images_Details(request, pk):
    product = get_object_or_404(ImageModel, reference_id=pk)
    return render(request, 'adminpages/details.html', {'product': product})

""" Softdelete """
@login_required
def delete_item(request, pk):
    products = ImageModel.objects.get(reference_id=pk)
    products.is_delete=True
    products.save()
    return redirect('/images')



@login_required
def dashboard_view(request):
    return render(request,'adminpages/dashboard.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            messages.error(request, 'There was an error logging in. Please try again.')
    return render(request, 'adminpages/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('dash')  # Redirect to the home page or another page
    else:
        form = UserRegistrationForm()
    return render(request, 'adminpages/signup.html', {'form': form})