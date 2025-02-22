# Trabalho 2

## Descrição

O programa foi desenvolvido para processar um ficheiro `.csv` contendo registos musicais,
onde extrai informações relevantes e gera um resumo da distribuição dos artistas, dos períodos e das obras musicais.

## Funcionalidade

O programa executa as seguintes etapas:

1. **Leitura do ficheiro de entrada**: Obtém o conteúdo do ficheiro especificado pelo utilizador (neste caso, `obras.csv`);
2. **Identificação das linhas de dados**: Processa as linhas do ficheiro para extrair registos;
3. **Análise dos registos**:
   - Extrai e organiza os dados em campos delimitados por `;` (título, ano, género, período, artista, outros campos);
   - Recolhe informações sobre artistas, distribuição de períodos e obras associadas a cada período (Barroco, Clássico, Medieval, etc.);
4. **Escrita dos resultados num ficheiro JSON**: Guarda o resumo no ficheiro `out/music_results.json`;
5. **Exibição do resumo no terminal**: Apresenta os dados recolhidos de forma estruturada.

## Funcionamento

### Raciocínio do Código

O programa segue um fluxo bem definido:

1. **Leitura do ficheiro CSV**:
   - A função `read_input_file(file_path)` abre o ficheiro e retorna o seu conteúdo como uma string.
   
2. **Extração de dados**:
   - `find_data_rows(file_content)` utiliza uma expressão regular para identificar linhas com registos musicais.
   - `parse_record(full_line)` divide cada linha em campos, respeitando os delimitadores `;`, inclusive quando dentro de aspas.
   
3. **Análise dos registos**:
   - `analyze_records(records)` percorre cada linha processada, extrai informações dos campos e constrói um resumo:
     - Conjunto de artistas distintos.
     - Distribuição dos períodos musicais.
     - Obras organizadas por período.
   
4. **Geração de saída**:
   - `write_output_file(summary)` grava os resultados num ficheiro JSON.
   - `display_summary(summary, total_records)` imprime os resultados no terminal.

### Expressões Regulares Utilizadas

1. **Extração de Linhas de Dados**:
   ```python
   row_pattern = r'^(.*)(?:\n {8}(.*?))*$'
   ```
   - Captura uma linha completa, incluindo continuações indentadas.
   
2. **Divisão de Campos CSV**:
   ```python
   tokens = re.split(rf'({FIELD_DELIMITER}\")|(\"{FIELD_DELIMITER})|({FIELD_DELIMITER})', full_line)
   ```
   - Divide a linha em campos considerando `;`, mesmo quando entre aspas duplas.

## Exemplo de Output

Após a execução do programa, o utilizador pode visualizar um resumo da distribuição dos artistas, períodos e obras musicais, bem como a contagem total de registos processados. Segue-se um excerto do output:

```json
{
    "artists": [
        "Alessandro Stradella",
        "Antonio Maria Abbatini",
        "Bach, Johann Christoph",
        ...
    ],
    "period_distribution": {
        "Barroco": 26,
        "Clássico": 15,
        "Medieval": 48,
        "Renascimento": 41,
        "Século XX": 18,
        "Romântico": 19,
        "Contemporâneo": 7
    },
    "works_by_period": {
        "Barroco": [
            "Ab Irato",
            "Die Ideale, S.106",
            "Fantasy No. 2",
            ...
        ],
        "Clássico": [
            "Bamboula, Op. 2",
            "Capriccio Italien",
            "Czech Suite",
            ...
        ],
        "Medieval": [
            "Adagio in B minor",
            "Ballade No.1",
            ...
        ],
        ...
    }
}
Processed 174 records
```

Os resultados também são guardados em `out/music_results.json`.

## Conclusão

O programa foi desenvolvido com o intuito de processar ficheiros `.csv` contendo registos musicais, permitindo extrair informações relevantes e gerar um resumo da distribuição dos artistas, períodos e obras musicais. Através da análise dos dados, é possível obter uma visão geral dos registos processados, facilitando a identificação de padrões e a organização dos dados de acordo com estes.

## Autor
- Flávia Alexandra Silva Araújo, A96587

<img src="https://avatars.githubusercontent.com/u/73347444?v=4" alt="Autora" width="10%">

