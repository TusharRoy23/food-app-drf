from rest_framework import serializers


class LogSerializer(serializers.Serializer):
    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()

    def get_created_by(self, instance):
        return (
            f"{instance.created_by.first_name} {instance.created_by.last_name}"
            if instance.created_by
            else None
        )

    def get_updated_by(self, instance):
        return (
            f"{instance.updated_by.first_name} {instance.updated_by.last_name}"
            if instance.updated_by
            else None
        )


class BaseSerializer(serializers.ModelSerializer, LogSerializer):
    pass
