from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views as quickstart_views
from api import views as api_views

router = routers.DefaultRouter()
router.register(r'users', quickstart_views.UserViewSet)
router.register(r'groups', quickstart_views.GroupViewSet)
router.register(r'api', api_views.RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]