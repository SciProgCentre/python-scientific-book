# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1567179431.1508622
_enable_loop = True
_template_filename = 'themes/bnw/templates/zzz_helper.tmpl'
_template_uri = 'zzz_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'html_stylesheets', 'html_feedlinks', 'late_load_js', 'html_tags', 'html_title', 'html_translations', 'html_sourcelink']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_stylesheets():
            return render_html_stylesheets(context)
        permalink = context.get('permalink', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        url_replacer = context.get('url_replacer', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        description = context.get('description', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        title = context.get('title', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\n\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        __M_writer('\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('        <link href="/assets/css/font-awesome.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/bnw.css" rel="stylesheet" type="text/css">\n\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js" type="text/javascript"></script>\n')
        else:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n')
            else:
                __M_writer('            <script src="/assets/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n            <script src="/assets/js/headroom.min.js" type="text/javascript"></script>\n            <script src="/assets/js/scripts.js" type="text/javascript"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        theme_tag = context.get('theme_tag', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <div itemprop="keywords" class="tags right">\n        <span class=tags>\n            <span class=\'muted small\'> <i class="icon-tag"></i> </span>\n')
        for tag in post.tags:
            __M_writer('        <a\n')
            if theme_tag is not UNDEFINED:
                for (theme, tag_name) in theme_tag.items():
                    if tag_name == tag:
                        __M_writer("                    class='small ")
                        __M_writer(str(theme))
                        __M_writer("'\n                    id='tag-theme' \n                    data-theme='")
                        __M_writer(str(theme))
                        __M_writer("'\n\n")
            __M_writer('        href="')
            __M_writer(str(_link('tag', tag)))
            __M_writer('" rel="tag">')
            __M_writer(str(tag))
            __M_writer('</a>\n')
        __M_writer('        </span>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">\n                ')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('        &nbsp;&nbsp;|&nbsp;&nbsp;\n        <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bnw/templates/zzz_helper.tmpl", "uri": "zzz_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 61, "23": 80, "24": 94, "25": 113, "26": 137, "27": 143, "28": 154, "29": 161, "35": 3, "62": 3, "63": 6, "64": 7, "65": 8, "66": 10, "67": 11, "68": 13, "69": 14, "70": 15, "71": 17, "72": 18, "73": 21, "74": 21, "75": 21, "76": 24, "77": 25, "78": 25, "79": 25, "80": 27, "81": 28, "82": 28, "83": 28, "84": 28, "85": 30, "86": 30, "87": 31, "88": 31, "89": 32, "90": 33, "91": 33, "92": 33, "93": 35, "94": 36, "95": 37, "96": 38, "97": 38, "98": 38, "99": 38, "100": 38, "101": 38, "102": 38, "103": 41, "104": 42, "105": 43, "106": 43, "107": 43, "108": 45, "109": 46, "110": 47, "111": 47, "112": 47, "113": 49, "114": 50, "115": 50, "116": 50, "117": 52, "118": 53, "119": 53, "120": 54, "121": 55, "122": 56, "123": 57, "124": 57, "125": 57, "126": 59, "127": 60, "128": 60, "134": 63, "141": 63, "142": 64, "143": 65, "144": 66, "145": 67, "146": 68, "147": 70, "148": 71, "149": 76, "150": 77, "156": 82, "165": 82, "166": 83, "167": 84, "168": 84, "169": 84, "170": 85, "171": 86, "172": 87, "173": 88, "174": 88, "175": 88, "176": 88, "177": 88, "178": 90, "179": 91, "180": 91, "181": 91, "187": 96, "193": 96, "194": 97, "195": 98, "196": 99, "197": 100, "198": 101, "199": 103, "200": 104, "201": 105, "202": 106, "203": 107, "209": 116, "215": 116, "216": 121, "217": 122, "218": 123, "219": 124, "220": 125, "221": 126, "222": 126, "223": 126, "224": 128, "225": 128, "226": 133, "227": 133, "228": 133, "229": 133, "230": 133, "231": 135, "237": 139, "243": 139, "244": 140, "245": 141, "246": 141, "247": 141, "253": 145, "261": 145, "262": 146, "263": 147, "264": 148, "265": 149, "266": 149, "267": 149, "268": 149, "269": 149, "270": 150, "271": 150, "277": 156, "284": 156, "285": 157, "286": 158, "287": 159, "288": 159, "289": 159, "290": 159, "296": 290}}
__M_END_METADATA
"""
