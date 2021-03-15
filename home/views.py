from django.shortcuts import render,redirect
import africastalking
from .models import*
from .serializers import*
import codecs
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser,FileUploadParser
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import urllib,json

username = "nesjoselyne@gmail.com"
api_key = "7d5ec7e665579ee7ef1a3a71927f74123d0542960de776089cc89b28b4977804"
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import datetime
from random import randint
from django.core.signing import Signer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def welcome(request):
    return render(request,'harvest.html') 
def kiny(request):
    return render(request,'kiny.html') 
def index(request):
    return render(request,'index.html') 
def cooperative(request):
    return render(request,'cooperative.html') 


def work(request):
    return render(request,'work.html')    

def pay(request):
    return render(request,'pay.html')    
# def register(request):
#     return render(request,'register.html')
def signin(request):
    return render(request,'signin.html')      
def record(request):
    return render(request,'record.html')
    # ussd
@csrf_exempt
def digitalapp (request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_numer = request.POST.get('phonenumer')
        text = request.POST.get('text')
        level = text.split('*')
        response = ''
        num = text[:3]

        if text == '':
            response = 'CON murakaza neza kurubuga rwabahinzi Smart ikigega \n'
            response += '1.ikigega pay \n'
            response += '2.ibijyanye numusaruro \n'
            response += '3.kwiyandikisha mukigega \n'
            response += '4.kubarura umusaruro \n'
            #  harvesting session
        elif text == '1':
            response = 'CON kwishyura \n'
            response += '1.uri mukigega \n'
            response += '2.momo isanzwe'
        elif text == '1*1':
            response = 'CON shyiramo code yumuhinzi '+str(level)+' \n' 
            # insert=Harvestrecord.objects.filter(farmercode=str(level[2]))
            # insert.save()
        elif num == '1*1' and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON shyiramo ingano yumusaruro mu biro cg litiro \n'
            # insert=Harvestrecord.objects.create(Quantity=str(level[3]))
            # insert.save()
        elif num == '1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON shyiramo amafaranga ugiye kwishyura \n' 
        elif num == '1*1' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON  wahisemo kwishyura'+ str(level[4]) + 'ugiye kwishyura kuri' + str(level[2]) +'shyiramo umubare wibanga wemeze kwishyura  \n'
        elif text == '1*2':
            response = 'CON nimero ya mobile : '+str(len(level))+ '\n'        
            # insert=Harvestrecord.objects.create(farmercode=str(level[2]))
            # insert.save()
        elif num == '1*2' and int(len(level))==2 and str(level[3]) in str(level):
            response = 'CON umubare wamafaranga  \n'
        elif num == '1*2' and int(len(level))==3 and str(level[4]) in str(level):
            response = 'CON wahisemo kwishyura'+ str(level[4]) + 'ugiye kwishyura kuri' + str(level[2]) +'shyiramo umubare wibanga wemeze kwishyura  \n'   
         
        
        elif text == '2':
            response = 'CON  hitamo \n'
            response += '1.kureba umusaruro mbumbe \n'
            response += '2.ubwishingizi bwumusaruro \n'
            response += '3.ikigega Loan'
        elif text == '2*1':
            response = 'CON  shyiramo code yawe ubashe kureba umusaruro :' +str(len(level))+ '\n'
            
        elif num == '2*1'and int(len(level))==3 and str(level[2]) in str(level):
            # insert=Harvestrecord(Quantity=str(level[3]))
            # if insert.is_valid():
             response = 'CON hitamo kureba \n'
             response += '1.umusaruro wukukwezi\n'
             response += '2.umusaruro mbumbe wose'
            # response = 'CON code mwashyizemo ntibaho : \n'
                 
        elif text =='2*1*1':
            response = 'CON umusaruro wa' + str(level[2]) +'wukukwezi ni 360kg'+str(level[3])+'\n'
        elif text =='2*1*2':
            response = 'CON umusaruro mbumbe wa' + str(level[2]) + 'ni 3600kg'+str(level[3])+'\n'
        elif text == '2*2':
            response = 'CON  ubwishingizi bw \n'
            response += '1.umwaka umwe \n'
            response += '2.imyaka itanu  \n'
            response += '3.imyaka icumi '   
        elif text == '2*2*1':
            response = 'CON  shyiramo code yawe ubashe kwinjira mu bwishingizi bwumwaka umwe:' +str(len(level))+ '\n'
        elif num == '2*2*1'and int(len(level))==4 and str(level[3]) in str(level):
             response = 'CON kwiyandikisha gusaba ubwishingizi bwumwaka byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n'   
            #  insert=Insurance.objects.filter(farmercode=str(level[4])) 
            #  insert.save()     

        elif text == '2*2*2':
            response = 'CON  shyiramo code yawe ubashe kwinjira mubwishingizi bwimyaka itanu :' +str(len(level))+ '\n'
        elif num == '2*2*2'and int(len(level))==4 and str(level[3]) in str(level):  
            response = 'CON kwiyandikisha gusaba ubwishingizi bwimyaka 5 byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n' 
            # insert=Insurance.objects.filter(farmercode=str(level[4])) 
            # insert.save()                        
            # response = 'CON code mwashyizemo ntibaho : \n'
        elif text == '3':
            response = 'CON  hitamo kwiyandikisha  nk \n'
            response += '1. itsinda(cooperative)\n'
            response += '2.umuhinzi ku giti cye '
        elif text == '3*1':
            response = 'CON  shyiramo izina rya cooperative :' +str(len(level))+ '\n'
            # insert = Cooperativesreg.objects.create(name=str(level[2]))
            # insert.save() 
        elif num == '3*1'and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON  shyiramo izina ryumuyobozi wa cooperative' +str(len(level))+ '\n'
            # insert= Cooperativesreg.objects.create(leadername=str(level[3]))
            # insert.save()   

        elif num == '3*1'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON  shyiramo numero zumuyobozi wa cooperative :' +str(len(level))+ '\n'
            # insert= Cooperativesreg.objects.create(leaderphone=str(level[4]))
            # insert.save()   
        elif num == '3*1'and int(len(level))==5 and str(level[4]) in str(level):  
            response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega nkitsinda bwakiriwe urahabwa igisubizo mu gihe gito' +str(len(level))+ '\n'  
        elif text == '3*2':
            response = 'CON  shyiramo izina rya mbere :' +str(len(level))+ '\n'
            # insert= Regfarmer.objects.create(firstname=str(level[2]))
            # insert.save()
        elif num == '3*2'and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON  shyiramo izina rya kabiri \n'
            # insert= Regfarmer.objects.create(lastname=str(level[3]))
            # insert.save()
        elif num == '3*2'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON  shyiramo numero yawe ya telephone \n'
            # insert= Regfarmer.objects(telephone=str(level[4]))    
            # insert.save()

        elif num == '3*2' and int(len(level))==5 and str(level[4]) in str(level):  
            response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega bwakiriwe urahabwa igisubizo mu gihe gito \n'
        elif text == '4':
            response = 'CON  shyiramo code yawe ubashe kubarura :' +str(len(level))+ '\n'
        elif num == '4'and int(len(level))==2 and str(level[1]) in str(level):  
            response = 'CON  shyiramo izina rya cooperative \n'  
            # insert=Cooperative.objects.filter(name=str(level[2]))  
            # insert.save()
        elif num == '4' and int(len(level))==3 and str(level[2]) in str(level):  
            response = 'CON  shyiramo code yumuhinzi \n'  
            # insert=Harvestrecord.objects.filter(farmercode=str(level[3]))  
            # insert.save()
        elif num == '4' and int(len(level))==4 and str(level[3]) in str(level):  
            response = 'CON  shyiramo ibiro yagize \n'  
            # insert=Harvestrecord.objects(Quantity=str(level[4]))  
            # insert.save()    
        else:
            response = 'END Invalid Choice'
        
        return HttpResponse(response)

    return HttpResponse('harvest')    
        # return JsonResponse(serializer.errors,status=400)
        #    '
        #     response = 'CON murakaza neza muhinzi wumuceri hitamo ibijyanye na '+str(len(level))+'\n'
        #     response += '1.ikigega pay \n'
        #     response += '2.ibijyanye numusaruro \n'
        #     response += '3.kwiyandikisha mukigega'
        #     # current harvesting session
        # elif text == '1*1':
        #     response = 'CON  shyiramo code yumuhinzi ugiye kwishyura : \n'
        #     response += '1.umusaruro mbumbe wose \n'
        #     response += '2.ingano yumusaruro muri uku kwezi \n'
        # elif text == '1*1*1':
        #     response = 'CON injizamo code yumuhinzi  \n'
        #     insert=Harvestrecord(farmercode=str(level[3]))
        #     insert.save() 
        #     y = input
        #     y =request.POST['farmercode']
        #     v=Harvestrecord.objects.filter(farmercode=y)
        #     for rt in v:
        #         qty = rt.Quantity
        # elif num == '1*1*1' and int(len(level))==4 and str(level[3]) in str(level):
        #     response = 'CON umusaruro mbumbe wawe ni' + qty + ' \n'
        # elif text == '1*1*2':
        #     response = 'CON injizamo code yumuhinzi \n'
        # elif num == '1*1*2'and int(len(level))==4 and str(level[3]) in str(level):
        #     response = 'CON ingano yumusaruro muri uku kwezi ni 140kg \n'
        # #  financial session
        # elif text == '1*2':
        #     response = 'CON murakaza neza  \n'
        #     response += '1. kwishyura umusaruro \n'
        #     response += '2. inguzanyo \n'
        #     response += '3. uko nabona inguzanyo'
        #     # direct loan session
        # elif text == '1*2*1':
        #     response = 'CON injizamo code yumuhinzi ugiye kwishyura '+str(len(level))+' \n'
        # elif num == '1*2*1' and int(len(level))==4 and str(level[3]) in str(level):
        #     response = 'CON shyiramo amafaranga ugiye kwishyura : \n'
        # elif num == '1*2*1' and int(len(level))==5 and str(level[4]) in str(level):
        #     response = 'CON washyizemo' + str(level[4])  + 'ugiye kwishyura '+str(level[3])+  'kuri shyiramo umubare wibanga wemeze: \n'
        # elif num == '1*2*1' and int(len(level))==6 and str(level[5]) in str(level):
        #     response = 'CON  kwishyura amafaranga byagenze neza  murakoze: \n'
        # elif text == '1*2*2':
        #     response = 'CON Enter farmers code '+str(len(level))+' \n'
        # elif num == '1*2*2' and int(len(level))==4 and str(level[3]) in str(level):
        #     response = 'CON Enter the money you want pay: \n'   
        # elif num == '1*2*2' and int(len(level))==5 and str(level[4]) in str(level):
        #     response = 'CON Enter mobile-money pin to pay: \n'   
        # elif num == '1*2*2' and int(len(level))==6 and str(level[5]) in str(level):
        #     response = 'CON you have succesfully paid the loan thanks: \n'   
        # elif text == '1*3':
        #     response = 'CON Other services: \n'
        #     response += '1.how to get crops insurance\n'
        #     response += '2.join crops insurance \n'
        # elif text == '1*3*1':
        #     response = 'END how to get crops insurance: \n'
        #     response += 'in order to get crops insurance you have to be an active member of any registrated cooperative in our system \n'
        # elif text == '1*3*2':
        #     response = 'END  enter the farmers code to get the insurance:'

#farm

# farmercreate

# @csrf_exempt
# def farmercreate(request):
#     if request.method=='GET':
#         reg=Regfarmer.objects.all()
#         serializer=farmerSerializer(reg,many=True)
#         return JsonResponse(serializer.data,safe=False)
        
#     elif request.method=='POST':
#         data=JSONParser().parse(request)
#         serializer=farmerSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'message':'data submited successful'},status=201)
#         return JsonResponse(serializer.errors,status=400)
def LoanRequest(request):
    if request.method=='GET':
        reg=Loan.objects.all()
        serializer=LoanSerializer(reg,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=LoanSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'data submited successful'},status=201)
        return JsonResponse(serializer.errors,status=400)

