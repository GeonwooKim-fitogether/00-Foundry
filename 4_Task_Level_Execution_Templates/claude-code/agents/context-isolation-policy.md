# Context Isolation Policy

How the main agent passes context to subagents and ingests their results without polluting itself.

## Pass-In: What a Subagent Receives
- **The question or AC**, stated narrowly.
- **A path allowlist** — explicit files or globs the subagent may read.
- **Output shape** — what the return must look like (table? 1-paragraph? citations only?).
- **Hard limits** — token budget, file count, depth.

## Pass-In: What a Subagent Does NOT Receive
- The entire `NPI_Brief` unless directly relevant.
- Memory dumps from prior conversations.
- Other subagents' raw outputs.
- Project-wide ontology unless the task is about ontology.

## Return: What the Subagent Sends Back
- **Decision-ready summary**, not raw transcript.
- **Citations** (`file:line`, source URL) instead of quoted blocks.
- **Confidence** marker per claim where uncertainty matters.
- **Open questions** at the end (if any), not buried.

## Return: What the Main Agent Does With It
- Quote only the summary into BuildLog or downstream commands.
- Discard the raw transcript from active context once the summary is captured.
- If the summary is insufficient, **re-ask** with a sharper brief — do not pull the raw transcript back.

## Context Budgeting Rules
- The main agent should aim to keep working context under the noise threshold for the current step.
- When approaching the limit, prefer (in order): **drop** stale context → **summarize** large blobs → **delegate** to a subagent.

## Memory vs. Context
- **Memory** (persistent, file-based): durable user/project facts, feedback, references.
- **Context** (current conversation): only what's needed for the current step.
- Do not write transient task state to memory; do not rely on memory for what should be in the Brief.

## Anti-patterns
- Streaming a subagent's full transcript back into main context.
- Subagents reading "everything just in case".
- Treating main context as a junk drawer of every doc the agent has ever opened.
