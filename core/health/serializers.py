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

from rest_framework import serializers
from .models import DailyRecordModel, GlycemiaModel, BloodPressureModel

class GlycemiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlycemiaModel
        fields = ['pre_workout', 'post_workout']

class BloodPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodPressureModel
        fields = ['pre_workout_systolic', 'pre_workout_diastolic', 'post_workout_systolic', 'post_workout_diastolic']

class DailyRecordSerializer(serializers.ModelSerializer):
    glycemia = GlycemiaSerializer()
    blood_pressure = BloodPressureSerializer()

    class Meta:
        model = DailyRecordModel
        fields = ['date', 'glycemia', 'blood_pressure']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return {
            "glycemia": {
                "date": response['date'],
                "pre_workout": response['glycemia']['pre_workout'],
                "post_workout": response['glycemia']['post_workout'],
            },
            "blood_pressure": {
                "date": response['date'],
                "pre_workout_systolic": response['blood_pressure']['pre_workout_systolic'],
                "pre_workout_diastolic": response['blood_pressure']['pre_workout_diastolic'],
                "post_workout_systolic": response['blood_pressure']['post_workout_systolic'],
                "post_workout_diastolic": response['blood_pressure']['post_workout_diastolic'],
            }
        }


class DailyRecordGetSerializer(serializers.Serializer):
    glycemia = GlycemiaSerializer()
    blood_pressure = BloodPressureSerializer()
    water_intake = WaterConsumeSerializer()