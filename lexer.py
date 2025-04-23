import re

def html_lexer(code):
    tokens = []
    tag_pattern = re.compile(r'</?[^>]+>')
    pos = 0

    while pos < len(code):
        match = tag_pattern.match(code, pos)
        if match:
            tag = match.group()
            if tag.startswith('</'):
                tokens.append({'type': 'CLOSE_TAG', 'value': tag[2:-1].strip()})
            else:
                tokens.append({'type': 'OPEN_TAG', 'value': tag[1:-1].strip()})
            pos = match.end()
        else:
            text_end = code.find('<', pos)
            if text_end == -1:
                text_end = len(code)
            tokens.append({'type': 'TEXT', 'value': code[pos:text_end]})
            pos = text_end
    return tokens
