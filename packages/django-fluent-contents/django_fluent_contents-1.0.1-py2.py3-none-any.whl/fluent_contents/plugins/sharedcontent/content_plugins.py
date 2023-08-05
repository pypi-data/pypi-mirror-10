from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from fluent_contents import appsettings
from fluent_contents.extensions import ContentPlugin, ContentItemForm, plugin_pool
from fluent_contents.plugins.sharedcontent.models import SharedContentItem
from fluent_contents.rendering import render_placeholder


class SharedContentItemForm(ContentItemForm):
    """
    Admin form for shared content item.
    """
    def __init__(self, *args, **kwargs):
        super(SharedContentItemForm, self).__init__(*args, **kwargs)

        # Filter dynamically, not with limit_choices_to.
        # This supports a threadlocal SITE_ID that django-multisite uses for example.
        if appsettings.FLUENT_CONTENTS_FILTER_SITE_ID:
            field = self.fields['shared_content']
            field.queryset = field.queryset.parent_site(settings.SITE_ID)


@plugin_pool.register
class SharedContentPlugin(ContentPlugin):
    """
    Plugin for sharing content at the page.
    """
    model = SharedContentItem
    form = SharedContentItemForm
    category = _('Advanced')
    cache_output = False                # Individual items are cached, complete block not yet.
    render_ignore_item_language = True  # Only switch for individual items, not this entire block.

    def render(self, request, instance, **kwargs):
        # Not using "template" parameter yet of render_placeholder().
        # The render_placeholder() returns a ContentItemOutput object, which contains both the media and HTML code.
        # Hence, no mark_safe() or escaping is applied here.
        shared_content = instance.shared_content
        return render_placeholder(request, shared_content.contents, parent_object=shared_content, fallback_language=True)

    # NOTE: typically, get_frontend_media() should be overwritten,
    # but render_placeholder() already tracks all media in the request.
