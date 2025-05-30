from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView,
    ProductViewSet,
    CategoryViewSet,
    CartViewSet,
    WishlistViewSet,
    OrderView,
    PayOrderView,
    sales_summary,
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

cart_list = CartViewSet.as_view({'get': 'list', 'post': 'create'})
cart_delete = CartViewSet.as_view({'delete': 'destroy'})

wishlist_list = WishlistViewSet.as_view({'get': 'list', 'post': 'create'})

urlpatterns = [
    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User registration
    path('api/register/', RegisterView.as_view(), name='register'),

    # Cart endpoints
    path('api/cart/', cart_list, name='cart'),
    path('api/cart/item/<int:pk>/', cart_delete, name='cart-item-delete'),

    # Wishlist endpoints
    path('api/wishlist/', wishlist_list, name='wishlist'),

    # Order endpoints
    path('api/orders/', OrderView.as_view(), name='orders'),
    path('api/orders/<int:order_id>/pay/', PayOrderView.as_view(), name='pay-order'),

    # Admin analytics
    path('api/admin/analytics/', sales_summary, name='sales-summary'),

    # Include router URLs for products and categories
    path('api/', include(router.urls)),
]
