"""dandelion-demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# add sitemap feature
from django.contrib.sitemaps.views import index
from django.contrib.sitemaps.views import sitemap

from zinnia.sitemaps import AuthorSitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import TagSitemap
from zinnia.views.channels import EntryChannel

sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^weblog/$', EntryChannel.as_view(
        query='category:python OR category:django')),
    path(r'weblog/', include('zinnia.urls', namespace='zinnia')),
    path(r'comments/', include('django_comments.urls')),
]

urlpatterns += [
    path(r'^sitemap.xml$',
         index,
         {'sitemaps': sitemaps}),
    path(r'^sitemap-(?P<section>.+)\.xml$',
         sitemap,
         {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
