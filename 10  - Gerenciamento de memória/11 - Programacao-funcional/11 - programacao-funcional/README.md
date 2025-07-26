## 10 - Gerenciamento de Memoria

### Quadro Comparativo: Gestão de Memória em C vs Python

| Aspecto                  | C                                        | Python                                  |
|--------------------------|------------------------------------------|----------------------------------------|
| **Tipo de linguagem**     | Linguagem de programação procedural, de baixo nível | Linguagem de programação de alto nível, interpretada |
| **Gestão de memória**     | Manual                                   | Automática (Gerenciamento automático via Garbage Collector) |
| **Alocação de memória**   | Programador deve usar funções como `malloc()`, `calloc()` para alocar memória dinamicamente | Memória alocada automaticamente ao criar objetos e variáveis |
| **Liberação de memória**  | Programador deve usar `free()` para liberar memória alocada manualmente | Garbage Collector libera memória de objetos que não são mais referenciados |
| **Risco de erros**        | Alto: vazamentos de memória, acesso inválido, estouro de buffer | Baixo: gerenciamento automático minimiza vazamentos e erros de ponteiro |
| **Controle da memória**   | Total controle pelo programador          | Controle abstrato, o programador não manipula diretamente a memória |
| **Ferramentas de suporte**| Debuggers e analisadores de memória externos são necessários (ex: Valgrind) | Monitoramento integrado e bibliotecas para análise de memória (ex: `gc` module) |
| **Performance**           | Alta performance, pois o programador controla exatamente quando alocar e liberar memória | Geralmente menor performance devido ao overhead do Garbage Collector |
| **Uso típico**            | Sistemas embarcados, sistemas operacionais, onde o controle e eficiência são críticos | Aplicações web, ciência de dados, automação, onde a facilidade e rapidez de desenvolvimento são prioritárias |
