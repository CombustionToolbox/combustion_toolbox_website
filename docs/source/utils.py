def html_align_string(str, align='center'):
    # Get Website title
    str_prefix = '<div "align=' + align + '">'
    str_suffix = '</div>'
    return str_prefix + str + str_suffix