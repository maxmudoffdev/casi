from rest_framework import serializers

from casi.journals.models import Journal
from django.utils.text import slugify

class JournalSerialziers(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    def get_logo_url(self, obj):
        if obj.logo:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.logo.url)
            return obj.logo.url
        return None

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    class Meta:
        model = Journal
        fields = ("id","name","description","image","logo","issn","logo_url","image_url")
        read_only_fields = ["id","is_active"]




