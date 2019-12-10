from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/',include('SAInference.urls')),
    path('api/token/', obtain_jwt_token, name='token_obtain_pair'),
    path('api/token/refresh', refresh_jwt_token, name='token_refresh'),

]
