# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1567179431.1667628
_enable_loop = True
_template_filename = 'themes/bnw/templates/zzz_footer.tmpl'
_template_uri = 'zzz_footer.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_footer']


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
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        twitter = _import_ns.get('twitter', context.get('twitter', UNDEFINED))
        github = _import_ns.get('github', context.get('github', UNDEFINED))
        email = _import_ns.get('email', context.get('email', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <footer>\n        <div class="container">\n            <div class="social">\n')
        if email:
            __M_writer('                <div class="social-entry">\n                    <a href="mailto:')
            __M_writer(str(email))
            __M_writer('" target="_blank">\n                        <i class="fa fa-envelope-o"></i>\n                    </a>\n                </div>\n')
        __M_writer('\n')
        if twitter:
            __M_writer('                <div class="social-entry">\n                    <a href="https://twitter.com/')
            __M_writer(str(twitter))
            __M_writer('" target="_blank">\n                        <i class="fa fa-twitter"></i>\n                    </a>\n                </div>\n')
        __M_writer('\n')
        if github:
            __M_writer('                <div class="social-entry">\n                    <a href="https://github.com/')
            __M_writer(str(github))
            __M_writer('" target="_blank">\n                        <i class="fa fa-github"></i>\n                    </a>\n                </div>\n')
        __M_writer('\n                <div class="social-entry">\n                    <a href="')
        __M_writer(str(_link('rss', None, lang)))
        __M_writer('" target="_blank">\n                        <i class="fa fa-rss"></i> \n                    </a>\n                </div>\n            </div>\n')
        if content_footer:
            __M_writer('                <div class="copyright">\n                    ')
            __M_writer(str(content_footer))
            __M_writer('\n                    ')
            __M_writer(str(template_hooks['page_footer']()))
            __M_writer('\n                </div>\n')
        __M_writer('           ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n        </div>\n    </footer>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bnw/templates/zzz_footer.tmpl", "uri": "zzz_footer.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 47, "40": 4, "53": 4, "54": 8, "55": 9, "56": 10, "57": 10, "58": 15, "59": 16, "60": 17, "61": 18, "62": 18, "63": 23, "64": 24, "65": 25, "66": 26, "67": 26, "68": 31, "69": 33, "70": 33, "71": 38, "72": 39, "73": 40, "74": 40, "75": 41, "76": 41, "77": 44, "78": 44, "79": 44, "85": 79}}
__M_END_METADATA
"""
