from rest_framework import  serializers

from casi.authors.api.serializers import AuthorSerializersPrivate
from casi.journals.api.serializers import JournalSerialziers, VolumeSerialziers
from casi.submission.models import Submission
from casi.users.api.serializers import UserSerializer


class SubmissionSerializers(serializers.ModelSerializer):
    journal_id = serializers.CharField(write_only=True)
    journal = JournalSerialziers(read_only=True)
    submitted_by = UserSerializer(read_only=True)
    user_id = serializers.CharField(write_only=True)
    author = AuthorSerializersPrivate(read_only=True,many=True)
    author_id = serializers.ListField(
        child=serializers.UUIDField(),
        write_only=True,
        required=False
    )

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
            "cover_letter",
            "status",
            "doi",
            "author",
            "author_id",
            "submitted_by",
            "user_id"
        )

    def create(self, validated_data):
        author_id = validated_data.pop("author_id", [])
        submission = Submission.objects.create(**validated_data)
        if author_id:
            submission.author.set(author_id)
        return submission
