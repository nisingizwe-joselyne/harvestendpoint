from django.urls import path
from .import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static
                                                         
urlpatterns=[
    path('',views.welcome, name='harvest'),
    path('kiny',views.kiny, name='kiny'),
    path('cooperative',views.cooperative, name='cooperative'),
    path('work',views.work, name='work'),
    path('signin',views.signin, name='signin'),
    path('record',views.record, name='record'),
    path('pay',views.pay, name='pay'),
    # path('about-us',views.about, name='about'),
    # path('digital-ikigega',views.Ikigega, name='ikigega'),
    # path('farmercreate/',views.farmercreate, name='farmercreate'),
    path('loan/endpoints/',views.LoanRequest, name='loanendpoints'),
    path('insurance/endpoints/',views.InsuranceRequest, name='insurancendpoints'),
    path('payharvest/endpoints/',views.Harvestpay, name='payharvestpoints'),
    path('registration', views.registration, name='register'),
    path('harvestrecording', views.Harvestrecording, name='recording'),
    path('digitalapp/',views.digitalapp, name='digital'),
    path('dashboard/get_admin/staff',views.dashboard,name='dashboard'),
    # path('proove/get_admin/<int:pk>',views.prooving,name='proove'),
    path('farmerreg/',views.Farmerreg,name='farmerreg'),
    # path('<int:id>deleteInfos', views.delreg, name='deleteInfos'),
    # path('<int:id>updateInfos',views.updatereg, name='updateInfos'),
    # path('reg/endpoint', views.registerEndpoint, name='endpoint'),
    # path('deleteEndpoints/<int:id>', views.deleteEndpoint, name='deleteEndpoints'),
    # path('user-creation/', CustomAuthToken.as_view())
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)