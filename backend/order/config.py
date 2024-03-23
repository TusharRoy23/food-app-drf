class OrderStatus:
    PENDING = "pending"
    RELEASED = "released"
    ON_SHIPPING = "on shipping"
    PAID = "paid"
    CANCELLED = "cancelled"
    IN_PROGRESS = "in progress"

    CHOICES = (
        (PENDING, "pending"),
        (RELEASED, "released"),
        (ON_SHIPPING, "on shipping"),
        (PAID, "paid"),
        (CANCELLED, "cancelled"),
        (IN_PROGRESS, "in progress"),
    )


class PaidBy:
    CASH_ON_DELIVERY = "cash on delivery"
    CARD = "card"
    PAID_VIA_MOBILE = "paid via mobile"

    CHOICES = (
        (CASH_ON_DELIVERY, "cash on delivery"),
        (CARD, "card"),
        (PAID_VIA_MOBILE, "paid via mobile"),
    )
