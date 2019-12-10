from django.urls import path
from .views import (
                   SentimentAnalysisInferenceListApiView,
                   SentimentAnalysisInferenceCreateApiView,
                   SentimentAnalysisInferenceUpdateApiView,
                   SentimentAnalysisInferenceDetailApiView,
                   SentimentAnalysisInferenceDeleteApiView,
                   )

urlpatterns = [

    path('sa_inferences', SentimentAnalysisInferenceListApiView.as_view()),
    path('make_sa_inference', SentimentAnalysisInferenceCreateApiView.as_view()),
    path('sa_inference/<int:pk>', SentimentAnalysisInferenceCreateApiView.as_view()),
    path('sa_inference/<int:pk>/update', SentimentAnalysisInferenceCreateApiView.as_view()),
    path('sa_inference/<int:pk>/delete', SentimentAnalysisInferenceCreateApiView.as_view()),

]
