from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('recipe-list', views.recipeList, name='recipe-list'),
    path('recipe-detail/<str:pk>/', views.recipeDetail, name='recipe-detail'),
    path('recipe-create', views.recipeCreate, name='recipe-create'),
    path('recipe-update/<str:pk>/', views.recipeUpdate, name='recipe-update'),
]