from rest_framework import serializers

from casi.journals.models import Journal, Volume,JournalRequirements


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


class VolumeSerialziers(serializers.ModelSerializer):
    journal = JournalSerialziers(read_only=True)
    journal_id = serializers.UUIDField(write_only=False)

    class Meta:
        model = Volume
        fields = [
            "id",
            "journal",
            "journal_id",
            "number",
            "issue",
            "year",
            "published_date",
            "is_published"
        ]
        read_only_fields = ["id", "journal"]

class JournalRequirementsSerilizers(serializers.ModelSerializer):
    journal = JournalSerialziers(read_only=True)
    journal_id = serializers.UUIDField(write_only=False)
    class Meta:
        model = JournalRequirements
        fields = [
            "id",
            "journal",
            "journal_id",
            "content"
        ]

        read_only_fields = ["id", "journal"]





