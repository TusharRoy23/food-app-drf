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


class MealState:
    HOT = "hot"
    COLD = "cold"
    NORMAL = "normal"

    CHOICES = (
        (HOT, "hot"),
        (COLD, "cold"),
        (NORMAL, "normal"),
    )


class MealFlavor:
    SWEET = "sweet"
    SPICY = "spicy"
    SALTY = "salty"
    SOUR = "sour"
    BITTER = "bitter"
    SAVORY = "savory"

    CHOICES = (
        (SWEET, "sweet"),
        (SPICY, "spicy"),
        (SALTY, "salty"),
        (SOUR, "sour"),
        (BITTER, "bitter"),
        (SAVORY, "savory"),
    )


class MealType:
    DAILYFOOD = "daily food"
    FASTFOOD = "fast food"
    SNACKS = "snacks"
    BURGERS = "burgers"
    MEAT = "meat"
    FISH = "fish"
    BEVERAGE = "beverage"
    DESSERT = "dessert"
    KEBAB = "kebab"
    ALCOHOL = "alcohol"

    CHOICES = (
        (DAILYFOOD, "daily food"),
        (FASTFOOD, "fast food"),
        (SNACKS, "snacks"),
        (BURGERS, "burgers"),
        (MEAT, "meat"),
        (FISH, "fish"),
        (BEVERAGE, "beverage"),
        (DESSERT, "dessert"),
        (KEBAB, "kebab"),
        (ALCOHOL, "alcohol"),
    )
