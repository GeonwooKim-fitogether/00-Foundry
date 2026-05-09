# Agents (Main Agent + Subagents)

## Subagent Principles (must-read)

1. **A subagent is not a person — it is a context-isolated specialist.** Treat it as a sealed room with a narrow brief, not a colleague who shares your memory.
2. **Subagents exist to keep the main context clean.** Their primary job is to absorb noise (long files, search results, failing logs) and return a small, decision-ready answer.
3. **Do not split every task into subagents.** Most work belongs in the main agent. Spawning a subagent has cost: brief drafting, context handoff, summary parsing.
4. **Use a subagent when context pollution is the bigger risk.** Typical fits:
   - Large-scale codebase exploration / "where is X defined".
   - Risk review across many files.
   - Test-failure diagnosis with long stack traces and logs.
   - Parallel evaluation of independent options.
   - Background research with many sources.
5. **Subagents receive only the context they need.** Do not pass them the whole project. Pass: the question, the relevant paths, the AC, and the expected output shape.
6. **Subagent output is decision-ready summary, not raw transcript.** The main agent should never need to re-read the subagent's source material to act.

## Anti-patterns
- Spawning a subagent for a 10-line question.
- Asking a subagent to "do the whole task" — that defeats orchestration.
- Letting a subagent's full transcript flow back into main context.
- Running parallel subagents on overlapping work without a merge plan.

## Files
- `agent-candidates.md` — concrete agent roles for v0.1.0.
- `context-isolation-policy.md` — what context to pass, what to withhold, how to ingest results.
