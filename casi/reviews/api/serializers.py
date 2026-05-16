from rest_framework import  serializers

from casi.reviews.api.validators import validate_assignment
from casi.reviews.models import Review,ReviewAssigment
from casi.submission.api.serializers import SubmissionSerializers
from casi.users.api.serializers import UserSerializer


class ReviewSerailizers(serializers.ModelSerializer):
    submission_id = serializers.CharField(write_only=True)
    reviewer_id =  serializers.CharField(write_only=True)
    submission = SubmissionSerializers(read_only=True)
    reviewer = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = (
            "id",
            "submission",
            "submission_id",
            "reviewer",
            "reviewer_id",
            "comment",
            "recommendation",
            "file",
            "is_submitted"
        )

    def create(self, validated_data):
        submission_id = validated_data.get("submission_id")
        reviewer_id = validated_data.get("reviewer_id")

        existing = Review.objects.filter(
            submission_id=submission_id,
            reviewer_id=reviewer_id
        ).first()

        if existing:
            raise serializers.ValidationError(
                "You already have a review for this submission."
            )

        return super().create(validated_data)


class ReviewAssigmentSerializer(serializers.ModelSerializer):
    submission = SubmissionSerializers(read_only=True)
    submission_id = serializers.CharField(write_only=True)
    reviewer = UserSerializer(read_only=True)
    reviewer_id = serializers.CharField(write_only=True)
    asigment_by = UserSerializer(read_only=True)
    asigment_by_id = serializers.CharField(write_only=True)

    class Meta:
        model = ReviewAssigment
        fields = (
            "id",
            "submission",
            "submission_id",
            "reviewer",
            "reviewer_id",
            "asigment_by",
            "asigment_by_id",
            "deadline",

            )

        read_only_fields = ["id","created_at","status"]

    def validate(self, data):
        validate_assignment(
            data.get("submission_id"),
            data.get("reviewer_id"),
            data.get("asigment_by_id"),
        )
        return data




