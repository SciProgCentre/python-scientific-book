# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1567179431.161365
_enable_loop = True
_template_filename = 'themes/bnw/templates/zzz_header.tmpl'
_template_uri = 'zzz_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_header', 'html_site_title', 'html_site_tagline', 'html_navigation_links']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def html_site_title():
            return render_html_site_title(context)
        def html_navigation_links():
            return render_html_navigation_links(context)
        __M_writer = context.writer()
        __M_writer('\n\n    <header id="header" class="navbar">\n        <div class="container">\n            ')
        __M_writer(str(html_site_title()))
        __M_writer('\n            ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n        </div>\n    </header>\n    <div class="header-padding"> </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <div class="brand">\n')
        if logo_url:
            __M_writer('        <div class="logo">\n            <a href="')
            __M_writer(str(abs_link('/')))
            __M_writer('" title="')
            __M_writer(str(blog_title))
            __M_writer('" rel="home">\n                <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(str(blog_title))
            __M_writer('" id="logo">\n            </a>\n        </div>\n        <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(str(blog_title))
            __M_writer('" id="logo">\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('        <div class="brand-text">\n            <a href="')
            __M_writer(str(abs_link('/')))
            __M_writer('" title="')
            __M_writer(str(blog_title))
            __M_writer('" rel="home">\n                ')
            __M_writer(str(blog_title))
            __M_writer('\n            </a>\n        </div>\n')
        __M_writer('\n        <a id="btn-toggle-nav" class="navbar-toggle">\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n        </a>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_tagline(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        blog_description = _import_ns.get('blog_description', context.get('blog_description', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if show_blog_title and blog_description:
            __M_writer('    <div class="tagline">\n        <div class="container">\n        ')
            __M_writer(str(blog_description))
            __M_writer('\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <nav class="navbar-collapse collapse">\n    <ul class="nav">\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            <!-- sub navigation not supported yet -->\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('                <li class="active"><a href="')
                    __M_writer(str(permalink))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
                else:
                    __M_writer('                <li><a href="')
                    __M_writer(str(url))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n    </ul>\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bnw/templates/zzz_header.tmpl", "uri": "zzz_header.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 13, "35": 41, "36": 51, "37": 71, "43": 4, "53": 4, "54": 8, "55": 8, "56": 9, "57": 9, "63": 16, "73": 16, "74": 18, "75": 19, "76": 20, "77": 20, "78": 20, "79": 20, "80": 21, "81": 21, "82": 21, "83": 21, "84": 24, "85": 24, "86": 24, "87": 24, "88": 26, "89": 27, "90": 28, "91": 29, "92": 29, "93": 29, "94": 29, "95": 30, "96": 30, "97": 34, "103": 43, "111": 43, "112": 44, "113": 45, "114": 47, "115": 47, "121": 53, "134": 53, "135": 56, "136": 57, "137": 58, "138": 59, "139": 60, "140": 61, "141": 61, "142": 61, "143": 61, "144": 61, "145": 62, "146": 63, "147": 63, "148": 63, "149": 63, "150": 63, "151": 67, "152": 67, "153": 67, "154": 68, "155": 68, "161": 155}}
__M_END_METADATA
"""
