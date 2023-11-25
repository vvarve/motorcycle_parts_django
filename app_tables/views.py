from django.shortcuts import render, redirect, HttpResponse
from .models import motorcycle, product, compatibility_acc
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


# Principal.
def login_html(request):  
    if request.POST:
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            try:
                user = User.objects.get(username=request.POST["username"])
                if user.check_password(request.POST["password"]):
                    login(request, user)
                    return render(request, "home.html")
                else:
                    return render(request, "login.html", {"form_auth_login" : AuthenticationForm, 
                                                            "auth_validate" : "user or password invalid!"})
            except:
                return render(request, "login.html", {"form_auth_login" : AuthenticationForm, 
                                                        "auth_validate" : "user or password invalid!"})         
        else:
            HttpResponse("Please, activate the cookies for login")
    request.session.set_test_cookie()       
    return render(request, "login.html", {"form_auth_login" : AuthenticationForm})

def home_html(request):
    return render(request, "home.html")

#Functions for login
def sign_up(request):
    if request.POST:
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            try: 
                if request.POST["password2"] and request.POST["password1"]:
                    user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])  
                    if user.check_password(request.POST["password2"]):
                        login(request, user)
                        return render(request, "home.html")
                    else:
                        return render(request, "login.html")
                else:
                    return render(request, "sign_up.html", {"form_create_user": UserCreationForm, 
                    "auth_validate" : "the password is not equal!"}
                    )
            except:
                return render(request, "sign_up.html", {"form_create_user": UserCreationForm, 
                    "auth_validate" : "user already exits!"})       
        else:
            HttpResponse("Please, activate the cookies for sing in")

    request.session.set_test_cookie()
    return render(request, "sign_up.html", {"form_create_user": UserCreationForm})

# NAV VIEW
def products_html(request):
    search = request.POST.get("search_product")
    product_all = product.objects.all()
    product_all_compatibility = motorcycle.objects.all()

    if search:
        product_all = product.objects.filter(
            Q(code__icontains = search) |
            Q(accessory__icontains = search) |
            Q(compatibility__manufacturer__icontains = search) |
            Q(compatibility__motorcycle__icontains = search) 
        ).distinct()

    return_product_query = {
        "product_a" : product_all,
        "product_motorcycle" : product_all_compatibility 
    }

    return render(request, "products.html", return_product_query)

def motorcycle_html(request):
    search = request.POST.get("search_product")
    motorcycle_all = motorcycle.objects.all()

    if search:
        motorcycle_all = motorcycle.objects.filter(
            Q(manufacturer__icontains = search) |
            Q(motorcycle__icontains = search) |
            Q(year__icontains = search)
        ).distinct()
    

    return render(request, "motorcycle.html", {"motorcycle_a" : motorcycle_all})

def compatibility_html(request):
    search = request.POST.get("search_product")
    compatibility_all = compatibility_acc.objects.all()
    product_all = product.objects.all()

    if search:
        compatibility_all = compatibility_acc.objects.filter(
            Q(code_product__code__icontains = search) |
            Q(code_ref__code__icontains = search) |
            Q(code_product__accessory__icontains = search) |
            Q(code_ref__accessory__icontains = search) |
            Q(code_ref__compatibility__manufacturer__icontains = search) |
            Q(code_product__compatibility__manufacturer__icontains = search) 
    ).distinct()

    return_product_compatibility = {
        "compatibility_a" : compatibility_all,
        "product_a": product_all
    }

    return render(request, "compatibility.html", return_product_compatibility)


# FUNCTIONS FOR products_html

def products_html_delete(request, id):
    product_deleted = product.objects.get(id=id)
    product_deleted.delete()
    return redirect("/products")

def edit(request, id):
    global add_id_edit
    search = request.POST.get("search_product")
    product_edit = product.objects.get(id=id)
    add_id_edit = {"id": id}
    product_all = product.objects.all()
    product_all_compatibility = motorcycle.objects.all()

    if search:
        product_all = product.objects.filter(
            Q(code__icontains = search) |
            Q(accessory__icontains = search) |
            Q(compatibility__manufacturer__icontains = search) |
            Q(compatibility__motorcycle__icontains = search) 
    ).distinct()
        
    return_product_query = {
        "product_motorcycle" : product_all_compatibility,
        "product_edit": product_edit,
        "product_a": product_all
    }
    return render(request, "products.html", return_product_query)