def InsuranceRequest(request):
    if request.method=='GET':
        reg=Insurance.objects.all()
        serializer=InsuranceSerializer(reg,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=InsuranceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'data submited successful'},status=201)
        return JsonResponse(serializer.errors,status=400)
def Harvestpay(request):
   if request.method == 'GET':
        reg = Payharvest.objects.all()
        serializer = PayharvestSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)
   elif request.method == 'POST':
        data = JSONParser().parse(request) #/request.data
        serializer = PayharvestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successfull','data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)
      

# techer login
class RecordingAuthToken:
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # auth.login(request,user)
        print(user)

        
        token, created = Token.objects.get_or_create(user=user)
        recording=Recorder.objects.filter(user=user)

        for dt in recording:
            record=dt.name

        if Recorder.objects.filter(user=user).exists():
            print('Recorder')
            return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'Recorder':token.key,
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'name':record,
            })
        return JsonResponse({"message":"not registerd as Recorder"},status=400)

#  def logout(request):
#         auth.logout(request)
#     return redirect('/')


# def login(request):
#     if request.method=='POST':
#         userd=request.POST['username']
#         pass1=request.POST['pass']
#         user=auth.authenticate(username=userd,password=pass1)
#         if user is not None:
#             auth.login(request,user)
#             if Workers.objects.filter(user=request.user).exists():
#                 return redirect('worker')
#             elif Active.objects.filter(user=request.user).exists():
#                 return redirect('inside')
#             else:
#                 messages.info(request,'make sure if your account is Activate')
#                 return redirect('login')
#         else:
#             print(userd)
#             print(pass1)
#             messages.info(request,'Check your username and password password ')
#             return redirect('login')
#     else:
#         return render(request,'login.html')
#     return render(request,'login.html')       
def reset(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(email=username).exists():

            subject='Password Resetting- Cityplus'
            message='Dear User, you requested  password reset,  click or copy the link below \n'+'activation link is https://www.cityplus.rw/reset-now/cityplus-password/'+str(username)
            from_email=settings.EMAIL_HOST_USER
            rt=send_mail(subject,message,from_email,[str(username),],fail_silently=True)
            return render(request,'reset.html',{'success':'Reset account link has been sent to your email, check inbox'})

        else:
            return render(request,'reset.html',{'success':'Sorry user with provided email does not exist!'})

    return render(request,'reset.html')

@csrf_exempt
def Recorderaccountcreation(request):
    if request.method=='GET':
        # reg=Teacher.objects.filter(companyname=request.username)
        reg=Recorder.objects.all()
        # print(request.username)
        serializer=RecordingSerializeren(reg,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=RecorderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'account create successful'},status=201)
        return JsonResponse(serializer.errors,status=400)

