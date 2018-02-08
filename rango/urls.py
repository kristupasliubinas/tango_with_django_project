from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    # This URL pattern will match a sequence of alphanumeric characters (\w)
    # and hyphens (\-) which are between the rango/category/ and the trailing /.
    # This sequence will be stored in the parameter category_- name_slug
    # and passed to views.show_category().

    # For example, the URL rango/category/python-books/ would result
    # in the category_name_slug having the value python-books.
]
