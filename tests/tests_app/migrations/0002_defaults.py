from django.db import migrations
import random
import string
from ..models import TestModel


def create_default_items(*args, **kwargs):
    for _ in range(5):
        TestModel.objects.create(
            title="".join(random.choices(string.ascii_letters, k=16))
        )


class Migration(migrations.Migration):
    dependencies = [
        ('tests_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_items),
    ]
