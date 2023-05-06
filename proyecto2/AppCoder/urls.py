from django.urls import path
from .views import *
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path("", inicioApp, name="inicioApp"),

    path("comentario/", comentarios, name="comentarios"),

    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("agregarAvatar", agregarAvatar, name="agregarAvatar"),
    
    path("abrigos/", abrigos, name="abrigos"),
    path("abrigo/list/", AbrigoList.as_view(), name="abrigo_list"),
    path("abrigo/nuevo", AbrigoAgregar.as_view(), name="abrigo_agregar"),
    path("abrigo/<pk>", AbrigoDetalle.as_view(), name="abrigo_detalle"),
    path("abrigo/editar/<pk>", AbrigoUpdate.as_view(), name="abrigo_editar"),
    path("abrigo/borrar/<pk>", AbrigoDelete.as_view(), name="abrigo_borrar"),

    path("camisetas/", camisetas, name="camisetas"),
    path("camiseta/list/", CamisetaList.as_view(), name="camiseta_list"),
    path("camiseta/nuevo", CamisetaAgregar.as_view(), name="camiseta_agregar"),
    path("camiseta/<pk>", CamisetaDetalle.as_view(), name="camiseta_detalle"),
    path("camiseta/editar/<pk>", CamisetaUpdate.as_view(), name="camiseta_editar"),
    path("camiseta/borrar/<pk>", CamisetaDelete.as_view(), name="camiseta_borrar"),

    path("pantalones/", pantalones, name="pantalones"),
    path("pantalon/list/", PantalonList.as_view(), name="pantalon_list"),
    path("pantalon/nuevo", PantalonAgregar.as_view(), name="pantalon_agregar"),
    path("pantalon/<pk>", PantalonDetalle.as_view(), name="pantalon_detalle"),
    path("pantalon/editar/<pk>", PantalonUpdate.as_view(), name="pantalon_editar"),
    path("pantalon/borrar/<pk>", PantalonDelete.as_view(), name="pantalon_borrar"),

    path("zapatos/", zapatos, name="zapatos"),
    path("zapato/list/", ZapatoList.as_view(), name="zapato_list"),
    path("zapato/nuevo", ZapatoAgregar.as_view(), name="zapato_agregar"),
    path("zapato/<pk>", ZapatoDetalle.as_view(), name="zapato_detalle"),
    path("zapato/editar/<pk>", ZapatoUpdate.as_view(), name="zapato_editar"),
    path("zapato/borrar/<pk>", ZapatoDelete.as_view(), name="zapato_borrar"),

    path('pantalon_detalle/<pk>/comentario/', ComentarioPage.as_view(), name='comentarios'),
    path('abrigo_detalle/<pk>/comentario/', ComentarioPage.as_view(), name='comentarios'),
    path('camiseta_detalle/<pk>/comentario/', ComentarioPage.as_view(), name='comentarios'),
    path('zapato_detalle/<pk>/comentario/', ComentarioPage.as_view(), name='comentarios'),
]