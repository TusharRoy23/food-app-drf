from django.core.exceptions import ObjectDoesNotExist
from django.db.models.fields.related import ForeignKey

from backend.common.mixins import InputMixins


class BaseModelService:
    model = None
    input_mixin = InputMixins

    def __init__(self, user=None, *args, **kwargs):
        """
        Initiating itself. (Not necessary)
        """
        super().__init__(*args, **kwargs)
        self.user = user

    def get_app_label(self):
        """
        To check the permission in app label
        """
        if self.model:
            return self.model._meta.app_label
        return None

    def user_has_permission(self, user, permission_code):
        """
        To check if the user has the permission on app_label
        ref:
        https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#django.contrib.auth.models.PermissionsMixin.has_perm
        """
        return user.has_perm(self.get_app_label() + "." + permission_code)

    def __get_model_fields_names(self, model):
        """
        Get the name of model fields
        """
        model_field_set = set()
        if model:
            for field in model._meta.get_fields():
                if isinstance(field, ForeignKey):
                    db_field_name = field.name + "_id"
                    keys = [field.name, db_field_name]
                else:
                    keys = [field.name]
                # keys = If it is FK field in the model then combine with _id otherwise only the field name
                model_field_set.update(keys)
        return model_field_set

    def __map_model_fields_and_data(self, model, defaults):
        """
        Mapping only those fields whose are available in model.
        """
        model_fields_names = self.__get_model_fields_names(model)
        filtered_fields = {
            key: value for key, value in defaults.items() if key in model_fields_names
        }
        return filtered_fields

    def create_model_instance(self, model, **field_value):
        """
        Create an instance of a given model as params
        """
        prefix_code = field_value.get("code", "")  # To generate unique code for entity
        if prefix_code:
            field_value["code"] = self.input_mixin.generate_unique_code(prefix_code)

        filtered_fields = self.__map_model_fields_and_data(model(), field_value)
        # instance = model(**filtered_fields)
        # instance.save()
        if self.user:
            filtered_fields["created_by"] = self.user
        instance = model.objects.create(**filtered_fields)

        return instance

    def create(self, *args, **kwargs):
        """
        Create an instance of a model which is defined in service class.
        self.model value of service class
        """
        assert self.model is not None, (
            "'%s' should either include a `model` attribute, "
            "or override the `create()` method." % self.__class__.__name__
        )  # It will raise an assertion error if self.model is None
        return self.create_model_instance(self.model, **kwargs)

    def update_model_instance(self, instance, **field_value):
        """
        Update a model instance.
        """
        model = instance.__class__
        filtered_fields = self.__map_model_fields_and_data(model, field_value)
        if self.user:
            filtered_fields["updated_by"] = self.user

        for key, value in filtered_fields.items():
            # setattr(Class-instance, attribute, value) used because it is an instance of a class
            setattr(instance, key, value)
        instance.save()
        return instance

    def __get_query_params(self, query_params):
        """
        Parse the query params and filter against the model fields.

        :param query_params: Query parameter dictionary
        """
        model_field_names = self.__get_model_fields_names(self.model)
        and_query_params = {}
        for key, val in query_params.items():
            if key.split("__")[0] in model_field_names:
                if key.endswith("__in"):
                    val = val.split(",")
                and_query_params.update({key: val})
        return and_query_params

    def __get_queryset(self, **query_params):
        """
        Return the Queryset for the model which defined in service.
        If there is no query_params then it will return all the objects of that model.
        However, filtered data will return

        :param query_params: Query params by which queryset will be filtered.
        :return: Filtered queryset.
        """

        assert self.model is not None, (
            "'%s' should either include a `model` attribute, "
            "or override the `read_id_pk()` method." % self.__class__.__name__
        )
        queryset = self.model.objects.all()

        and_query_params = self.__get_query_params(query_params=query_params)
        if and_query_params:
            queryset = queryset.filter(**and_query_params)

        return queryset

    def read_by_uuid(self, uuid, **kwargs):
        """
        Read object by UUID
        :return: model instance
        """
        try:
            return self.__get_queryset(**kwargs).get(uuid=uuid)
        except self.model.DoesNotExist:
            raise ObjectDoesNotExist

    def list(self, **query_params):
        assert self.model is not None, (
            "'%s' should either include a `model` attribute, "
            "or override the `list()` method." % self.__class__.__name__
        )
        queryset = self.__get_queryset()
        and_query_params = self.__get_query_params(query_params=query_params)
        if and_query_params:
            queryset = queryset.filter(**and_query_params)

        return queryset
