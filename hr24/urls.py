"""hr24 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from rest_framework_nested.routers import NestedSimpleRouter

from quizapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tests', views.TestViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'answers', views.PossibleAnswerViewSet)

tests_router = NestedSimpleRouter(router, r'tests', lookup='test')
tests_router.register(r'tasks', views.NestedTaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(tests_router.urls)),
    url(r'^api-quiz/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', auth_views.obtain_auth_token)
]
