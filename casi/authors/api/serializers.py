from rest_framework import serializers

from casi.authors.api.mixins import AuthorValidationMixin
from casi.authors.models import Author

class AuthorSerializersPrivate(AuthorValidationMixin,serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id",
                  "first_name",
                  "last_name",
                  "affiliation",
                  "email",
                  "orc_id"
                  ]
        read_only_fields = ["created_at"]



# Hammaga ko'rinadigan (public)
class AuthorPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "first_name",
            "last_name",
            "affiliation",
            "orc_id",
        ]
        read_only_fields = ["created_at"]



