class ExcludeFieldsMixin:

    def __init__(self, *args, **kwargs):
        exclude = []
        fields = []
        if kwargs.get("exclude", None):
            exclude = kwargs.pop("exclude")
        if kwargs.get("fields", None):
            fields = kwargs.pop("fields")

        if fields and exclude:
            raise ValueError("exclude and fields cannot be used together")

        super().__init__(*args, **kwargs)

        if exclude:
            for field_name in exclude:
                self.fields.pop(field_name)

        """
        remove fields which are not in the fields (Class Meta:) from serializer
        """

        serializer_fields = self.fields.keys()
        exclude_fields = [field for field in serializer_fields if field not in fields]
        if fields:
            for field in exclude_fields:
                self.fields.pop(field)
