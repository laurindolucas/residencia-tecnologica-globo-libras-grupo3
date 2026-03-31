# Projeto de Geração Automática de Libras com IA
## Grupo 3 — Tradução para Libras e Geração de Avatar

### Visão Geral
Este módulo faz parte do projeto desenvolvido na Residência Tecnológica GrowUp, com o objetivo de criar um sistema capaz de gerar traduções automáticas em Libras a partir de vídeos. O Grupo 3 é responsável por transformar o texto transcrito em representações em Libras e exibi-las por meio de um avatar animado, atuando como ponte entre a linguagem natural (português) e a linguagem visual (Libras).

---

### Responsabilidades do Grupo 3
* Converter texto (com timestamps) em estrutura compatível com Libras.
* Aplicar regras linguísticas e adaptações necessárias (evitar tradução literal).
* Integrar APIs ou modelos de tradução para Libras.
* Gerar animações com avatar em sincronia com o tempo do vídeo.
* Garantir qualidade visual e semântica da tradução.

---

### Organização no Trello
O fluxo de desenvolvimento é organizado através das seguintes colunas de tarefas:

| Coluna | Descrição |
| :--- | :--- |
| Backlog | Funcionalidades, melhorias e pesquisas. |
| Em andamento | Atividades em desenvolvimento técnico. |
| Em revisão | Código aguardando validação de pares. |
| Concluído | Tarefas finalizadas e validadas. |
| Integração | Comunicação entre Grupo 2 (entrada) e Grupo 4 (exibição). |
| links importnates | Salvar links importantes para o desenvolvimento |

---

### Estrutura das Tarefas

#### Padrão de Título
Todas as tarefas devem seguir o formato:  
`[G3] Nome da tarefa`

#### Descrição da Tarefa
Cada tarefa deve conter:
1. **Objetivo claro**
2. **Contexto** (quando necessário)
3. **Dependências** (ex: dados do Grupo 2 ou integração com Grupo 4)

#### Checklist Padrão
- [ ] Receber texto com timestamps
- [ ] Processar tradução para Libras
- [ ] Adaptar estrutura gramatical
- [ ] Integrar com sistema de avatar
- [ ] Validar sincronização
- [ ] Testar resultado final

---

### Critérios de Conclusão
Uma tarefa só pode ser marcada como concluída quando apresentar:
* Checklist totalmente finalizado.
* Tradução validada (sem erros semânticos graves).
* Avatar executando corretamente.
* Sincronização com timestamps funcional.
* Testes realizados com sucesso.
* Integrações validadas.

---

### Boas Práticas
> **Nota linguística:** Evitar tradução literal — respeitar sempre a estrutura da Libras.

* Testar sempre com diferentes tipos de frases.
* Manter consistência nas animações do avatar.
* Dividir tarefas grandes (ex: separar tradução de animação).
* Documentar decisões linguísticas importantes.
* Alinhar frequentemente com Grupo 2 e Grupo 4.

---

### Integrações e Metodologia

**Dependências de Fluxo:**
1. **Grupo 2:** Fornece texto e timestamps.
2. **Grupo 3:** Realiza a tradução e gera a animação.
3. **Grupo 4:** Consome o avatar renderizado para exibição.

**Metodologia Scrum:**
* **Planning:** Definição das tarefas da sprint.
* **Daily:** Acompanhamento do progresso.
* **Review:** Validação das entregas.
* **Retrospectiva:** Melhoria contínua do processo.

---

### Objetivo Final
Desenvolver uma solução eficiente e escalável para tradução automática em Libras, garantindo fidelidade linguística, clareza visual, sincronização temporal e facilidade de integração.