class CustomAuthToken(ObtainAuthToken):
     def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username':user.username,
            'first_name':user.first_name

        })       

# def registration(request):
#     select = Cooperative.objects.all()
#     if request.method == 'POST':
#         name = request.POST['name']
#         Cooperativedistrict = request.POST['Cooperativedistrict']
#         leaderphone = request.POST['leaderphone']
#         harvesttype = request.POST['harvesttype']
#         leadername = request.POST['leadername']
#         Cooperativesector = request.POST['Cooperativesector']
#         insert = Cooperativesreg(name=name,Cooperativedistrict=Cooperativedistrict,leaderphone=leaderphone, harvesttype= harvesttype,leadername=leadername,Cooperativesector=Cooperativesector)
#         try:
#             insert.save()
#             return render(request,'cooperative.html',{'message':'your request has been succeeful submitted we will  get in touch with u soon','data':select})
#         except :
#             return render(request,'cooperative.html',{'message':'failed to insert','data':select})
#     return render(request,'cooperative.html',{'data':select})

def Harvestrecording(request):
    select = Harvestrecord.objects.all()
    if request.method == 'POST':
        Quantity = request.POST['Quantity']
        farmercode = request.POST['farmercode']
        donetime = request.POST['donetime']
        donedate = request.POST['donedate']
        insert = Harvestrecord(Quantity=Quantity,farmercode=farmercode, donetime=donetime,donedate=donedate)
        try:
            insert.save()
            return render(request,'record.html',{'message':'data submitted successful','data':select})
        except :
            return render(request,'record.html',{'message':'failed to insert','data':select})
    return render(request,'record.html',{'data':select})

