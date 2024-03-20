"""
For test purpose only
"""


class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization

    def getUsername(self, request):
        header_token = request.META.get("HTTP_AUTHORIZATION", None)
        if header_token is not None:
            pass
            # try:
            # token = sub("Bearer ", "", header_token)
            # token_obj = AccessToken().decode(token)
            # except Token.DoesNotExist:
            #     pass
        return None  # token_obj.user.username

    def __call__(self, request):
        #  Code to be executed for each request before
        #  the view (and later middleware) are called

        if request.user.is_anonymous is False:
            # contact = ContactPerson.objects.get(Q(user=request.user.id))
            # print(contact)
            self.getUsername(request)
            request.restaurant = "I am testing"

        #  Code to be executed for each request/response after
        #  the view is called.
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        #  This can be used to Do something before passing it to the View
        #  Sometime like, Do various things with HOST or anything else of request object
        pass
