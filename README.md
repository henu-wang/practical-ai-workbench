# TokRepo Workflows

Practical English guides and editable templates that combine TokRepo prompts, skills and tools for common work and study tasks.

[Open the public workflows](https://henu-wang.github.io/practical-ai-workbench/)

The guides connect a searcher's task to the corresponding assets on TokRepo: audio transcription, meeting minutes, PDF tables, presentations, CSV cleaning and study flashcards. Each explains the combination, setup, result checks and limitations. This MIT-licensed project publishes original editorial material; linked assets and third-party tools retain their own licenses.

## Contribute

Edit `recipes/*.md`, original `templates/`, and `recipes.json`. Read `AGENTS.md` and the shared editorial context in `team/`. Research, authorship and independent review are separate responsibilities. Search-demand signals are qualitative; no search-volume or ranking claims are implied.

```sh
python3 -m pip install -r requirements.txt
python3 scripts/build.py
python3 scripts/recipe_check.py
python3 scripts/editorial_gate.py
python3 scripts/monitor_public.py --output /tmp/tokrepo-public-monitor.json
```

GitHub Pages publishes `main/docs`. Existing browser utilities keep their old URLs; they are no longer the publishing strategy. Their vendored dependencies and licenses remain included. Runtime changes to them require `npm ci --ignore-scripts`, `npm test` and `python3 scripts/browser_check.py`.

Indexing and growth are reviewed separately from deployment. See `team/MONITORING.md` and `team/context/METRICS.md` for the evidence-based follow-up protocol. No raw analytics account exports, credentials or private source documents belong in this repository.
