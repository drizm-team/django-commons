from rest_framework import routers
from . import views

app_name = "tests_app"

router = routers.SimpleRouter()
router.register(
    r"model",
    views.TestingModelViewset,
    basename="model_viewset"
)
router.register(
    r"one",
    views.OneToOneModelViewset,
    basename="one_viewset"
)

urlpatterns = router.urls
