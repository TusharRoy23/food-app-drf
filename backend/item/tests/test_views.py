from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from backend.item.serializer import ItemOutputSerializer
from backend.item.views import ItemListAPIView, ItemRetrieveAPIView


class TestItemListAPIView:
    def test_items_list_apiview(self, request_factory, force_auth, item_list, item):
        view = ItemListAPIView.as_view()
        url = reverse("Item:item-list")
        data = {"count": 10, "next": [], "previous": [], "results": item_list}
        request = request_factory.get(url, data=data, format="json")
        force_auth(request)

        response = view(request)
        assert response.status_code == 200


class TestItemRetrieveAPIView:
    serializer_class = ItemOutputSerializer

    def test_items_retrieve_apiview(self, request_factory, force_auth, item):
        view = ItemRetrieveAPIView.as_view()
        url = reverse("Item:item-details", kwargs={"uuid": str(item.uuid)})

        serializer = self.serializer_class(item)
        request = request_factory.get(url, data=serializer.data, format="json")
        force_auth(request)
        response = view(request, uuid=item.uuid)
        assert response.status_code == 200
