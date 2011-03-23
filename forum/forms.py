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

from transmeta import get_real_fieldname

from merengue.base.forms import BaseModelForm
from plugins.forum.models import ForumThreadComment, Thread


class CaptchaForumThreadCommentForm(BaseModelForm):

    class Meta:
        model = ForumThreadComment
        fields = ('title', 'comment', )

    def __init__(self, user, *args, **kwargs):
        super(CaptchaForumThreadCommentForm, self).__init__(*args, **kwargs)


class CreateThreadForm(BaseModelForm):
    class Meta:
        model = Thread
        fields = (get_real_fieldname('name'), get_real_fieldname('description'), 'tags', )