# @requires_csrf_token
# def registerEndpoint(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         reg = Cooperativesreg.objects.all()
#         serializer = RegisterSerializer(reg, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request) #request data
#         serializer = RegisterSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'message':'sucecesful registred', 'data':serializer.data}, status=201)
#         return JsonResponse(serializer.errors, status=400)

def registration(request):
    if request.method=='POST':
        # recaptcha_response = request.POST.get('g-recaptcha-response')
        # url = 'https://www.google.com/recaptcha/api/siteverify'
        # values = {
        #     'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        #     'response': recaptcha_response
        # }
        # data = urllib.parse.urlencode(values).encode()
        # req =  urllib.request.Request(url, data=data)
        # response = urllib.request.urlopen(req)
        # result = json.loads(response.read().decode())
        # ''' End reCAPTCHA validation '''

            
            Name=request.POST['name']
            email=request.POST['email']
            password1=request.POST['password1']
            password2=request.POST['password2']
            leaderphone=request.POST['leaderphone']
            district = request.POST['district']
            harvesttype = request.POST['harvesttype']
            signer = Signer()
            passleng=len(password2)
            if password1==password2:

                if passleng>=8:

                    if User.objects.filter(username=Name).exists():
                        messages.info(request,'cooperativename already exist taken')
                        return redirect('register')
                    elif User.objects.filter(email=email).exists():
                        messages.info(request,'Email is already exist taken')
                        return redirect('register')
                    else:
                        subject='Verification from smart ikigega'
                        message='This link is for activating your account on smart ikigega'+'\n'+'your Username:  '+Name+'\n'+'https://harvestendpoint.herokuapp.com/activation/'+email+'/'+signer.sign(email)
                        from_email=settings.EMAIL_HOST_USER
                        rt=send_mail(subject,message,from_email,[str(email),],fail_silently=False)
                        print(rt)
                        if rt==True:
                            user=User.objects.create_user(email=email,username=Name,password=password1,leaderphone=leaderphone,district=district,harvesttype=harvesttype)
                            user.save()
                            mess=email
                            return render(request,'cooperative.html',{'mess':mess})
                        else:
                            messages.info(request,'email is not exist please')
                            return redirect('register')

                else:
                    messages.info(request,'Please fill the 8 and above word for password')
                    return redirect('register')
            else:
                messages.info(request,'Password not match')
                return redirect('register')
    
            
    else:
              
        return render(request,'cooperative.html')


