from rest_framework import routers
from . import views

app_name = "test"

router = routers.SimpleRouter()
router.register(
    r"auto",
    views.AutoTestModelViewset,
    basename="auto"
)
router.register(
    r"explicit",
    views.ExplicitTestModelViewset,
    basename="explicit"
)

urlpatterns = router.urls
