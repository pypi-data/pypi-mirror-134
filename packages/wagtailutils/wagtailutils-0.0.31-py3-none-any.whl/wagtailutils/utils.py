from wagtail.core.models import Site
from wagtail.core.rich_text import expand_db_html


def prepare_richtext_for_api(value):
    s = Site.objects.get(is_default_site=True)
    current_site = s.root_url
    replace_text = 'src="{0}/'.format(current_site)
    html_data = expand_db_html(value)
    html_data = html_data.replace('src="/', replace_text)
    return html_data