def user(request):
    if str(request.user)=='AnonymousUser':
        return redirect('index')
    else:
        if Recorder.objects.filter(user=str(request.user)):
            return redirect('dashboard')
        else:
            site=sites.objects.all()
    lastcode=Regfarmer.objects.all().order_by('-pub_date')[:1]
    lastcodes=lastcode.count()
    prof=Profilecooperative.objects.filter(cooperative=str(request.user))
 
    reg = Regfarmer.objects.all().filter(cooperative=request.user).order_by('-id')
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        # resi=request.POST['resi']
        gender=request.POST['gender']
        site=25
        tel=request.POST['telephone']
        telephone =tel[1:]
        # now= datetime.datetime.now()
        # froms=request.POST['from']
        # temp=request.POST['temp']
        dateofbirth=request.POST['dateofbirth']
        district =request.POST['district']
        village = request.POST['village']
        # Cooperativesreg = request.POST['cell']

        # years= now.year
        newcode=str(tel)+str(lastname)+str(1)
        one=1
        # if lastcodes ==0:
        lastnum=Regfarmer.objects.filter(telephone=telephone)
        nums=lastnum.count()
        print(nums)
        if nums <= 2:
            def random_with_N_digits(n):
                range_start = 10**(n-1)
                range_end = (10**n)-1
                return randint(range_start, range_end)
            nost = random_with_N_digits(6)
            Regfarmer.objects.create(district=district,village=village,email=email,dateofbirth=dateofbirth,firstname=firstname,lastname=lastname,gender=gender,telephone=telephone,code= nost, Cooperative=str(request.user),user=request.user).save()

            mess='Dear '+str(firstname) +' '+str(lastname) +'\n'+'your  new Smart ikigaga code is : '+str(nost)

            if email != None or tel !=None:
                subject='Thank you for using smart ikigega'
                message='Dear '+str(firstname) +' '+str(lastname) +'\n'+'your code is : '+str(nost)
                from_email=settings.EMAIL_HOST_USER
                rt=send_mail(subject,message,from_email,[str(email),],fail_silently=True)
                #account_sid = 'AC1b41153cd2a60b01893bb9740d2fd875'
                #auth_token = 'efa2a032ba78dff3111fce2efafa5940'
                #client =Client(account_sid, auth_token)
                #message = client.messages.create(body='your Code is: '+nost,from_='+16305280341',to='+250784447864')
                sendsms = requests.post('http://rslr.connectbind.com:8080/bulksms/bulksms?username=1212-pathos&password=Chance@1&type=0&dlr=1&destination='+str(telephone)+'&source=CityPlus&message='+str(mess)+'')
                pass
            else:
                pass
            mess='Dear '+str(firstname) +' '+str(lastname) +'\n'+'your code is : '+str(nost)     
            return render(request,'user.html',{'site':site,'mess':mess,'register':reg})

    else:
        return render(request,'failed.html',{mess:'not created'})
        # if prof.exists():
        #     if Payment.objects.filter(chur_name=str(request.user)).exists():
        #         #print('mpwmw')
        #         last_pay=Payment.objects.filter(chur_name=str(request.user)).order_by('-pay_date')[:1]
        #         for ft in last_pay:
        #             last=ft.pay_date
        #         month_pay=last + datetime.timedelta(30)
        #         date_tod=datetime.date.today()
        #         if month_pay<=date_tod:
        #             instal=10000
        #             bulk=10000
        #             total=instal+bulk
        #             return render(request,'user.html',{'last':last,'month_pay':month_pay,'bulk':bulk,'total':total,'instal':instal,'zipcod':zipcod,'prof':prof,'service':serv})
        #         else:
        #             return render(request,'user.html',{'zipcod':zipcod,'prof':prof,'service':serv})
        #     else:
        #         pay=1
        #         #print(pay)
        #         instal=20000
        #         bulk=10000
        #         total=instal+bulk
        #         return render(request,'user.html',{'bulk':bulk,'total':total,'instal':instal,'pay':pay,'zipcod':zipcod,'prof':prof,'service':serv})
