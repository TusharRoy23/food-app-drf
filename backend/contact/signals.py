from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ContactPerson


def assign_django_groups(user, group_list):
    if len(group_list):
        group_id_list = list(set(group_list))  # Do Unique
        groups = Group.objects.filter(id__in=group_id_list)
        for group in groups:
            user.groups.add(group)

        # remove non-relevant groups
        exclude_groups = user.groups.all().exclude(
            id__in=group_id_list
        )  # Get ID's except group_id_list
        for group in exclude_groups:
            user.groups.remove(group)


@receiver(post_save, sender=ContactPerson)
def on_contact_person_save(sender, instance, created, **kwargs):
    assign_django_groups(
        instance.user,
        list(instance.contact.contact_group.django_groups.values_list("id", flat=True)),
    )
