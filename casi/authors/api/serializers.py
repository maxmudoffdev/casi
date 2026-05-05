from rest_framework import serializers
from django.core.validators import validate_email
from casi.authors.models import Author
from django.core.exceptions import ValidationError as DjangoValidationError
import  re

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id","first_name","last_name","affiliation","email","orc_id"]

    def validate(self, attrs):
        first_name = attrs.get("first_name")
        if first_name is None or len(first_name) < 4:
            raise serializers.ValidationError("First name is not None and First name character must much 4")
        attrs['first_name'] = first_name.strip().capitalize()
        last_name = attrs.get("last_name")
        if last_name is None or len(last_name) < 4:
            raise serializers.ValidationError("Last name is not None and Last name character must much 4")
        attrs['last_name'] = last_name.strip().capitalize()
        email = attrs.get("email")
        if email:
            email = email.lower().strip()
            try:
                validate_email(email)
            except DjangoValidationError:
                raise serializers.ValidationError("Enter a valid email address.")
            if Author.objects.filter(email=email).exists():
                raise serializers.ValidationError("This email is already in use.")
            attrs['email'] = email
        affiliation = attrs.get("affiliation")
        if affiliation:
            affiliation = affiliation.capitalize()
            if len(affiliation) < 4:
                raise serializers.ValidationError("Affiliation must be at least 4 characters.")
            attrs['affiliation'] = affiliation.strip().capitalize()

        orc_id = attrs.get("orc_id")
        if orc_id:
            orc_id = orc_id.strip()
            pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
            if not re.match(pattern, orc_id):
                raise serializers.ValidationError("Invalid ORCID format. Expected: 0000-0000-0000-0000")
            if Author.objects.filter(orc_id=orc_id).exists():
                raise serializers.ValidationError("This ORCID is already in use.")
            attrs['orcid'] = orc_id

        return attrs


