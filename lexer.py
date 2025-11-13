import re

def tokenize(text):
    # Padrão para identificar: <tag>, </tag> e texto
    token_pattern = r'(</?[a-zA-Z_][a-zA-Z0-9_]*>)'

    raw_tokens = re.split(token_pattern, text)
    tokens = []

    for item in raw_tokens:
        item = item.strip()
        if not item:
            continue

        # TAG DE FECHAMENTO
        if re.match(r'</[a-zA-Z_][a-zA-Z0-9_]*>', item):
            tag_name = item[2:-1]
            tokens.append(('TAG_FECHAMENTO', tag_name))

        # TAG DE ABERTURA
        elif re.match(r'<[a-zA-Z_][a-zA-Z0-9_]*>', item):
            tag_name = item[1:-1]
            tokens.append(('TAG_ABERTURA', tag_name))

        # TEXTO
        else:
            tokens.append(('TEXTO', item))

    return tokens
