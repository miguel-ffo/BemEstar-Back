from rest_framework import serializers
from .models import AnamnesisModel, WaterConsumeModel

class WaterConsumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WaterConsumeModel
        fields = ['date', 'water_goal', 'water_consumed']
        
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)



from rest_framework import serializers
from .models import AnamnesisModel

class AnamnesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnamnesisModel
        fields = ['weight', 'height', 'medical_conditions', 'medications', 'exercise_frequency', 'goals']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

