from django.contrib import admin
from Backend.models import CategoryDB,ProductDB,MembersDB
from Frontend.models import RegistrationDB,SellDB,wishlistDB,ContactDB,EnquiryDB,RatingDB,BookingDB

# Register your models here.
admin.site.register(CategoryDB)
admin.site.register(ProductDB)
admin.site.register(MembersDB)

#Frontend
admin.site.register(RegistrationDB)
admin.site.register(SellDB)
admin.site.register(wishlistDB)
admin.site.register(ContactDB)
admin.site.register(EnquiryDB)
admin.site.register(RatingDB)
admin.site.register(BookingDB)



