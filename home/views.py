from django.shortcuts import render
import africastalking
from .models import*
from .serializers import*
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


username = "nesjoselyne@gmail.com"
api_key = "7d5ec7e665579ee7ef1a3a71927f74123d0542960de776089cc89b28b4977804"
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def welcome(request):
    return render(request,'harvest.html') 

def cooperative(request):
    return render(request,'cooperative.html') 

def work(request):
    return render(request,'work.html')    

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
        num = text[:6]

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
            res = 'CON shyiramo code yumuhinzi '+str(len(level))+' \n' 
            if res==1:
                res="hello"
            else:
                res="not"
        elif num == '1*1' and int(len(level))==2 and str(level[1]) in str(level):
            response = 'CON shyiramo ingano yumusaruro mu biro cg litiro \n'
        elif num == '1*1' and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON shyiramo amafaranga ugiye kwishyura \n' 
        elif num == '1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON  wahisemo kwishyura'+ str(level[4]) + 'ugiye kwishyura kuri' + str(level[2]) +'shyiramo umubare wibanga wemeze kwishyura  \n'
        elif text == '1*2':
            response = 'CON nimero ya mobile : '+str(len(level))+ '\n'        
            # insert=Harvestrecord(farmercode=str(level[1]))
            # insert.save()
        elif num == '1*2' and int(len(level))==2 and str(level[3]) in str(level):
            response = 'CON umubare wamafaranga  \n'
        elif num == '1*2' and int(len(level))==3 and str(level[4]) in str(level):
            response = 'CON wahisemo kwishyura'+ str(level[4]) + 'ugiye kwishyura kuri' + str(level[2]) +'shyiramo umubare wibanga wemeze kwishyura  \n'   
            # insert=Harvestrecord(Quantity=str(level[2]))
            # insert.save()
        
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
            response = 'CON umusaruro wawe wukukwezi ni 360kg'+str(level[3])+'\n'
        elif text =='2*1*2':
            response = 'CON umusaruro mbumbe wawe ni 3600kg'+str(level[3])+'\n'
        elif text == '2*2':
            response = 'CON  ubwishingizi bw \n'
            response += '1.umwaka umwe \n'
            response += '2.imyaka itanu  \n'
            response += '3.imyaka icumi '   
        elif text == '2*2*1':
            response = 'CON  shyiramo code yawe ubashe kwinjira mubwishingizi bwumwaka umwe:' +str(len(level))+ '\n'
        elif num == '2*2*1'and int(len(level))==4 and str(level[3]) in str(level):   
            insert=Insurance(farmercode=str(level[2])) 
            if insert.is_valid():
                response = 'CON kwiyandikisha gusaba ubwishingizi bwumwaka byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n'
                insert.save()     

        elif text == '2*2*2':
            response = 'CON  shyiramo code yawe ubashe kwinjira mubwishingizi bwimyaka itanu :' +str(len(level))+ '\n'
        elif num == '2*2*2'and int(len(level))==4 and str(level[3]) in str(level):   
            insert=Insurance(farmercode=str(level[2])) 
            if insert.is_valid():
                response = 'CON kwiyandikisha gusaba ubwishingizi bwimyaka 5 byagenze neza murahabwa igisubizo mu masaha macye'+str(len(level))+'\n'
                insert.save()                        
            # response = 'CON code mwashyizemo ntibaho : \n'
        elif text == '3':
            response = 'CON  hitamo kwiyandikisha  nk \n'
            response += '1. itsinda(cooparative)\n'
            response += '2.umuhinzi ku giti cye '
        elif text == '3*1':
            response = 'CON  shyiramo izina rya cooperative :' +str(len(level))+ '\n'
            # insert= Cooperativesreg(name=str(level[2]))
            # insert.save 
        elif num == '3*1'and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON  shyiramo izina ryumuyobozi wa cooperative' +str(len(level))+ '\n'
            # insert= Cooperativesreg(leadername=str(level[3]))
            # insert.save   

        elif num == '3*1'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON  shyiramo numero zumuyobozi wa cooperative :' +str(len(level))+ '\n'
            # insert= Cooperativesreg(leaderphone=str(level[4]))
            # insert.save   
        elif num == '3*1'and int(len(level))==5 and str(level[4]) in str(level):  
            response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega nkitsinda bwakiriwe urahabwa igisubizo mu gihe gito' +str(len(level))+ '\n'  
        elif text == '3*2':
            response = 'CON  shyiramo izina rya mbere :' +str(len(level))+ '\n'
            # insert= Regfarmer(firstname=str(level[2]))
            # insert.save
        elif num == '3*2'and int(len(level))==3 and str(level[2]) in str(level):
            response = 'CON  shyiramo izina rya kabiri \n'
            insert= Regfarmer(lastname=str(level[3]))
            insert.save
        elif num == '3*2' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON  shyiramo numero yawe ya telephone \n'
            insert= Regfarmer(telephone=str(level[4]))    
            insert.save

        elif num == '3*2' and int(len(level))==4 and str(level[5]) in str(level):  
            response = 'CON  ubusabe bwawe bwo kwiyandikisha mukigega bwakiriwe urahabwa igisubizo mu gihe gito \n'
        elif text == '4':
            response = 'CON  shyiramo code yawe ubashe kubarura \n'
        elif num == '4' and int(len(level))==2 and str(level[1]) in str(level):  
            response = 'CON  shyiramo izina rya cooperative \n'  
        elif num == '4' and int(len(level))==3 and str(level[2]) in str(level):  
            response = 'CON  shyiramo code yumuhinzi \n'  
        elif num == '4' and int(len(level))==4 and str(level[3]) in str(level):  
            response = 'CON  shyiramo ibiro yagize \n'         
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

@csrf_exempt
def farmercreate(request):
    if request.method=='GET':
        reg=Regfarmer.objects.all()
        serializer=farmerSerializer(reg,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=farmerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'data submited successful'},status=201)
        return JsonResponse(serializer.errors,status=400)
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

def registration(request):
    select = Cooperativesreg.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        Cooperativedistrict = request.POST['Cooperativedistrict']
        leaderphone = request.POST['leaderphone']
        harvesttype = request.POST['harvesttype']
        leadername = request.POST['leadername']
        Cooperativesector = request.POST['Cooperativesector']
        insert = Cooperativesreg(name=name,Cooperativedistrict=Cooperativedistrict,leaderphone=leaderphone, harvesttype= harvesttype,leadername=leadername,Cooperativesector=Cooperativesector)
        try:
            insert.save()
            return render(request,'cooperative.html',{'message':'your request has been succeeful submitted we will  get in touch with u soon','data':select})
        except :
            return render(request,'cooperative.html',{'message':'failed to insert','data':select})
    return render(request,'cooperative.html',{'data':select})

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

