import pytest
from django.core.exceptions import ValidationError
from casi.authors.models import Author


@pytest.mark.django_db
class TestAuthorModel:
    def test_create_author(self):
        author = Author.objects.create(
            first_name="John",
            last_name="Smith",
            affiliation="MIT",
            email="john@mit.edu",
        )
        assert author.id is not None
        assert author.is_active is True

    def test_str(self):
        author = Author(first_name="John",last_name="Smith")
        assert str(author) == "John Smith"

    def test_invalid_first_name_xss(self):
        author = Author(
            first_name="<script>",
            last_name="Smith",
            affiliation="MIT",
            email="john@mit.edu",
        )
        with pytest.raises(ValidationError) as err:
            author.full_clean()
        assert err.value.message_dict["first_name"]


    def test_first_name_number(self):
        author = Author(
            first_name="John123",
            last_name="Smith",
            affiliation="MIT",
            email="john@mit.edu",
        )
        with pytest.raises(ValidationError):
            author.full_clean()



    def test_invalid_orcid(self):
        author = Author(
            first_name="John",
            last_name="Smith",
            affiliation="MIT",
            email="john@mit.edu",
            orc_id="1234-45454-sadasd"
        )

        with pytest.raises(ValidationError) as err:
            author.full_clean()
        assert "orc_id" in err.value.message_dict


    def test_invalid_orcid_checksum(self):
        author = Author(
                first_name="John",
                last_name="Smith",
                affiliation="MIT",
                email="john@mit.edu",
                orc_id="1234-45454-sadasd"
        )

        with pytest.raises(ValidationError) as err:
            author.full_clean()

        assert "invalid_orcid_checksum"


    def test_valid_orcid(self):
        author = Author(
            first_name="John",
            last_name="Smith",
            affiliation="MIT",
            email="john@mit.edu",
            orc_id="0000-0002-1825-0097"
        )
        author.full_clean()

    def test_manager_only_active_user(self):
        Author.objects.create(
            first_name="John",
            last_name="Smith",
            affiliation="MIT",
            email="john@mit.edu",
            is_active=True
        )
        Author.objects.create(
            first_name="John",
            last_name="Smith",
            affiliation="MIT",
            email="john1@mit.edu",
            is_active=False
        )

        assert Author.objects.count() == 1









