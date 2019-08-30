# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1567179431.1286485
_enable_loop = True
_template_filename = 'themes/bnw/templates/list_post.tmpl'
_template_uri = 'list_post.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        posts = context.get('posts', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        posts = context.get('posts', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div class="meta-header">\n    <div class="container">\n      <div class="title">\n\t')
        __M_writer(str(title))
        __M_writer('\n      </div>\n    </div>\n  </div>\n  <div id="post-list" class="main">\n    <div class="container">\n')
        if posts:
            __M_writer('    <ul class="postlist">\n')
            for post in posts:
                __M_writer('          <li> <time class="listdate" datetime="')
                __M_writer(str(post.date.isoformat()))
                __M_writer('" title="')
                __M_writer(str(post.formatted_date(date_format)))
                __M_writer('">')
                __M_writer(str(post.formatted_date('YYYY-MM-dd')))
                __M_writer('</time> <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</a> </li>\n')
            __M_writer('    </ul>\n')
        else:
            __M_writer('    <p>')
            __M_writer(str(messages("No posts found.")))
            __M_writer('</p>\n')
        __M_writer('    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bnw/templates/list_post.tmpl", "uri": "list_post.tmpl", "source_encoding": "utf-8", "line_map": {"27": 0, "38": 2, "43": 25, "49": 4, "59": 4, "60": 8, "61": 8, "62": 14, "63": 15, "64": 16, "65": 17, "66": 17, "67": 17, "68": 17, "69": 17, "70": 17, "71": 17, "72": 17, "73": 17, "74": 17, "75": 17, "76": 19, "77": 20, "78": 21, "79": 21, "80": 21, "81": 23, "87": 81}}
__M_END_METADATA
"""