def activation(request,email,un):
    signer = Signer()
    unf=signer.sign(email)
    if un == unf:
        return render(request,'activate.html')
    else:
        return redirect('index')

def upload(request):
    profiles=Profilecooperative.objects.filter(cooperativename=str(request.user))
    if profiles.exists():
        return redirect('inside')
    else:
        if request.method =='POST':
            img=request.FILES['image']
            profile.objects.create(image=img,cooperativename=str(request.user)).save()
            return redirect('inside')
        else:
            return render(request,'upload.html')       
def activate(request):
    if request.method=='POST':
        user=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=user,password=password)
        if user is not None:
            auth.login(request,user)
            if Active.objects.filter(user=request.user).exists():
                return redirect('inside')
            else:
                Active.objects.create(user=request.user,activate=True).save()
                return redirect('inside')
        else:
                messages.info(request,'incorect password')
                return redirect('activate')
    else:
        return render(request,'activate.html')

def Record(request):
    if str(request.user)=='AnonymousUser':
        return redirect('index')
    else:
        if Recorder.objects.filter(user=str(request.user)):
            return redirect('Recorder')
        else:
            prof=Profilecooperative.objects.filter(cooperativename=str(request.user))
            ty=Recorder.objects.filter(cooperativename=str(request.user))
            return render(request,'recorders.html',{'ty':ty,'prof':prof})        

