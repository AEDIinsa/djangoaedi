from django.db import models
from django.contrib.auth.models import User

class TaigaAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
                ("create_taiga", "Can create a new Taiga account."),
        )


