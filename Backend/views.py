from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Backend.models import CategoryDB,ProductDB,MembersDB
from Frontend.models import RegistrationDB,EnquiryDB,BookingDB



# Create your views here.

def indexpage(request):
    data = RegistrationDB.objects.all()
    return render(request,"Index.html",{'data':data})

def addcategory(request):
    return render(request,"AddCategory.html")

def savedata(request):
    if request.method=="POST":
        cn = request.POST.get('p_name')
        des = request.POST.get('p_des')
        img = request.FILES['p_img']
        obj = CategoryDB(Category_Name=cn,Description=des,Image=img)
        obj.save()
        return redirect(addcategory)

def displaycategory(request):
    data = CategoryDB.objects.all()
    return render(request,"Displaycategory.html",{'data':data})

def editcategory(request,dataid):
    data = CategoryDB.objects.get(id=dataid)
    return render(request,"EditCategory.html",{'data':data})

def updatecategory(request,dataid):
    if request.method=="POST":
        cn = request.POST.get('p_name')
        des = request.POST.get('p_des')
        try:
            img = request.FILES['p_img']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).Image
        CategoryDB.objects.filter(id=dataid).update(Category_Name=cn,Description=des,Image=file)
        return redirect(displaycategory)

def deletecategory(request,dataid):
    data = CategoryDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)

def addproperty(request):
    data = CategoryDB.objects.all()
    return render(request,"AddProperty.html",{'data':data})

def savedata1(request):
    if request.method=="POST":
        cn = request.POST.get('p_cname')
        place = request.POST.get('proplace')
        add = request.POST.get('address')
        bed = request.POST.get('bedroom')
        bath = request.POST.get('bathroom')
        des = request.POST.get('description')
        pri = request.POST.get('price')
        sqf = request.POST.get('sqfeet')
        img1 = request.FILES['pimg1']
        img2 = request.FILES['pimg2']
        img3 = request.FILES['pimg3']
        an = request.POST.get('a_name')
        dis = request.POST.get('a_des')
        mob = request.POST.get('a_mobile')
        pl = request.POST.get('a_place')
        pro = request.FILES['a_pro']
        gmap = request.POST.get('g_map')
        obj1 = ProductDB(Category_Name=cn,Propertyplace=place,Address=add,Bedrooms=bed,Bathrooms=bath,Description=des,Price=pri,Sqfeet=sqf,Image1=img1,Image2=img2,Image3=img3,Agent_Name=an,Designation=dis,Mobile=mob,Agent_Place=pl,Profile=pro,Googlemap=gmap)
        obj1.save()
        return redirect(addproperty)

def displayproperty(request):
    data = ProductDB.objects.all()
    return render(request,"DisplayProperty.html",{'data':data})

def editproperty(request,dataid):
    cat = CategoryDB.objects.all()
    data = ProductDB.objects.get(id=dataid)
    return render(request,"EditProperty.html",{'data':data,'cat':cat})

def updateproperty(request,dataid):
    cn = request.POST.get('p_cname')
    place = request.POST.get('proplace')
    add = request.POST.get('address')
    bed = request.POST.get('bedroom')
    bath = request.POST.get('bathroom')
    des = request.POST.get('description')
    pri = request.POST.get('price')
    sqf = request.POST.get('sqfeet')
    try:
        img1 = request.FILES['pimg1']
        fs = FileSystemStorage()
        file = fs.save(img1.name, img1)
    except MultiValueDictKeyError:
        file = ProductDB.objects.get(id=dataid).Image1
    try:
        img2 = request.FILES['pimg2']
        fs = FileSystemStorage()
        file1 = fs.save(img2.name, img2)
    except MultiValueDictKeyError:
        file1 = ProductDB.objects.get(id=dataid).Image2
    try:
        img3 = request.FILES['pimg3']
        fs = FileSystemStorage()
        file2 = fs.save(img3.name, img3)
    except MultiValueDictKeyError:
        file2 = ProductDB.objects.get(id=dataid).Image3
    an = request.POST.get('a_name')
    dis = request.POST.get('a_des')
    mob = request.POST.get('a_mobile')
    pl = request.POST.get('a_place')
    try:
        pro = request.FILES['a_pro']
        fs = FileSystemStorage()
        file4 = fs.save(pro.name, pro)
    except MultiValueDictKeyError:
        file4 = ProductDB.objects.get(id=dataid).Profile
    ProductDB.objects.filter(id=dataid).update(Category_Name=cn,Propertyplace=place,Address=add,Bedrooms=bed,Bathrooms=bath,Description=des,Price=pri,Sqfeet=sqf,Image1=file,Image2=file1,Image3=file2,Agent_Name=an,Designation=dis,Mobile=mob,Agent_Place=pl,Profile=file4)
    return redirect(displayproperty)

def deleteproperty(request,dataid):
    data = ProductDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproperty)

#admin session

def adminlogin(request):
    return render(request,"Adminlogin.html")

def adminlogpage(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        psd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname,password=psd)
            if user is not None:
                login(request,user)
                request.session['username'] = uname
                request.session['password'] = psd
                return redirect(indexpage)
            else:
                return redirect(adminlogin)
        else:
            return redirect(adminlogin)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(indexpage)
#members
def addmembers(request):
    return render(request,"AddMembers.html")

def savemember(request):
    if request.method=="POST":
        nam = request.POST.get('m_name')
        role = request.POST.get('m_role')
        img = request.FILES['m_img']
        obj5 = MembersDB(Name=nam,Role=role,Image=img)
        obj5.save()
        return redirect(addmembers)

def displaymembers(request):
    mem = MembersDB.objects.all()
    return render(request,"Displaymembers.html",{'mem':mem})

def editmembers(request,memberid):
    mdata = MembersDB.objects.get(id=memberid)
    return render(request,"Editmembers.html",{'mdata':mdata})

def updatemembers(request,memberid):
    if request.method == "POST":
        nam = request.POST.get('m_name')
        role = request.POST.get('m_role')
        try:
            img = request.FILES['m_img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = MembersDB.objects.get(id=memberid).Image
        MembersDB.objects.filter(id=memberid).update(Name=nam,Role=role,Image=file)
        return redirect(displaymembers)

def deletemembers(request,memberid):
    mdata = MembersDB.objects.filter(id=memberid)
    mdata.delete()
    return redirect(displaymembers)

def display_users(request):
    data = RegistrationDB.objects.all()
    return render(request,"Display_users.html",{'data':data})

def view_users(request,dataid):
    data = RegistrationDB.objects.get(id=dataid)
    return render(request,"View_users.html",{'data':data})

def display_enquiry(request):
    data = EnquiryDB.objects.all()
    return render(request,"Enquiry_request.html",{'data':data})

def view_bookingAR(request):
    data = BookingDB.objects.all()
    return render(request,"ViewBooking.html",{'data':data})












