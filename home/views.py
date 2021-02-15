from django.shortcuts import render
import africastalking
from .models import*
from .serializers import*
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


username = "nesjoselyne@gmail.com"
api_key = "7d5ec7e665579ee7ef1a3a71927f74123d0542960de776089cc89b28b4977804"

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.

def welcome(request):
    return render(request,'harvest.html') 

def cooperative(request):
    return render(request,'cooperative.html') 

def work(request):
    return render(request,'work.html')    

def signin(request):
    return render(request,'signin.html')      

    # ussd
@csrf_exempt
def digitalapp (request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        level = text.split('*')
        response = ''
        numb = text[:5]
        if text == '':
            response = 'CON murakaza neza kurubuga rwabahinzi Smart ikigega : \n'
            response += '1. umuceri \n'
            response += '2. amata \n'
            response += '3.ikawa \n'
            response += '4.ingano \n'
            response += '5.ibigori \n'
            response += '6.imbuto'
            #  harvesting session
        elif text == '1':
            response = 'CON murakaza neza muhinzi wumuceri hitamo ibijyanye na '+str(len(level))+'\n'
            response += '1. Umusaruro wanjye \n'
            response += '2. serivisi zubukungu\n'
            response += '3. ubwishingizi kumusaruro'
            # current harvesting session
        elif text == '1*1':
            response = 'CON  kureba umusaruro wanjye : \n'
            response += '1.umusaruro mbumbe wose \n'
            response += '2.ingano yumusaruro muri uku kwezi \n'
        elif text == '1*1*1':
            response = 'CON injizamo code yumuhinzi  \n'
            insert=Harvestrecord(farmercode=str(level[3]))
            insert.save() 
            y = input
            y =request.POST['farmercode']
            v=Harvestrecord.objects.filter(farmercode=y)
            for rt in v:
                qty = rt.Quantity
        elif numb == '1*1*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON umusaruro mbumbe wawe ni' + qty + ' \n'
        elif text == '1*1*2':
            response = 'CON injizamo code yumuhinzi \n'
        elif numb == '1*1*2'and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON ingano yumusaruro muri uku kwezi ni 140kg \n'
        #  financial session
        elif text == '1*2':
            response = 'CON murakaza neza  \n'
            response += '1. kwishyura umusaruro \n'
            response += '2. inguzanyo \n'
            response += '3. uko nabona inguzanyo'
            # direct loan session
        elif text == '1*2*1':
            response = 'CON injizamo code yumuhinzi ugiye kwishyura '+str(len(level))+' \n'
        elif numb == '1*2*1' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON shyiramo amafaranga ugiye kwishyura : \n'
        elif numb == '1*2*1' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON washyizemo' + str(level[4])  + 'ugiye kwishyura '+str(level[3])+  'kuri shyiramo umubare wibanga wemeze: \n'
        elif numb == '1*2*1' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON  kwishyura amafaranga byagenze neza  murakoze: \n'
        elif text == '1*2*2':
            response = 'CON Enter farmers code '+str(len(level))+' \n'
        elif numb == '1*2*2' and int(len(level))==4 and str(level[3]) in str(level):
            response = 'CON Enter the money you want pay: \n'   
        elif numb == '1*2*2' and int(len(level))==5 and str(level[4]) in str(level):
            response = 'CON Enter mobile-money pin to pay: \n'   
        elif numb == '1*2*2' and int(len(level))==6 and str(level[5]) in str(level):
            response = 'CON you have succesfully paid the loan thanks: \n'   
        elif text == '1*3':
            response = 'CON Other services: \n'
            response += '1.how to get crops insurance\n'
            response += '2.join crops insurance \n'
        elif text == '1*3*1':
            response = 'END how to get crops insurance: \n'
            response += 'in order to get crops insurance you have to be an active member of any registrated cooperative in our system \n'
        elif text == '1*3*2':
            response = 'END  enter the farmers code to get the insurance:'

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




