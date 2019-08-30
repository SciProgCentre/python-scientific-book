# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1567179431.2744343
_enable_loop = True
_template_filename = 'themes/bnw/templates/story.tmpl'
_template_uri = 'story.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('zzz', context._clean_inheritance_tokens(), templateuri='zzz_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'zzz')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'zzz')._populate(_import_ns, ['*'])
        def content():
            return render_content(context._locals(__M_locals))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'zzz')._populate(_import_ns, ['*'])
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('        <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(str(post.author()))
        __M_writer('">\n    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(math.math_styles_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'zzz')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        math = _mako_get_namespace(context, 'math')
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <div class="post-header">\n        <div class="container">\n            <div class="title">\n                ')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('\n            </div>\n        </div>\n    </div>\n')
        __M_writer('\n    <div id="post-main" class="main">\n        <div class="container">\n        ')
        __M_writer(str(post.text()))
        __M_writer('\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('            ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n')
        __M_writer('        ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bnw/templates/story.tmpl", "uri": "story.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "29": 5, "32": 6, "38": 0, "56": 1, "57": 3, "58": 4, "59": 5, "60": 6, "61": 7, "66": 19, "71": 41, "77": 9, "89": 9, "90": 10, "91": 10, "92": 11, "93": 12, "94": 12, "95": 12, "96": 14, "97": 14, "98": 14, "99": 15, "100": 15, "101": 16, "102": 16, "103": 17, "104": 17, "105": 18, "106": 18, "112": 21, "125": 21, "126": 22, "127": 23, "128": 26, "129": 26, "130": 31, "131": 34, "132": 34, "133": 35, "134": 36, "135": 36, "136": 36, "137": 38, "138": 38, "139": 38, "145": 139}}
__M_END_METADATA
"""
