
from . import views

from django.urls import path
from .views import ParagraphListCreateAPIView, ParagraphDetailAPIView
from django.contrib import admin


urlpatterns = [
    path('paragraphs/', ParagraphListCreateAPIView.as_view(), name='paragraph-list-create'),
    path('paragraphs/<int:pk>/', ParagraphDetailAPIView.as_view(), name='paragraph-detail'),
    path('admin/', admin.site.urls),
    path('api/', include('text_analysis.urls'))
]
