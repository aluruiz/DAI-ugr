# práctica_05/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test_template/$', views.test_template, name='test_template'),
  url(r'^nuevomusico$', views.AddMusico, name='crear_musico'),
  url(r'^nuevogrupo$', views.AddGrupo, name='crear_grupo'),
  url(r'^borrarmusico/(?P<id_musico>\d+)/$', views.DeleteMusico, name='borrar_musico'),
  url(r'^listarmusico$', views.ListMusico, name='listar_musico'),
  url(r'^editarmusico/(?P<id_musico>\d+)/$', views.ModifyMusico, name='editar_musico'),
  url(r'^borrargrupo/(?P<id_grupo>\d+)/$', views.DeleteGrupo, name='borrar_grupo'),
  url(r'^listargrupo$', views.ListGrupo, name='listar_grupo'),
  url(r'^editargrupo/(?P<id_grupo>\d+)/$', views.ModifyGrupo, name='editar_grupo'),
  url(r'^paginador/(?P<id_pagina>\d+)/$', views.paginador_Query, name='query'),
  url(r'^paginadorajax$', views.paginador_ajax, name='ajax'),
  url(r'^ajax/$', views.reclamaDatos, name='reclama_datos'),
  url(r'^ajax/(?P<id_pagina>\d+)/$', views.reclamaDatos, name='reclama_datos'),
  url(r'^grafica$', views.graficas, name='graficas'),
  url(r'^mapa$', views.mapas, name='mapas')
]