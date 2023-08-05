# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from blogit import settings as bs
from blogit.views import (
    CategoryListView, CategoryDetailView,
    PostYearArchiveView, PostMonthArchiveView, PostDayArchiveView,
    PostListView, PostDetailView, PostDateDetailView)
from blogit.feeds import PostRssFeed, PostAtomFeed


pats = [
    url(r'^$', PostListView.as_view(), name='blogit_post_list'),
]

pats.extend([
    url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/(?P<day>\d+)/$',
        PostDayArchiveView.as_view(), name='blogit_post_archive_day'),

    url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/$',
        PostMonthArchiveView.as_view(), name='blogit_post_archive_month'),

    url(r'^(?P<year>\d+)/$', PostYearArchiveView.as_view(),
        name='blogit_post_archive_year'),
])


pats.extend([
    url(r'^%s/$' % bs.CATEGORY_URL,
        CategoryListView.as_view(), name='blogit_category_list'),

    url(r'^%s/(?P<slug>[-\w\d]+)/$' % bs.CATEGORY_URL,
        CategoryDetailView.as_view(), name='blogit_category_detail'),
])


if bs.RSS_FEED:
    pats.extend([
        url(r'^%s/rss/$' % bs.FEED_URL, PostRssFeed()),
        url(r'^%s/rss/(?P<tag_slug>[-\w]+)/$' % bs.FEED_URL, PostRssFeed()),
    ])

if bs.ATOM_FEED:
    pats.extend([
        url(r'^%s/atom/(?P<tag_slug>[-\w]+)/$' % bs.FEED_URL, PostAtomFeed()),
        url(r'^%s/atom/$' % bs.FEED_URL, PostAtomFeed())
    ])


if bs.POST_DETAIL_DATE_URL:
    pats.append(url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/(?P<day>\d+)'
                    r'/(?P<slug>[-\w\d]+)/$', PostDateDetailView.as_view(),
                    name='blogit_post_detail_date'))
else:
    pats.append(url(r'^(?P<slug>[-\w\d]+)/$', PostDetailView.as_view(),
                name='blogit_post_detail'))


urlpatterns = patterns('', *pats)
