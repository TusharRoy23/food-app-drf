from django.contrib.auth import get_user_model

User = get_user_model()


def test_create_visitor_user(create_user):
    user = create_user(email="nomrota@gm.com", username="nomrota")
    assert isinstance(user, User)
    assert user.is_visitor == True


# def test_create_restaurant_user(create_user):
#     user = create_user(email="tushar@gm.com", username='tushar' , is_visitor=False)
#     assert isinstance(user, User)
#     assert user.is_visitor == False
