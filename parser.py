def parse(tokens):
    stack = []

    for token_type, value in tokens:

        # TAG DE ABERTURA → empilha
        if token_type == 'TAG_ABERTURA':
            stack.append(value)

        # TAG DE FECHAMENTO → verificar stack
        elif token_type == 'TAG_FECHAMENTO':
            if not stack:
                return False, f"Erro: tag </{value}> encontrada sem abertura."

            top = stack.pop()
            if top != value:
                return False, f"Erro: esperado </{top}> mas encontrado </{value}>."

        # TEXTO → ignorar
        else:
            continue

    # Após processar tudo, verificar se sobrou tag aberta
    if stack:
        return False, f"Erro: a tag <{stack[-1]}> foi aberta mas não fechada."

    return True, "Sintaxe válida!"
