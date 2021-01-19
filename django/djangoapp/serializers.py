from rest_framework import serializers
from djangoapp import models

class StudSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = models.StudModel