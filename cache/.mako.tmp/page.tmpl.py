# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1567179431.2703967
_enable_loop = True
_template_filename = '/home/zelenyy/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/page.tmpl'
_template_uri = 'page.tmpl'
_source_encoding = 'utf-8'
_exports = []


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
    return runtime._inherit_from(context, 'story.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/zelenyy/anaconda3/lib/python3.6/site-packages/nikola/data/themes/base/templates/page.tmpl", "uri": "page.tmpl", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "38": 32}}
__M_END_METADATA
"""
