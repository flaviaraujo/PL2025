# Trabalho 4 - Analisador Léxico para Linguagem de Query

## Descrição

Este programa implementa um analisador léxico para uma linguagem de consulta baseada em SPARQL.
Ele identifica e tokeniza os principais elementos de uma query, facilitando a sua posterior análise e execução.

O analisador suporta os seguintes tokens:

- **Palavras-chave:** `SELECT`, `WHERE`, `LIMIT` (*case insensitive*);
- **Variáveis:** (`?nome`, `?desc`);
- **Predicados:** (`dbo:MusicalArtist`, `foaf:name`, etc.);
- **Números:** (`1000`);
- **Strings:** (`"Chuck Berry"@en`) (a *tag* de linguagem é opcional);
- **Símbolos:** `{`,`}`, `.`;
- **Comentários:** (`# comentário`).

O código utiliza a biblioteca `ply.lex` para realizar a análise léxica.

## Execução

Para executar o analisador, utilize o seguinte comando:

```bash
python3 tpc4.py < query
```

## Exemplo

### Entrada (query SPARQL):
```
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

### Saída (tokens gerados):
```
LexToken(SELECT, 'select', 1, 0)
LexToken(VAR, '?nome', 1, 7)
LexToken(VAR, '?desc', 1, 13)
LexToken(WHERE, 'where', 1, 19)
LexToken(LCURLY, '{', 1, 25)
LexToken(VAR, '?s', 2, 29)
LexToken(PRED, 'a', 2, 32)
LexToken(PRED, 'dbo:MusicalArtist', 2, 34)
LexToken(DOT, '.', 2, 51)
...
LexToken(LIMIT, 'LIMIT', 7, 98)
LexToken(NUMBER, 1000, 7, 104)
```

## Dependências

- Python 3
- `ply` (instalar com `pip install ply`)

## Autor

- Flávia Alexandra Silva Araújo, A96587 (14/03/2025)


<img src="https://avatars.githubusercontent.com/u/73347444?v=4" alt="Autora" width="10%">

