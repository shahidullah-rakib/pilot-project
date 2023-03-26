
from django.contrib import admin
from rest_framework import routers
from course.views import CourseViewSet, StudentViewSet, AdminViewSet, UserViewSet
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'users', UserViewSet)
# router2 = routers.DefaultRouter()
# router2.register(r'adminx', AdminViewSet)

urlpatterns = [
    path('adminx/', admin.site.urls),
    path('', include(router.urls)),
    # path('2/', include(router2.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
