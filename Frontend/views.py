import re


from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect, get_object_or_404
from Backend.models import CategoryDB,ProductDB,MembersDB
from Frontend.models import RegistrationDB,SellDB,wishlistDB,ContactDB,EnquiryDB,RatingDB,BookingDB,PaymentDB,VisitDB
from django.contrib import messages
from django.core.exceptions import ValidationError

# Create your views here.
def homepage(request):
    data = CategoryDB.objects.all()
    pro = ProductDB.objects.all()
    mem = MembersDB.objects.all()
    sell = SellDB.objects.all()
    rate = RatingDB.objects.all()
    return render(request, "Home.html", {'data': data, 'pro': pro,'mem':mem,'sell':sell,'rate':rate})

def propertypage(request, pro_name):
    cat = CategoryDB.objects.all()
    data = ProductDB.objects.filter(Category_Name=pro_name)
    return render(request, "Properties.html", {'data': data,'cat':cat})

# def singleproperty(request, dataid):
#     pro = RegistrationDB.objects.get(Username=request.session['Username'])
#     data = ProductDB.objects.get(id=dataid)
#     return render(request, "SingleProperty.html", {'data':data,'pro':pro})
def singleproperty(request, dataid):
    pro = None  # Initialize pro as None
    if 'Username' in request.session:
        pro = RegistrationDB.objects.get(Username=request.session['Username'])

    try:
        data = ProductDB.objects.get(id=dataid)
        return render(request, "SingleProperty.html", {'data': data, 'pro': pro})
    except ProductDB.DoesNotExist:
        # Handle the case where the SellDB object with the given ID doesn't exist
        return HttpResponse("Property not found", status=404)

def servicepage(request):
    cat = CategoryDB.objects.all()
    data = RatingDB.objects.all()
    return render(request, "Services.html",{'data':data,'cat':cat})


def contactpage(request):
    cat = CategoryDB.objects.all()
    return render(request, "Contact.html",{'cat':cat})
def savecontact(request):
    if request.method=="POST":
        nam = request.POST.get('cont_name')
        mail = request.POST.get('cont_mail')
        sub = request.POST.get('cont_subject')
        msg = request.POST.get('cont_msg')
        obj = ContactDB(Contact_Name=nam,Email=mail,Subject=sub,Message=msg)
        obj.save()
        messages.success(request, "Your message sent successfully")
        return redirect(contactpage)


def aboutpage(request):
    cat = CategoryDB.objects.all()
    mem = MembersDB.objects.all()
    return render(request, "About.html",{'cat':cat,'mem':mem})

# def userregpage(request):
#     return render(request,"UserReg.html")

def editprofile(request):
    pro=RegistrationDB.objects.get(Username=request.session['Username'])
    return render(request,"EditProfile.html",{'pro':pro})

def save_data(request):
    if request.method=="POST":
        un = request.POST.get('u_name')
        pd = request.POST.get('u_password')
        mob = request.POST.get('u_mobile')
        um = request.POST.get('u_mail')
        add = request.POST.get('u_address')
        pic = request.FILES['pro_pic']
        try:
            obj = RegistrationDB(Username=un, Password=pd, Mobile_User=mob, Mail=um, Address=add, Profile_Pic=pic)
            obj.full_clean()  # Validate the model fields
            obj.save()
            messages.success(request, "Registration Successful")
            return redirect(userlogpage)
        except ValidationError as e:
            messages.error(request, e.message_dict)
    return render(request, "UserReg.html")

def updateprofile(request,dataid):
    if request.method=="POST":
        un = request.POST.get('u_name')
        pd = request.POST.get('u_password')
        mob = request.POST.get('u_mobile')
        um = request.POST.get('u_mail')
        add = request.POST.get('u_address')
        try:
            pic = request.FILES['pro_pic']
            fs = FileSystemStorage()
            file = fs.save(pic.name, pic)
        except MultiValueDictKeyError:
            file = RegistrationDB.objects.get(id=dataid).Profile_Pic
        RegistrationDB.objects.filter(id=dataid).update(Username=un,Password=pd,Mobile_User=mob,Mail=um,Address=add,Profile_Pic=file)
        messages.success(request, "Updated Successfully...")
        return redirect(homepage)



