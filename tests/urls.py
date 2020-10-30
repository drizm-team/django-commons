from django.urls import path, include

urlpatterns = [
    path(
        "items/",
        include(
            "tests.tests_app.urls",
            namespace="tests_app"
        ),
    )
]
