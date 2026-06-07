# Changelog

Todas as mudanças notáveis deste projeto serão documentadas aqui.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [Unreleased]

## [1.0.0] - 2026-06-06

### Added
- Exibição de status de conclusão dinâmico em format_task
- Separação de tarefas pendentes e concluídas em filter_tasks

### Changed
- format_task reformatada para exibir priority e title tratados
- filter_tasks reorganizada para retornar pendentes antes das concluídas

### Fixed
- Tratamento de campo title ausente em format_task
- Restauração da lógica de filtro em filter_tasks (hotfix)
