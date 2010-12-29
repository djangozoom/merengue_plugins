# Copyright (c) 2010 by Yaco Sistemas
#
# This file is part of Merengue.
#
# Merengue is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Merengue is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Merengue.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('plugins.feedback.views',
    url(r'^send_comment/(?P<content_type>\d+)/(?P<content_id>\d+)/(?P<parent_id>\d+)/$',
        'content_comment_add', name='comment_add_parent'),
    url(r'^send_comment/(?P<content_type>\d+)/(?P<content_id>\d+)/$', 'content_comment_add', name='comment_add'),
    url(r'^change_comment_visiblity/(?P<comment_id>\d+)/$', 'content_comment_change_visibity', name='comment_change_visibity'),
    url(r'^content_comment_delete/(?P<comment_id>\d+)/$', 'content_comment_delete', name='comment_delete'),
)
