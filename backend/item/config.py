class ItemStatus:
    ACTIVE = "active"
    INACTIVE = "inactive"
    OBSOLETE = "obsolete"
    WAITING = "waiting"
    DELETED = "deleted"

    CHOICES = (
        (ACTIVE, "active"),
        (INACTIVE, "inactive"),
        (OBSOLETE, "obsolete"),
        (WAITING, "waiting"),
        (DELETED, "deleted"),
    )


class ItemType:
    FOOD = "food"
    DRINK = "drink"
    ALCOHOL = "alcohol"
    VICTUALS = "victuals"

    CHOICES = (
        (FOOD, "food"),
        (DRINK, "drink"),
        (ALCOHOL, "alcohol"),
        (VICTUALS, "victuals"),
    )


class ItemState:
    HOT = "hot"
    COLD = "cold"
    NORMAL = "normal"
    FROZEN = "frozen"
    LIQUID = "liquid"

    CHOICES = (
        (HOT, "hot"),
        (COLD, "cold"),
        (NORMAL, "normal"),
        (FROZEN, "frozen"),
        (LIQUID, "liquid"),
    )


class ItemFlavor:
    SWEET = "sweet"
    SPICY = "spicy"
    SALTY = "salty"
    SOUR = "sour"
    BITTER = "bitter"
    SAVORY = "savory"
    GROOVE= "groove"
    NONE = "none"

    CHOICES = (
        (SWEET, "sweet"),
        (SPICY, "spicy"),
        (SALTY, "salty"),
        (SOUR, "sour"),
        (BITTER, "bitter"),
        (SAVORY, "savory"),
        (GROOVE, "groove"),
        (NONE, "none"),
    )
