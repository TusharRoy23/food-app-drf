class CurrentStatus:
    ACTIVE = "active"
    INACTIVE = "inactive"
    NOT_VERIFIED = "not-verified"
    VERIFIED = "verified"

    CHOICES = (
        (ACTIVE, "active"),
        (INACTIVE, "inactive"),
        (NOT_VERIFIED, "not-verified"),
        (VERIFIED, "verified"),
    )
