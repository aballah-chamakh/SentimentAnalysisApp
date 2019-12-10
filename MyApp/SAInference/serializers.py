from rest_framework import serializers
from .models import SentimentAnalysisInference
from  nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentAnalysisInferenceSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)
    result = serializers.CharField(read_only=True)
    class Meta :
        model = SentimentAnalysisInference
        fields = ('username','text','result')

    def create(self,validated_data):
        text = validated_data.get('text')
        print(validated_data)
        sai_inference_obj = SentimentAnalysisInference.objects.create(**validated_data)
        sid = SentimentIntensityAnalyzer()
        compound = float(sid.polarity_scores(str(sai_inference_obj.text))['compound'])
        if compound > 0.5 :
            sai_inference_obj.result = 'Happy'
        elif compound < 0.5 :
            sai_inference_obj.result = 'Sad'
        else:
            sai_inference_obj.result = 'Neutral'
        sai_inference_obj.save()
        return sai_inference_obj
