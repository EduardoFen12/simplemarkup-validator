from lexer import tokenize
from parser import parse

def validar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()

        print(f"\nValidando arquivo: {nome_arquivo}")

        tokens = tokenize(conteudo)
        print("Tokens:", tokens)

        valido, mensagem = parse(tokens)

        if valido:
            print("Resultado: ✔ Arquivo VÁLIDO!")
        else:
            print("Resultado: ❌ Arquivo INVÁLIDO!")
            print("Motivo:", mensagem)

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")


if __name__ == "__main__":
    validar_arquivo("src-sm-validos/documento1_valido.sm")
    validar_arquivo("src-sm-validos/documento2_valido.sm")
    validar_arquivo("src-sm-validos/documento3_valido.sm")
    validar_arquivo("src-sm-invalidos/documento1_invalido.sm")
    validar_arquivo("src-sm-invalidos/documento2_invalido.sm")
    validar_arquivo("src-sm-invalidos/documento3_invalido.sm")
