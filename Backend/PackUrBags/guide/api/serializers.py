from rest_framework import serializers
from guide.models import GuideData


class GuideDataSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)

    class Meta:
        model = GuideData
        fields = ['guide_id', 'email', 'first_name', 'last_name', 'username', 'phone_number', 'place', ]

    def validate(self, attrs):
        return attrs


class SearchGuideSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    city = serializers.CharField(max_length=100)

    class Meta:
        fields = ['start_date', 'end_date', 'city']
