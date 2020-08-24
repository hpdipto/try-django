from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
# Create your views here.

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


def dynamic_lookup_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    # obj = Product.objects.get(id=my_id)
    # try: 
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def render_initial_data(request):
    initial_data = {
        'title': "My awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid:
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_form.html", context)


# def product_create_view(request):
#     my_form = RawProductForm(request.GET)

#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is goods
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)

#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_form.html", context)


# def product_create_view(request):
#     if request.method == 'POST':
#         new_title = request.POST.get('title')
#         # Product.objects.create(title=new_title)

#     context = {
        
#     }
#     return render(request, "products/product_form.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_form.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title" : obj.title,
    #     "description": obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