def userlogpage(request):
    return render(request, "UserLogin.html")

def User_Login(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if RegistrationDB.objects.filter(Username=uname, Password=pwd).exists():
            request.session['Username'] = uname
            request.session['Password'] = pwd
            messages.success(request, "Login Successfull")
            return redirect(homepage)
        else:
            return redirect(userlogpage)
    return redirect(userlogpage)

def userlogout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Logged Out Successfully")
    return redirect(homepage)

#wishlist
def savewish(request):
    if request.method=="POST":
        usern = request.POST.get('user_name')
        prop = request.POST.get('pro_place')
        add = request.POST.get('pro_add')
        bed = request.POST.get('pro_bed')
        bath = request.POST.get('pro_bath')
        pri = request.POST.get('pro_price')
        obj = wishlistDB(Username=usern,Propertyplace=prop,Address=add,Bedrooms=bed,Bathrooms=bath,Price=pri)
        messages.success(request, "Added to wishlist")
        obj.save()
        return redirect(homepage)

def displaywishlist(request):
    data = wishlistDB.objects.filter(Username=request.session['Username'])
    return render(request, "Wishlist.html", {'data': data})

def deletewishlist(request,dataid):
    data = wishlistDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displaywishlist)

#sell property

def sellproperty(request):
    data = CategoryDB.objects.all()
    return render(request,"SellProperty.html",{'data':data})

def saveproperty(request):
    if request.method=="POST":
        cn = request.POST.get('s_cname')
        place = request.POST.get('p_place')
        add = request.POST.get('p_address')
        bed = request.POST.get('p_bed')
        bath = request.POST.get('p_bath')
        des = request.POST.get('p_des')
        pri = request.POST.get('p_price')
        sqf = request.POST.get('p_sqft')
        img1 = request.FILES['p_img1']
        img2 = request.FILES['p_img2']
        img3 = request.FILES['p_img3']
        use = request.POST.get('user_name')
        mob = request.POST.get('u_mobile')
        pl = request.POST.get('u_place')
        pro = request.FILES['u_pro']
        obj1 = SellDB(Category_Name=cn,Property_place=place,Property_Address=add,Bedroom=bed,Bathroom=bath,Property_Description=des,Rate=pri,SqFeet=sqf,Photo1=img1,Photo2=img2,Photo3=img3,Username=use,Mobile=mob,User_Place=pl,Profile_Picture=pro)
        obj1.save()
        messages.success(request, "You have added your property")
        return redirect(homepage)
def editsellpage(request,sellid):
    cat = CategoryDB.objects.all()
    data = SellDB.objects.get(id=sellid)
    return render(request,"Editsellproperty.html",{'cat':cat,'data':data})

def updatesellpage(request,dataid):
    cn = request.POST.get('s_cname')
    place = request.POST.get('p_place')
    add = request.POST.get('p_address')
    bed = request.POST.get('p_bed')
    bath = request.POST.get('p_bath')
    des = request.POST.get('p_des')
    pri = request.POST.get('p_price')
    sqf = request.POST.get('p_sqft')
    try:
        img1 = request.FILES['p_img1']
        fs = FileSystemStorage()
        file = fs.save(img1.name, img1)
    except MultiValueDictKeyError:
        file = SellDB.objects.get(id=dataid).Photo1
    try:
        img2 = request.FILES['pimg2']
        fs = FileSystemStorage()
        file1 = fs.save(img2.name, img2)
    except MultiValueDictKeyError:
        file1 = SellDB.objects.get(id=dataid).Photo2
    try:
        img3 = request.FILES['pimg3']
        fs = FileSystemStorage()
        file2 = fs.save(img3.name, img3)
    except MultiValueDictKeyError:
        file2 = SellDB.objects.get(id=dataid).Photo3
    use = request.POST.get('user_name')
    mob = request.POST.get('u_mobile')
    pl = request.POST.get('u_place')
    try:
        pro = request.FILES['u_pro']
        fs = FileSystemStorage()
        file3 = fs.save(pro.name, pro)
    except MultiValueDictKeyError:
        file3 = SellDB.objects.get(id=dataid).Profile_Picture
    SellDB.objects.filter(id=dataid).update(Category_Name=cn,Property_place=place,Property_Address=add,Bedroom=bed,Bathroom=bath,Property_Description=des,Rate=pri,SqFeet=sqf,Photo1=file,Photo2=file1,Photo3=file2,Username=use,Mobile=mob,User_Place=pl,Profile_Picture=file3)
    messages.success(request, "Updated Successfully")
    return redirect(myproperty)

