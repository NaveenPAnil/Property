from django.urls import path
from Frontend import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('propertypage/<pro_name>/',views.propertypage,name="propertypage"),
    path('singleproperty/<int:dataid>/',views.singleproperty,name="singleproperty"),
    path('servicepage/',views.servicepage,name="servicepage"),


    path('contactpage/',views.contactpage,name="contactpage"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),




    path('editprofile/', views.editprofile, name="editprofile"),
    path('updateprofile/<int:dataid>/', views.updateprofile, name="updateprofile"),
    path('userlogpage/', views.userlogpage, name="userlogpage"),
    path('save_data/',views.save_data,name="save_data"),
    path('User_Login/',views.User_Login,name="User_Login"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('profilepage/',views.profilepage,name="profilepage"),
    path('myproperty/',views.myproperty,name="myproperty"),


    path('checkout/',views.checkout,name="checkout"),
    path('savecheckout/',views.savecheckout,name="savecheckout"),
    path('savepayment/',views.savepayment,name="savepayment"),
    path('displaybooking/',views.displaybooking,name="displaybooking"),
    # path('download_booking_pdf/',views.download_booking_pdf,name="download_booking_pdf"),
    path('deletebooking/<int:dataid>/',views.deletebooking,name="deletebooking"),
    path('cancelbooking/<int:dataid>/',views.cancelbooking,name="cancelbooking"),

    path('bookvisit/',views.bookvisit,name="bookvisit"),



    path('savewish/',views.savewish,name="savewish"),
    path('displaywishlist/',views.displaywishlist,name="displaywishlist"),
    path('deletewishlist/<int:dataid>/',views.deletewishlist,name="deletewishlist"),

    path('sellproperty/',views.sellproperty,name="sellproperty"),
    path('editsellpage/<int:sellid>/',views.editsellpage,name="editsellpage"),
    path('updatesellpage/<int:dataid>/',views.updatesellpage,name="updatesellpage"),
    path('deletesellpage/<int:sellid>/',views.deletesellpage,name="deletesellpage"),
    path('saveproperty/',views.saveproperty,name="saveproperty"),

    path('featuredproperty/<pro_name>/',views.featuredproperty,name="featuredproperty"),
    path('usersingleproperty/<int:dataid>/',views.usersingleproperty,name="usersingleproperty"),


    path('property_search/',views.property_search,name="property_search"),
    path('property_search1/',views.property_search1,name="property_search1"),

    path('saveenquiry/',views.saveenquiry,name="saveenquiry"),
    path('displayenquiry/',views.displayenquiry,name="displayenquiry"),
    path('deleteenquiry/<int:dataid>/',views.deleteenquiry,name="deleteenquiry"),
    path('deleteenq/<int:dataid>/',views.deleteenq,name="deleteenq"),

    path('displaynotification/',views.displaynotification,name="displaynotification"),

    path('saverating/',views.saverating,name="saverating"),




]