def register_product(request):
    form_code = request.POST["code_input"]
    form_image = request.FILES["image_input"]
    form_accesory = request.POST["accessory_input"]
    form_compatibility = request.POST["select_compatibility"]
    product.objects.create(code = form_code, images = form_image, accessory = form_accesory, compatibility = motorcycle.objects.get(motorcycle = form_compatibility.split(" / ")[0]))
    return redirect("/products")
    
def form_editing(request):
    form_editing_get = product.objects.get(id=add_id_edit["id"])
    form_editing_get.code = request.POST["code_input"]
    form_editing_get.images = request.FILES["image_input"]
    form_editing_get.accessory = request.POST["accessory_input"]
    form_editing_get.compatibility = motorcycle.objects.get(motorcycle = request.POST["select_compatibility"].split(" / ")[0])
    form_editing_get.save()
    return redirect("/products")
    

# FUNCTIONS FOR motorcycle_html

def motorcycle_html_delete(request, id):
    motorcycle_deleted = motorcycle.objects.get(id=id)
    motorcycle_deleted.delete()
    return redirect("/motorcycle")

def edit_m(request, id):
    global add_id_edit
    search = request.POST.get("search_product")
    motorcycle_edit = motorcycle.objects.get(id=id)
    add_id_edit = {"id": id}
    motorcycle_all = motorcycle.objects.all()

    if search:
        motorcycle_all = motorcycle.objects.filter(
            Q(manufacturer__icontains = search) |
            Q(motorcycle__icontains = search) |
            Q(year__icontains = search)
    ).distinct()
    
    return_product_query = {
        "motorcycle_edit": motorcycle_edit,
        "motorcycle_a": motorcycle_all
    }
    return render(request, "motorcycle.html", return_product_query)

def form_editing_motorcycle(request):
    motorcycle_edit = motorcycle.objects.get(id=add_id_edit["id"])
    motorcycle_edit.manufacturer = request.POST["manufacturer"]
    motorcycle_edit.motorcycle = request.POST["motorcycle"]
    motorcycle_edit.year = request.POST["year"]
    motorcycle_edit.save()
    return redirect("/motorcycle")

def register_motorcycle(request):
    motorcycle.objects.create(
        manufacturer = request.POST["manufacturer"],
        motorcycle = request.POST["motorcycle"],
        year = request.POST["year"]
    )
    return redirect("/motorcycle")

# FUNCTIONS FOR compatibility_html

def edit_c(request, id):
    global add_id_edit
    search = request.POST.get("search_product")
    add_id_edit = {"id": id}
    compatibility_all = compatibility_acc.objects.all()
    compatibility_edit = compatibility_acc.objects.get(id=id)
    product_all = product.objects.all()

    if search:
        compatibility_all = compatibility_acc.objects.filter(
            Q(code_product__code__icontains = search) |
            Q(code_ref__code__icontains = search) |
            Q(code_product__accessory__icontains = search) |
            Q(code_ref__accessory__icontains = search) |
            Q(code_ref__compatibility__manufacturer__icontains = search) |
            Q(code_product__compatibility__manufacturer__icontains = search) 
    ).distinct()
    return_product_compatibility = {
        "compatibility_a" : compatibility_all,
        "product_a": product_all,
        "compatibility_edit" : compatibility_edit
    }

    return render(request, "compatibility.html", return_product_compatibility)

def compatibility_html_delete(request, id):
    compatibility_acc_delete = compatibility_acc.objects.get(id=id)
    compatibility_acc_delete.delete()
    return redirect("/compatibility")

def form_editing_compatibility(request):
    compatibility_edit = compatibility_acc.objects.get(id=add_id_edit["id"])
    compatibility_edit.code_product = product.objects.get(code = request.POST["select_compatibility1"].split(" / ")[0])
    compatibility_edit.code_ref = product.objects.get(code = request.POST["select_compatibility2"].split(" / ")[0])
    compatibility_edit.save()
    return redirect("/compatibility")

def register_compatibility(request):
    compatibility_acc.objects.create(
        code_product = product.objects.get(code = request.POST["select_compatibility1"].split(" / ")[0]),
        code_ref = product.objects.get(code = request.POST["select_compatibility2"].split(" / ")[0])
    )
    return redirect("/compatibility")


# Errors Pages

def page_404(request, exception):
    return HttpResponse("Page not found - code 404")

def page_500(request):
    return HttpResponse("view error - code 500")

def page_403(request, exception):
    return HttpResponse("Permision denied - code 403")

def page_400(request, exception):
    return HttpResponse("Bad request - code 400")