def deletesellpage(request,sellid):
    data = SellDB.objects.filter(id=sellid)
    data.delete()
    messages.warning(request, "You have deleted your property")
    return redirect(homepage)

#profile
def profilepage(request):
    pro = RegistrationDB.objects.get(Username=request.session['Username'])
    return render(request,"ProfileDetails.html",{'pro':pro})

#Myproperty

def myproperty(request):
    data = SellDB.objects.filter(Username=request.session['Username'])
    return render(request,"Myproperty.html",{'data':data})


#featured_userproperty
def featuredproperty(request,pro_name):
    cat = CategoryDB.objects.all()
    data = SellDB.objects.filter(Category_Name=pro_name)
    return render(request,"User_Properties.html",{'data':data,'cat':cat})

# def usersingleproperty(request, dataid):
#     pro = RegistrationDB.objects.get(Username=request.session['Username'])
#     data = SellDB.objects.get(id=dataid)
#     return render(request, "User_singleproperty.html", {'data':data,'pro':pro})
def usersingleproperty(request, dataid):
    pro = None  # Initialize pro as None
    if 'Username' in request.session:
        pro = RegistrationDB.objects.get(Username=request.session['Username'])

    try:
        data = SellDB.objects.get(id=dataid)
        return render(request, "User_singleproperty.html", {'data': data, 'pro': pro})
    except SellDB.DoesNotExist:
        # Handle the case where the SellDB object with the given ID doesn't exist
        return HttpResponse("Property not found", status=404)


def property_search(request):
    Propertyplace = request.GET.get('Propertyplace', '')  # Get the search criteria from the form

    # Check if a search criteria is provided
    if Propertyplace:
        # Perform the search using the filter() method
        properties = ProductDB.objects.filter(Propertyplace__icontains=Propertyplace)
    else:
        # If no criteria is provided, return all properties
        properties = ProductDB.objects.all()

    # Pass the filtered properties to the template
    context = {'data': properties}
    return render(request, 'Properties.html', context)

def property_search1(request):
    Property_place = request.GET.get('Property_place', '')  # Get the search criteria from the form

    # Check if a search criteria is provided
    if Property_place:
        # Perform the search using the filter() method
        properties = SellDB.objects.filter(Property_place__icontains=Property_place)
    else:
        # If no criteria is provided, return all properties
        properties = SellDB.objects.all()

    # Pass the filtered properties to the template
    context = {'data': properties}
    return render(request, 'User_Properties.html', context)



# enquiry
def saveenquiry(request):
    if request.method=="POST":
        usern = request.POST.get('username')
        mob = request.POST.get('mobile')
        add = request.POST.get('property_address')
        mob1 = request.POST.get('u_mobile')
        agn = request.POST.get('agname')
        obj = EnquiryDB(Username=usern,Mobile=mob,Address=add,Mobile_User=mob1,Agent=agn)
        obj.save()
        messages.success(request, "Enquiry Sent")
        return redirect(homepage)

def displayenquiry(request):
    data = EnquiryDB.objects.filter(Username=request.session['Username'])
    return render(request,"Enquiryrequest.html",{'data':data})

def deleteenquiry(request,dataid):
    data = EnquiryDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displayenquiry)

def displaynotification(request):
    data = EnquiryDB.objects.all()
    return render(request, "Notification.html",{'data':data})
def deleteenq(request,dataid):
    data = EnquiryDB.objects.filter(id=dataid)
    data.delete()
    return redirect(displaynotification)


def saverating(request):
    if request.method=="POST":
        usern = request.POST.get('username')
        sug = request.POST.get('suggestion')
        rat = request.POST.get('property_rating')
        obj = RatingDB(Username=usern,Suggestion=sug,Rating=rat)
        obj.save()
        messages.success(request, "Rating added..")
        return redirect(homepage)

