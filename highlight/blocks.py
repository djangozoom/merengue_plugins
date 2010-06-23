# Copyright (c) 2010 by Yaco Sistemas <msaelices@yaco.es>
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

from django.utils.translation import ugettext as _

from merengue.block.blocks import Block
from plugins.highlight.models import Highlight


class HighlightBlock(Block):
    name = 'highlight'
    default_place = 'homepage'

    @classmethod
    def render(cls, request, place, context, *args, **kwargs):
        highlight_items = Highlight.objects.published()
        return cls.render_block(request, template_name='highlight/block_highlight.html',
                                block_title=_('Highlight'),
                                context={'highlight_items': highlight_items})
