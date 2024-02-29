from django.urls import path
from .views import LanguageListView, TranslateView, DetectLanguage

urlpatterns = [
    path('languages/', LanguageListView.as_view(), name='language-list'),
    path('translate/', TranslateView.as_view(), name='translate-text'),
    path('detect_lang/', DetectLanguage.as_view(), name='detect-language')
]

