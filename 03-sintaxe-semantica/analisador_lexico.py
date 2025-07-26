#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analisador Léxico para a Linguagem Fantasil
Disciplina: Compiladores - Desafio 03
"""

class Token:
    def __init__(self, tipo, valor, linha):
        self.tipo = tipo
        self.valor = valor
        self.linha = linha
    
    def __str__(self):
        return f"Token(tipo='{self.tipo}', valor='{self.valor}', linha={self.linha})"

class AnalisadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0
        self.linha = 1
        self.tokens = []
        self.palavras_chave = {
            'conjurar': 'CONJURAR',
            'se': 'SE',
            'senao': 'SENAO',
            'enquanto': 'ENQUANTO',
            'int': 'INT',
            'texto': 'TEXTO',
            'bool': 'BOOL'
        }
        self.elementos = ['fogo', 'agua', 'terra', 'ar']

    def analisar(self):
        while self.pos < len(self.codigo):
            char = self.codigo[self.pos]

            if char.isspace():
                if char == '\n':
                    self.linha += 1
                self.pos += 1
                continue

            if char == '#':
                self.ignorar_comentario()
                continue

            # Identificadores e palavras-chave
            if char.isalpha():
                self.identificar_identificador()
                continue

            # Números
            if char.isdigit():
                self.identificar_numero()
                continue

            # Strings
            if char == '"':
                self.identificar_string()
                continue

            # Operadores e delimitadores
            if char in '+-*/%=<>!&|':
                self.identificar_operador()
                continue

            if char in '(){}[],;:':
                self.tokens.append(Token('DELIMITADOR', char, self.linha))
                self.pos += 1
                continue

            raise Exception(f"Caractere inesperado '{char}' na linha {self.linha}")

        return self.tokens

    def ignorar_comentario(self):
        while self.pos < len(self.codigo) and self.codigo[self.pos] != '\n':
            self.pos += 1

    def identificar_identificador(self):
        inicio = self.pos
        while self.pos < len(self.codigo) and (self.codigo[self.pos].isalnum() or self.codigo[self.pos] == '_'):
            self.pos += 1

        lexema = self.codigo[inicio:self.pos]

        if lexema in self.palavras_chave:
            tipo = self.palavras_chave[lexema]
        elif lexema in self.elementos:
            tipo = 'ELEMENTO'
        else:
            tipo = 'IDENTIFICADOR'

        self.tokens.append(Token(tipo, lexema, self.linha))

    def identificar_numero(self):
        inicio = self.pos
        while self.pos < len(self.codigo) and self.codigo[self.pos].isdigit():
            self.pos += 1

        # Verificar se há ponto decimal
        if self.pos < len(self.codigo) and self.codigo[self.pos] == '.':
            self.pos += 1
            while self.pos < len(self.codigo) and self.codigo[self.pos].isdigit():
                self.pos += 1
            tipo = 'REAL'
        else:
            tipo = 'INTEIRO'

        lexema = self.codigo[inicio:self.pos]
        self.tokens.append(Token(tipo, lexema, self.linha))

    def identificar_string(self):
        self.pos += 1  # Pular abertura "
        inicio = self.pos
        
        while self.pos < len(self.codigo) and self.codigo[self.pos] != '"':
            if self.codigo[self.pos] == '\n':
                self.linha += 1
            self.pos += 1

        if self.pos >= len(self.codigo):
            raise Exception(f"String não fechada na linha {self.linha}")

        lexema = self.codigo[inicio:self.pos]
        self.tokens.append(Token('STRING', lexema, self.linha))
        self.pos += 1  # Pular fechamento "

    def identificar_operador(self):
        char = self.codigo[self.pos]
        prox_char = self.codigo[self.pos + 1] if self.pos + 1 < len(self.codigo) else None

        # Operadores de 2 caracteres
        if char + prox_char in ['->', '==', '>=', '<=', '!=']:
            self.tokens.append(Token('OPERADOR', char + prox_char, self.linha))
            self.pos += 2
        else:
            self.tokens.append(Token('OPERADOR', char, self.linha))
            self.pos += 1

def main():
    codigo_exemplo = """
    conjurar bola_de_fogo(int poder) {
        # Comentário: Feitiço básico
        se (poder >= 10) {
            fogo -> inimigo;
        } senao {
            "Falha" -> inimigo;
        }
    }
    """

    analisador = AnalisadorLexico(codigo_exemplo)
    tokens = analisador.analisar()

    print(" ")
    print("Tokens encontrados:\n")
    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()