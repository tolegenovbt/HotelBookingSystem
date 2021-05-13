from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from auth_.views import CreateUserViewSet, ProfileApiViewSet

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('signup/', CreateUserViewSet.as_view({'post': 'post_user'})),
    path('profile/<int:pk>/', ProfileApiViewSet.as_view())
    # path('admin/', admin.site.urls),
    # path('api/', include('api.urls')),
    # path('auth_', include('auth_.urls'))
]
