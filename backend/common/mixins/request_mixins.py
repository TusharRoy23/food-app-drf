class RequestMixins:

    def get_store_from_request(self):
        return self.request.user.contact_person_user.contact.store

    def get_user(self):
        return self.request.user
