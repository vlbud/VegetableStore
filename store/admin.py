from .models import Product, Category,Discount,Profile,Wishlist
from django.contrib import admin


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Profile)
admin.site.register(Wishlist)
