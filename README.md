# Projeto de Geração Automática de Libras com IA

## Visão Geral

Este projeto é desenvolvido no contexto da Residência Tecnológica **GrowUp**, do Porto Digital, em parceria com a Globo (Rio de Janeiro).

O objetivo é criar um sistema capaz de gerar automaticamente traduções em Libras a partir de vídeos, utilizando técnicas de inteligência artificial.

A solução é estruturada como um pipeline de processamento que integra extração de áudio, transcrição com marcação temporal, conversão para Libras e exibição com avatar, permitindo a disponibilização de conteúdos acessíveis em escala.

---

## Organização do Projeto (Trello)

O gerenciamento das atividades é realizado por meio de um quadro no Trello, estruturado para refletir o fluxo de desenvolvimento e facilitar a colaboração entre as equipes.

### Estrutura do Quadro

O fluxo de tarefas é organizado nas seguintes etapas:

- **Backlog Geral**  
  Lista de todas as tarefas do projeto, incluindo funcionalidades futuras e melhorias.

- **Sprint Atual**  
  Tarefas selecionadas para desenvolvimento no ciclo atual.

- **Em andamento**  
  Atividades em desenvolvimento.

- **Em revisão**  
  Código finalizado aguardando validação técnica.

- **Testes**  
  Validação funcional e verificação de integração entre componentes.

- **Integração**  
  Tarefas que envolvem comunicação entre diferentes equipes ou módulos.

- **Concluído**  
  Atividades finalizadas e validadas.

- **Bloqueado**  
  Tarefas impedidas por dependências externas ou problemas técnicos.

---

## Identificação das Equipes

As tarefas são classificadas por equipe utilizando labels:

- **Grupo 1 — Processamento de Áudio e Vídeo**  
  Responsável pela extração, limpeza e segmentação do áudio.

- **Grupo 2 — Transcrição e Temporização de Fala**  
  Responsável pela conversão de áudio em texto e geração de timestamps.

- **Grupo 3 — Tradução para Libras e Geração de Avatar**  
  Responsável pela conversão do texto para Libras e integração com sistemas de avatar.

- **Grupo 4 — Interface e Exibição do Vídeo**  
  Responsável pela interface do usuário, reprodução do vídeo e exibição do avatar.

- **Integração**  
  Utilizado para tarefas que envolvem mais de uma equipe.

---

## Estrutura das Tarefas

Cada tarefa no Trello segue um padrão definido para garantir clareza e rastreabilidade.

# Estrutura de Tarefas (Trello)

Este documento define o padrão de criação e organização das tarefas no Trello, garantindo clareza, rastreabilidade e padronização entre as equipes.

---

## Padrão de Título

Todas as tarefas devem seguir o formato:

[G#] Nome da tarefa

Exemplos:
[G1] Extrair áudio do vídeo  
[G2] Gerar timestamps da transcrição  
[G3] Integrar API de tradução para Libras  
[G4] Implementar player de vídeo  

---

## Descrição da Tarefa

A descrição deve conter informações claras e objetivas:

- Objetivo da tarefa  
- Contexto (quando necessário)  
- Dependências (ex: outra equipe ou tarefa)  

---

## Checklist

Cada tarefa deve possuir um checklist com as etapas necessárias para sua conclusão.

Exemplo:

- [ ] Receber dados de entrada  
- [ ] Processar informação  
- [ ] Validar resultado  
- [ ] Testar funcionamento  

---

## Responsável

Toda tarefa deve ter pelo menos um responsável definido.

---

## Labels

As tarefas devem ser identificadas com labels de acordo com a equipe:

- Grupo 1 — Processamento de Áudio e Vídeo  
- Grupo 2 — Transcrição e Temporização de Fala  
- Grupo 3 — Tradução para Libras e Geração de Avatar  
- Grupo 4 — Interface e Exibição do Vídeo  
- Integração — tarefas que envolvem mais de uma equipe  

---

## Critérios de Conclusão

Uma tarefa só pode ser movida para "Concluído" quando:

- Todas as etapas do checklist forem finalizadas  
- O código estiver revisado (quando aplicável)  
- Testes forem realizados com sucesso  
- Integrações necessárias estiverem validadas  

---

## Boas Práticas

- Dividir tarefas grandes em tarefas menores  
- Evitar descrições vagas  
- Atualizar o status da tarefa constantemente  
- Registrar bloqueios quando existirem  
- Garantir alinhamento com outras equipes quando necessário  

---

## Metodologia

O projeto adota uma abordagem baseada em Scrum, com os seguintes ritos:

- **Planning:** definição das tarefas da sprint  
- **Daily:** acompanhamento do progresso  
- **Review:** apresentação das entregas  
- **Retrospectiva:** identificação de melhorias no processo  

---

## Objetivo

Estabelecer uma organização clara e eficiente para o desenvolvimento de um sistema distribuído entre múltiplas equipes, garantindo qualidade, integração e evolução contínua da solução.
