# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1567179431.2602568
_enable_loop = True
_template_filename = 'themes/bnw/templates/tags.tmpl'
_template_uri = 'tags.tmpl'
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
        items = context.get('items', UNDEFINED)
        range = context.get('range', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        len = context.get('len', UNDEFINED)
        title = context.get('title', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        range = context.get('range', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        len = context.get('len', UNDEFINED)
        title = context.get('title', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div class="meta-header">\n    <div class="container">\n      <div class="title">\n\t')
        __M_writer(str(title))
        __M_writer('\n      </div>\n    </div>\n  </div>\n  <div id="category-tag" class="main">\n    <div class="container">\n')
        if cat_items:
            if items:
                __M_writer('            <h2>')
                __M_writer(str(messages("Categories")))
                __M_writer('</h2>\n')
            for text, full_name, path, link, indent_levels, indent_change_before, indent_change_after in cat_hierarchy:
                for i in range(indent_change_before):
                    __M_writer('                <ul class="postlist">\n')
                __M_writer('            <li><a class="reference" href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a>\n')
                if indent_change_after <= 0:
                    __M_writer('                </li>\n')
                for i in range(-indent_change_after):
                    __M_writer('                </ul>\n')
                    if i + 1 < len(indent_levels):
                        __M_writer('                    </li>\n')
            if items:
                __M_writer('            <h2>')
                __M_writer(str(messages("Tags")))
                __M_writer('</h2>\n')
        if items:
            __M_writer('        <ul class="postlist">\n')
            for text, link in items:
                if text not in hidden_tags:
                    __M_writer('                <li><a class="reference listtitle" href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(str(text))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bnw/templates/tags.tmpl", "uri": "tags.tmpl", "source_encoding": "utf-8", "line_map": {"27": 0, "42": 2, "47": 48, "53": 4, "67": 4, "68": 8, "69": 8, "70": 14, "71": 15, "72": 16, "73": 16, "74": 16, "75": 18, "76": 19, "77": 20, "78": 22, "79": 22, "80": 22, "81": 22, "82": 22, "83": 23, "84": 24, "85": 26, "86": 27, "87": 28, "88": 29, "89": 33, "90": 34, "91": 34, "92": 34, "93": 37, "94": 38, "95": 39, "96": 40, "97": 41, "98": 41, "99": 41, "100": 41, "101": 41, "102": 44, "103": 46, "109": 103}}
__M_END_METADATA
"""
