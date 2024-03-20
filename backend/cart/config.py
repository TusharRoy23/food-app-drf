class CartStatus:
    SAVED = "saved"
    APPROVED = "approved"
    DELETED = "deleted"
    REJECTED = "rejected"

    CHOICES = (
        (SAVED, "saved"),
        (APPROVED, "approved"),
        (DELETED, "deleted"),
        (REJECTED, "rejected"),
    )
