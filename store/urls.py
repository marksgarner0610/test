from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    # trang chu
    path('', views.store, name="store"),
    # gio hang
    # path('cart/', views.cart, name="cart"),
    # thanh toan
    path('updateItem/', views.updateItem, name="updateItem"),
    # xem san pham trong danh muc
    path('category/<int:category_id>/', views.view_category.as_view(), name = "category"),
    # quan li them xoa sua hang hoa
    path('manage/', views.manage.as_view(), name = "manage"),
    path('manage/<int:action_id>/', views.manageAction.as_view(), name = "manage_action"),
    path('logout/', views.logout, name = 'logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
