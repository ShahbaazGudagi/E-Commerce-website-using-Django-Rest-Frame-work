from .import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('product_categories',views.ProductCatergoryViews)
router.register('product',views.ProductView)
router.register('customer',views.CustomerView)
router.register('order',views.OrderView)
router.register('address',views.delivery_details)

urlpatterns = [
   
    path('',include(router.urls)),
    path('login/',views.LoginView.as_view()),
    path('cart/',views.CartView.as_view()),
    path('checkout/',views.CheckoutView.as_view()),
]

