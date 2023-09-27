from django.contrib import admin
from django.urls import path

from django import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('listar', views.listar, name="listar"),
    path('agregar', views.agregar, name="agregar"),
    path('actualizar/<int:idUsuario>', views.actualizar, name="actualizar"),
    path('eliminar/<int:idUsuario>', views.eliminar, name="eliminar"),
    path('listardep', views.listardep, name="listardep"),
    path('agregardep', views.agregardep, name="agregardep"),
    path('actualizardep/<int:idDependencia>', views.actualizardep, name="actualizardep"),
    path('eliminardep/<int:idDependencia>', views.eliminardep, name="eliminardep"),
    path('listarveh', views.listarveh, name="listarveh"),
    path('agregarveh', views.agregarveh, name="agregarveh"),
    path('actualizarveh/<idVehiculo>', views.actualizarveh, name="actualizarveh"),
    path('eliminarveh/<idVehiculo>', views.eliminarveh, name="eliminarveh"),
    path('listarsoa', views.listarsoa, name="listarsoa"),
    path('agregarsoa', views.agregarsoa, name="agregarsoa"),
    path('actualizarsoa/<int:idSoat>', views.actualizarsoa, name="actualizarsoa"),
    path('eliminarsoa/<int:idSoat>', views.eliminarsoa, name="eliminarsoa"),
    path('listartec', views.listartec, name="listartec"),
    path('agregartec', views.agregartec, name="agregartec"),
    path('actualizartec/<int:idTecno>', views.actualizartec, name="actualizartec"),
    path('eliminartec/<int:idTecno>', views.eliminartec, name="eliminartec"),
    path('listarasi', views.listarasi, name="listarasi"),
    path('agregarasi', views.agregarasi, name="agregarasi"),
    path('actualizarasi/<int:idAsignacion>', views.actualizarasi, name="actualizarasi"),
    path('eliminarasi/<int:idAsignacion>', views.eliminarasi, name="eliminarasi"),
    path('listarprem', views.listarprem, name="listarprem"),
    path('agregarprem', views.agregarprem, name="agregarprem"),
    path('actualizarprem/<int:idprem>', views.actualizarprem, name="actualizarprem"),
    path('eliminarprem/<int:idprem>', views.eliminarprem, name="eliminarprem"),
    path('listarprec', views.listarprec, name="listarprec"),
    path('agregarprec', views.agregarprec, name="agregarprec"),
    path('actualizarprec/<int:idprec>', views.actualizarprec, name="actualizarprec"),
    path('eliminarprec/<int:idprec>', views.eliminarprec, name="eliminarprec"),
    path('listarman', views.listarman, name="listarman"),
    path('agregarman', views.agregarman, name="agregarman"),
    path('actualizarman/<int:idman>', views.actualizarman, name="actualizarman"),
    path('eliminarman/<int:idman>', views.eliminarman, name="eliminarman"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)