from rest_framework.renderers import JSONRenderer

"""
Ref: https://www.django-rest-framework.org/api-guide/renderers/#custom-renderers
"""


class APIJSONRenderer(JSONRenderer):
    base_mapper = {"message": ""}
    success_mapper = {"success": True, "meta": {}, **base_mapper}
    failure_mapper = {"success": False}

    def __error_mapper(self, errors):
        for key in errors:
            if isinstance(errors[key], list):
                tmp_error = []
                for error in errors[key]:
                    if (
                        isinstance(error, dict) and error
                    ):  # Check if error is a non-empty dictionary
                        self.__error_mapper(error)
                        tmp_error.append(error)
                    elif isinstance(error, str):
                        tmp_error.append(error)
                errors[key] = tmp_error
        return errors

    def set_error_response(self, data):
        errors = data.get("errors")
        message = data.get("message")

        if errors:
            self.__error_mapper(errors)  # Error mapper
            self.failure_mapper["error"] = errors
        else:
            self.failure_mapper["error"] = data

        # self.failure_mapper["error"] = errors  # Keep it as it is. Will check in the future

        self.base_mapper["message"] = message
        self.failure_mapper.update(**self.base_mapper)

    def get_proper_response(self, data):
        meta = dict()

        if isinstance(data, dict):  # Checking if the data is dict()
            if "meta" in data.keys():
                meta = data.pop("meta")

            if "errors" in data:
                self.set_error_response(data=data)
                return self.failure_mapper

            self.success_mapper.update(data=data, meta=meta)
            return self.success_mapper

        self.success_mapper.update(
            meta=meta, data={"results": data, "count": len(data) if data else 0}
        )
        return self.success_mapper

    def render(self, data, accepted_media_type=None, renderer_context=None):
        data = self.get_proper_response(data=data)
        return super().render(
            data=data,
            accepted_media_type=accepted_media_type,
            renderer_context=renderer_context,
        )
