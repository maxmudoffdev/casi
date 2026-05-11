from rest_framework import  serializers

from casi.journals.api.serializers import JournalSerialziers, VolumeSerialziers
from casi.submission.models import Submission
from casi.users.api.serializers import UserSerializer


class SubmissionSerializers(serializers.ModelSerializer):
    journal_id = serializers.CharField(write_only=True)
    volume_id = serializers.CharField(write_only=True)
    submitted_by_id = serializers.CharField(write_only=True)

    journal = JournalSerialziers(read_only=True)
    volume = VolumeSerialziers(read_only=True)
    submitted_by = UserSerializer(read_only=True)

    class Meta:
        model = Submission
        fields = (
            "id",
            "title",
            "abstract",
            "file",
            "keyword",
            "journal",
            "journal_id",
            "volume",
            "volume_id",
            "cover_letter",
            "status",
            "doi",
            "submitted_by",
            "submitted_by_id"
        )
