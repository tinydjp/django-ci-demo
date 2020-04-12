from datetime import datetime
from rest_framework import serializers

from .models import Company, Product


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['id', 'established_at']

    def save(self, **kwargs):
        data = self.validated_data
        data['established_at'] = datetime.now().timestamp()
        return super().save()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id', ]
