class RequestMixins:

    def get_restaurant_from_request(self):
        return self.request.user.contact_person_user.contact.restaurant

    def get_user(self):
        return self.request.user
