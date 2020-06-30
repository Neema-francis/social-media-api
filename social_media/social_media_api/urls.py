"""
    Defines urls for social media
"""

from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from social_media_api import views

schema_view = get_swagger_view(title='SOCIAL MEDIA API')
urlpatterns = [
    path('', schema_view),

    # Admin
    path('create-story-card/', views.StoryCardCreateAPIView.as_view(), name='create-story-card'),  
    path('story-card/', views.StoryCardAPIView.as_view(), name='story-card'),  
    path('story-card-status-count/<int:pk>/', views.StoryCardStatusCountAPIView.as_view(), name='story-card-status-count'), 

    # User
    path('list-story-card/', views.StoryCardListAPIView.as_view(), name='list-story-card'), 
    path('story-card-response/<int:pk>/', views.StoryCardResponseAPIView.as_view(), name='story-card-response'),  
     
]