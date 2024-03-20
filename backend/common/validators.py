from django.core.exceptions import ValidationError


class BaseValidator(object):
    """This is the base validator which provides method validation"""

    def __init__(self, *args, **kwargs):
        self.obj = kwargs["obj"]

    def validate(self):
        pass


class ScreenMethodValidator(BaseValidator):
    """This will run when a method will start with 'screen_*' prefix"""

    def validate(self):
        screen_method = self.obj.get_screen_methods()
        for method in screen_method:
            result = method()
            if result:
                raise ValidationError(result)
