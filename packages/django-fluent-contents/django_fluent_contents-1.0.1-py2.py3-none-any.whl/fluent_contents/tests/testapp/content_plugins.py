from django.utils.safestring import mark_safe
from fluent_contents.extensions import ContentPlugin, plugin_pool
from fluent_contents.tests.testapp.models import RawHtmlTestItem, TimeoutTestItem


@plugin_pool.register
class RawHtmlTestPlugin(ContentPlugin):
    """
    The most basic "raw HTML" plugin item, for testing.
    """
    model = RawHtmlTestItem

    def render(self, request, instance, **kwargs):
        return mark_safe(instance.html)


@plugin_pool.register
class TimeoutTestPlugin(ContentPlugin):
    """
    Testing a plugin timeout.
    """
    model = TimeoutTestItem
    cache_timeout = 60

    def render(self, request, instance, **kwargs):
        return mark_safe(instance.html)
