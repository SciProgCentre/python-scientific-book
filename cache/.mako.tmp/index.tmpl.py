# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1567179431.1724746
_enable_loop = True
_template_filename = 'themes/bnw/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('header', context._clean_inheritance_tokens(), templateuri='zzz_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'header')] = ns

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
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        helper = _mako_get_namespace(context, 'helper')
        html_site_tagline = _import_ns.get('html_site_tagline', context.get('html_site_tagline', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        __M_writer = context.writer()
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
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        helper = _mako_get_namespace(context, 'helper')
        html_site_tagline = _import_ns.get('html_site_tagline', context.get('html_site_tagline', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(html_site_tagline()))
        __M_writer('\n    <div id="index-main" class="main">\n        <div class="container">\n')
        for post in posts:
            __M_writer('        <div class="post-entry">\n            <time class="post-time" datetime="')
            __M_writer(str(post.date.isoformat()))
            __M_writer('">')
            __M_writer(str(post.formatted_date('YYYY-MM-dd')))
            __M_writer('</time>\n            <div class="post-desc">\n                <div class="post-title">\n                    <a href="')
            __M_writer(str(post.permalink()))
            __M_writer('">')
            __M_writer(str(post.title()))
            __M_writer('</a>\n                </div>\n                <div class="post-tags">\n')
            for tag in post.tags:
                __M_writer('                    <div class="tag">\n                        <a href="')
                __M_writer(str(_link('tag', tag)))
                __M_writer('" rel="tag">')
                __M_writer(str(tag))
                __M_writer('</a>\n                    </div>\n')
            __M_writer('                </div>\n                <div class="num-of-comments">\n')
            if not post.meta('nocomments'):
                __M_writer('                    ')
                __M_writer(str(comments.comment_link(post.permalink(), post.base_path)))
                __M_writer('\n')
            __M_writer('                </div>\n                <div class="post-description">\n                    ')
            __M_writer(str(post.description()))
            __M_writer('\n                </div>\n            </div>\n        </div>\n')
        __M_writer('        </div>\n    </div>\n\n    ')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n    ')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bnw/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "55": 2, "56": 3, "57": 4, "58": 5, "59": 6, "64": 10, "69": 47, "75": 8, "85": 8, "86": 9, "87": 9, "93": 12, "107": 12, "108": 13, "109": 13, "110": 16, "111": 17, "112": 18, "113": 18, "114": 18, "115": 18, "116": 21, "117": 21, "118": 21, "119": 21, "120": 24, "121": 25, "122": 26, "123": 26, "124": 26, "125": 26, "126": 29, "127": 31, "128": 32, "129": 32, "130": 32, "131": 34, "132": 36, "133": 36, "134": 41, "135": 44, "136": 44, "137": 45, "138": 45, "139": 46, "140": 46, "146": 140}}
__M_END_METADATA
"""