def addRecorder(request):
    if str(request.user)=='AnonymousUser':
            return redirect('index')
    else:
        if Recorder.objects.filter(user=str(request.user)):
                return redirect('recorder')
        else:
            # zipcod=Zipcodes.objects.all()
            prof=Profilecooperative.objects.filter(cooperativename=str(request.user))
            if request.method=='POST':
                email=request.POST['username']
                name=request.POST['name']
                rand=random.randint(1111,99999)
                password=str(name)+str(rand)
                if User.objects.filter(username=email).exists():
                    messages.info(request,'Email have already used')
                    return redirect('adduser')
                else:
                    subject='Thank you for Using SmartIkigega '
                    message='Dear '+name +'\n'+'https://harvestendpoint.herokuapp.com/login/'+'\n'+'Username: '+email+'\n'+'Password: '+password+'\n'+'Thank you are now employed by'+str(request.user)
                    from_email=settings.EMAIL_HOST_USER
                    rt=send_mail(subject,message,from_email,[str(email),],fail_silently=True)
                    User.objects.create_user(name=name,username=email,password=password).save()
                    Recorder.objects.create(name=str(request.user),user=email).save()
                    mess='added sucessfully'
                    return render(request,'addRecorder.html',{'mess':mess})
            else:
                return render(request,'addRecorder.html',{prof:'prof'})
        

def Farmerreg(request):
    # ty=Recorder.objects.filter(user=str(request.user))
    # for tr in ty:
    #     gy=tr.cooperativename
    # prof=Profilecooperative.objects.filter(cooperativename=gy)
    # # zipcod=Zipcodes.objects.all()
    # lastcode=Farmers.objects.all().order_by('-pub_date')[:1]
    # lastcodes=lastcode.count()
    # inst=Recorder.objects.get(user=request.user)
    # cooperative=inst.cooperativename
    # for gt in lastcode:
    #     codf=gt.code
    def random_with_N_digits(n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
    nost = random_with_N_digits(6)
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        gender=request.POST['gender']
        harvesttype=request.POST['harvesttype']
        tel=request.POST['number']
        # tel=request.POST['number']
        telephone =tel[1:]
        now = datetime.datetime.now()
        village=request.POST['village']
        email=request.POST['email']
        district =request.POST['district']
        sector = request.POST['sector']
        cell = request.POST['cell']
        years=now.year
        newcode=str(years)+str(1)
        one=1
        print(telephone)
        lastnum=Farmers.objects.filter(number=telephone)
        nums=lastnum.count()
        print(nums)
        if nums <= 12:
            Farmers.objects.create(district=district,sector=sector,village=village,cell=cell,email=email,firstname=firstname,lastname=lastname,gender=gender,number=telephone,harvesttype=harvesttype,code= nost).save()
        
            mess='Hey '+firstname+'\n Your Code :'+str(nost)
            if email != None or tel !=None:
                subject='Thank you for Using smartikigega'
                message='Dear '+firstname +' '+lastname +'\n'+'your new SmartIkigega code is : '+str(nost)
                from_email=settings.EMAIL_HOST_USER
                rt=send_mail(subject,message,from_email,[str(email),],fail_silently=True)
                #account_sid = 'AC1b41153cd2a60b01893bb9740d2fd875'
                #auth_token = 'efa2a032ba78dff3111fce2efafa5940'
                #client =Client(account_sid, auth_token)
                #message = client.messages.create(body='your Code is: '+nost,from_='+16305280341',to='+250784447864')
                # sendsms = requests.post('http://rslr.connectbind.com:8080/bulksms/bulksms?username=1212-pathos&password=Chance@1&type=0&dlr=1&destination='+str(tel)+'&source=CityPlus&message='+str(mess)+'')
                # pass
            else:
                pass
            return render(request,'farmerreg.html',{'mess':mess})

        else:
            messages.info(request,'This number is  not full')
            return render(request,'farmerreg.html')

    else:

        return render(request,'farmerreg.html')

def dashboard(request):
    if request.user.is_superuser:
        cooperatives=User.objects.all()
        farmers=Farmers.objects.all()
        farmers=Farmers.count()
        Record=Harvestrecord.objects.all()
        Record=Record.count()
        recorder=recorder.objects.all()
        recorder=recorder.count()

        return render(request,'dashboard.html',{'cooparatives':cooperatives,'farmers':farmers,'Record':Record,'recorder':recorder})
    else:
        return redirect('index')