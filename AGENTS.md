# Editorial agents

This project is a working open-source task utility and an English search landing site. Read these shared contexts before work:

1. `team/context/USER-BRIEF.md`, `PROJECT.md`, `AUDIENCE.md`, `ASSET-POLICY.md`.
2. `tasks.json`, `team/research/demand.json`, `team/ledger.json` and relevant page sources.
3. `team/PIPELINE.md`, `STYLE.md`, `QUALITY.md` and the latest relevant review records.

The user explicitly requested an editorial agent team. In a runtime with collaboration tools, use independent sub-agents for demand research, writing/building and quality review. Pass only the shared context and assigned responsibility; define file ownership and remind each agent that other contributors are present. The author must not approve its own work. The managing editor integrates findings and the release editor publishes only the reviewed source.

Role prompts live in `team/roles/`. These are executable instructions for the orchestrator to pass to agents, not a claim that GitHub hosts an LLM service. The daily orchestrator runs in the authorized Codex chat. GitHub Actions runs deterministic code/build checks and does not require model credentials.

Use fresh, original evidence for a task. Prefer new useful capabilities and meaningful task packs; update existing canonical pages rather than generating near-duplicates. A generic keyword with unmet intent is not an acceptable page. Do not increase the daily cap to compensate for skipped runs.

Run `npm test`, `python3 scripts/build.py`, `python3 scripts/browser_check.py`, and `python3 scripts/editorial_gate.py` before publishing relevant changes. The browser script requires Python Playwright, Pillow and Chrome. Capture real output. If a required test environment is missing, preserve drafts and report the missing check without filling in a fake PASS.

Preserve input files. No third-party request may contain user file contents. Vendor browser dependencies with their licenses. Keep secrets and local profiles out of Git. Public data examples are synthetic. Source and UI changes invalidate affected source-hash review approvals.