def checkout(request):
    data = BookingDB.objects.filter(Username=request.session['Username'])
    return render(request, "Checkout.html",{'data':data})

def savecheckout(request):
    if request.method=="POST":
        bdate = request.POST.get('currentDatetime')
        usern = request.POST.get('b_username')
        mob = request.POST.get('b_mobile')
        mai = request.POST.get('b_mail')
        add = request.POST.get('b_address')
        price = request.POST.get('b_price')
        addp = request.POST.get('b_proaddress')
        agn = request.POST.get('ag_name')
        amob = request.POST.get('ag_mob')
        obj = BookingDB(Username=usern,Mobile_User=mob,Mail=mai,Address=add,Booking_date=bdate,Property_Address=addp,Price=price,Agent_Name=agn,Agent_Mobile=amob)
        obj.save()
        return redirect(checkout)



def savepayment(request):
    if request.method=="POST":
        bdate = request.POST.get('currentDatetime')
        usern = request.POST.get('b_username')
        mob = request.POST.get('b_mobile')
        mai = request.POST.get('b_mail')
        add = request.POST.get('b_address')
        price = request.POST.get('b_price')
        addp = request.POST.get('b_proaddress')
        agn = request.POST.get('ag_name')
        amob = request.POST.get('ag_mob')
        cdn = request.POST.get('p_card')
        exp = request.POST.get('p_exp')
        cv = request.POST.get('p_cvv')
        obj = PaymentDB(Username=usern,Mobile_User=mob,Mail=mai,Address=add,Booking_date=bdate,Property_Address=addp,Price=price,Agent_Name=agn,Agent_Mobile=amob,Card_number=cdn,Expiry_date=exp,CVV=cv)
        obj.save()
        messages.success(request, "Successfully Paid")
        return redirect(homepage)



# def download_booking_pdf(req, infoid):
#     booking = get_object_or_404(BookingDB, Bookingid=infoid)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="booking_{booking.Bookingid}.pdf"'
#     p = canvas.Canvas(response)
#     p.drawString(100, 750, f"Booking ID: {booking.Bookingid}")
#     p.drawString(100, 710, f"Booking Date: {booking.Booking_date.strftime('%Y-%m-%d')}")
#     p.drawString(100, 690, f"Booked By: {booking.Username}")
#     p.drawString(100, 670, f"Mobile: {booking.Mobile_User}")
#     p.drawString(100, 650, f"Email: {booking.Mail}")
#     p.drawString(100, 630, f"Address: {booking.Address}")
#     p.drawString(100, 600, f"Price: {booking.Price}")
#     p.drawString(100, 580, f"Property Address: {booking.Property_Address}")
#     p.drawString(100, 550, f"Agent Name: {booking.Agent_Name}")
#     p.drawString(100, 510, f"Agent Mobile: {booking.Agent_Mobile}")
#     p.showPage()
#     p.save()
#     return response

def displaybooking(request):
    data = BookingDB.objects.filter(Username=request.session['Username'])
    return render(request,"View_Booking.html",{'data':data})


def deletebooking(request,dataid):
    data = BookingDB.objects.filter(Bookingid=dataid)
    data.delete()
    return redirect(displaybooking)

def cancelbooking(request,dataid):
    data = BookingDB.objects.filter(Bookingid=dataid)
    data.delete()
    return redirect(checkout)

def bookvisit(request):
    if request.method=="POST":
        vdate = request.POST.get('visiting_date')
        vtime = request.POST.get('visiting_time')
        existing_appointment = VisitDB.objects.filter(Visit_date=vdate, Visit_time=vtime).first()
        if existing_appointment:
            messages.error(request, "Cannot make an appointment at this time. Please choose a different time.")
        else:
            nam = request.POST.get('name')
            mob = request.POST.get('mobile')
            prop = request.POST.get('pro_address')
            obj = VisitDB(Name=nam,Visit_date=vdate,Visit_time=vtime,Mobile=mob,Property_Address=prop)
            obj.save()
            messages.success(request, "Booked your visit..")
        return redirect(homepage)

