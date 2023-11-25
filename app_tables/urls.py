from django.urls import path
from .views import  (
    home_html, 
    motorcycle_html, 
    products_html, 
    compatibility_html, 
    edit, 
    products_html_delete, 
    register_product, 
    form_editing,
    edit_m,
    motorcycle_html_delete,
    form_editing_motorcycle,
    register_motorcycle,
    edit_c,
    compatibility_html_delete,
    form_editing_compatibility,
    register_compatibility,
    login_html,
    sign_up, 
)

urlpatterns = [
    path('', login_html, name="login"),
    path('home/', home_html, name="home"),
    path('motorcycle/', motorcycle_html, name="motorcycle"),
    path('products/', products_html, name="products"),
    path('compatibility/', compatibility_html, name="compatibility"),
    #Functions for products
    path('edit/<int:id>/', edit, name="edit"),
    path('delete/<int:id>/', products_html_delete, name="delete"),
    path('form_send/', register_product, name="form_send"),
    path('form_editing/', form_editing, name="form_editing"),
    #Functions for motorcycle
    path('edit_m/<int:id>/', edit_m, name="edit_m"),
    path('delete_m/<int:id>/', motorcycle_html_delete, name="delete_m"),
    path('form_editing_motorcycle/', form_editing_motorcycle, name="form_editing_motorcycle"),
    path('form_send_motorcycle/', register_motorcycle, name="form_send_motorcycle"),
    #Functions for compatibility
    path('edit_c/<int:id>/', edit_c, name="edit_c"),
    path('delete_c/<int:id>/', compatibility_html_delete, name="delete_c"),
    path('form_editing_compatibility/', form_editing_compatibility, name="form_editing_compatibility"),
    path('form_send_compatibility/', register_compatibility, name="form_send_compatibility"),
    #Functions for login
    path('sign_up/', sign_up, name="sign_up"),
]