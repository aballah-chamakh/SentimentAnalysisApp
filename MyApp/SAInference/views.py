from django.shortcuts import render
from rest_framework import generics
from .serializers import SentimentAnalysisInferenceSerializer
from .models import SentimentAnalysisInference
from .permissions import IsAuthenticatedAndOwnerOrDeny

class SentimentAnalysisInferenceListApiView(generics.ListAPIView):
    queryset  = SentimentAnalysisInference.objects.all()
    serializer_class = SentimentAnalysisInferenceSerializer
    permission_class = IsAuthenticatedAndOwnerOrDeny

    def get_queryset(self):
      qs = SentimentAnalysisInference.objects.filter(user=self.request.user)
      return qs

class SentimentAnalysisInferenceCreateApiView(generics.CreateAPIView):
    queryset  = SentimentAnalysisInference.objects.all()
    serializer_class = SentimentAnalysisInferenceSerializer
    #permission_class = IsAuthenticatedAndOwnerOrDeny
    def perform_create(self,serializer):
        return serializer.save(user=self.request.user)

class SentimentAnalysisInferenceDetailApiView(generics.RetrieveAPIView):
    queryset  = SentimentAnalysisInference.objects.all()
    serializer_class = SentimentAnalysisInferenceSerializer
    permission_class = IsAuthenticatedAndOwnerOrDeny

class SentimentAnalysisInferenceUpdateApiView(generics.UpdateAPIView):
    queryset  = SentimentAnalysisInference.objects.all()
    serializer_class = SentimentAnalysisInferenceSerializer
    permission_class = IsAuthenticatedAndOwnerOrDeny

class SentimentAnalysisInferenceDeleteApiView(generics.DestroyAPIView):
    queryset  = SentimentAnalysisInference.objects.all()
    serializer_class = SentimentAnalysisInferenceSerializer
    permission_class = IsAuthenticatedAndOwnerOrDeny
