from django.urls import path
from Backend import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('savedata/',views.savedata,name="savedata"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),
    path('addproperty/', views.addproperty, name="addproperty"),
    path('savedata1/', views.savedata1, name="savedata1"),
    path('displayproperty/',views.displayproperty,name="displayproperty"),
    path('editproperty/<int:dataid>/', views.editproperty, name="editproperty"),
    path('updateproperty/<int:dataid>/', views.updateproperty, name="updateproperty"),
    path('deleteproperty/<int:dataid>/',views.deleteproperty,name="deleteproperty"),
    path('adminlogin/', views.adminlogin, name="Adminlogin.html"),
    path('adminlogpage/', views.adminlogpage, name="adminlogpage"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('addmembers/', views.addmembers, name="addmembers"),
    path('savemember/', views.savemember, name="savemember"),
    path('displaymembers/', views.displaymembers, name="displaymembers"),
    path('editmembers/<int:memberid>/',views.editmembers,name="editmembers"),
    path('updatemembers/<int:memberid>/',views.updatemembers,name="updatemembers"),
    path('deletemembers/<int:memberid>/',views.deletemembers,name="deletemembers"),
    path('display_users/',views.display_users,name="display_users"),
    path('view_users/<int:dataid>/',views.view_users,name="view_users"),
    path('display_enquiry/',views.display_enquiry,name="display_enquiry"),

    path('view_bookingAR/',views.view_bookingAR,name="view_bookingAR"),




]