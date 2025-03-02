# Trabalho 3 - Conversor de Markdown para HTML

## Descrição
Este programa converte arquivos escritos em Markdown para HTML.
Ele implementa a conversão dos seguintes elementos da sintaxe básica de Markdown:

- Cabeçalhos (# (título), ## (subtítulo), ### (sub-subtítulo));

- Texto em negrito (**texto**, usando **);

- Texto em itálico (*texto*, usando *);

- Listas numeradas (1. item);

- Links ([texto](url));

- Imagens (![texto alternativo](url));

O programa usa expressões regulares para identificar os elementos Markdown e substituí-los pelas *tags* equivalentes em HTML.
A função `markdown_to_html` realiza essa conversão, recebendo como argumento uma *string* com o conteúdo do ficheiro Markdown e retornando uma *string* com o conteúdo do ficheiro HTML.
A sua execução é feita através da linha de comandos, com a seguinte sintaxe:

```
python3 tpc3.py <input_file> <output_file>
```
Onde `<input_file>` é o caminho para o arquivo Markdown a ser convertido e `<output_file>` é o caminho para o arquivo HTML gerado.



## Exemplo

**Markdown:**
```
# Título Principal

## Subtítulo

### Subsubtítulo

Este é um texto com **negrito** e *itálico*.

1. Primeiro item da lista
2. Segundo item da lista
3. Terceiro item da lista

Aqui está um [link para a Universidade do Minho](https://www.uminho.pt/PT).

E aqui está uma imagem:
[Logo UMinho](https://www.uminho.pt/_layouts/15/UMinho.PortalUM.UI/images/portal-logo.png)
```

**HTML:**
```
<ol><h1>Título Principal</h1>

<h2>Subtítulo</h2>

<h3>Subsubtítulo</h3>

Este é um texto com <b>negrito</b> e <i>itálico</i>.

<li>Primeiro item da lista</li>
<li>Segundo item da lista</li>
<li>Terceiro item da lista</li>

Aqui está um <a href="https://www.uminho.pt/PT">link para a Universidade do Minho</a>.

E aqui está uma imagem:
<a href="https://www.uminho.pt/_layouts/15/UMinho.PortalUM.UI/images/portal-logo.png">Logo UMinho</a>
</ol>
```


## Autor
- Flávia Alexandra Silva Araújo, A96587 (02/03/2025)


<img src="https://avatars.githubusercontent.com/u/73347444?v=4" alt="Autora" width="10%">


