from urllib import parse
from django import template
from django.shortcuts import resolve_url

register = template.Library()


@register.simple_tag
def get_return_link(request):
    top_page = resolve_url('hp:top')
    referer = request.environ.get('HTTP_REFERER')

    if referer:

        parse_result = parse.urlparse(referer)
        if request.get_host() == parse_result.netloc:
            return referer

    return top_page


@register.simple_tag
def url_replace(request, field, value):
    url_dict = request.GET.copy()
    url_dict[field] = str(value)
    return url_dict.urlencode()
