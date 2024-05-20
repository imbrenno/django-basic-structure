from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.controller.person_ctrl import PersonCtrl

router = DefaultRouter()
router.register(r'panel/person', PersonCtrl)

urlpatterns = [
    path('', include(router.urls)),
]
