# Skills

A **Skill** is a repeatable, reusable expert work package. It bundles instructions, templates, and (later) scripts for a recurring task.

## Status (v0.1.0)
- **No skill packages are implemented.**
- This folder contains candidates only (`skill-candidates.md`).
- Concrete `SKILL.md` definitions, scripts, and metadata land in v0.2.0+.

## Relationship to Other Pieces
| Piece | What it is | Lifespan |
|---|---|---|
| **Command** | Standard execution button (this folder's siblings). | Per task. |
| **Skill** | Packaged know-how for recurring work. | Reusable across tasks/projects. |
| **Subagent** | Context-isolated executor. | Per invocation. |

A command may *invoke* a skill; a skill may run inside a subagent.

## Authoring Standard (when implementation begins)
Each skill will have:
- A short trigger description (when Claude should use it).
- Inputs / Outputs / Acceptance Criteria.
- A clear scope: this is what the skill does, this is what it does NOT.

See `skill-candidates.md` for the v0.1.0 candidate list.
