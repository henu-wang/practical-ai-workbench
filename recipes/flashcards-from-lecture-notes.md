## Quick answer

Make flashcards from lecture notes by turning one source-backed idea into one question, putting a short answer on the back, and keeping a reference you can check. Start with one section rather than converting an entire notebook into hundreds of cards. Missing information should become a question to resolve, not an answer to memorize.

Get the complete [Lecture Transcript to Study Cards asset on TokRepo](https://tokrepo.com/en/workflows/turn-lecture-transcript-into-study-cards-585e76f2?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=flashcards-from-lecture-notes). It supplies the reusable card-generation prompt. If your source is recorded audio, combine it with [Whisper](https://tokrepo.com/en/workflows/whisper-openai-speech-text-eb0f9dd6?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=flashcards-from-lecture-notes) to obtain a transcript first. Written notes do not need Whisper.

## Download a small worked example

- [Example lecture excerpt](../../templates/flashcards-from-lecture-notes/lecture-excerpt.md), with line references.
- [Card-planning brief](../../templates/flashcards-from-lecture-notes/card-planning-brief.md), for your own source.
- [Four source-backed cards](../../templates/flashcards-from-lecture-notes/cards.tsv), as a two-column TSV.
- [Gap log and review plan](../../templates/flashcards-from-lecture-notes/review-plan.md).

The example is original, manually written, and checked against the excerpt. It is not a generated deck or a claim that an assistant was run. The TSV structure is checked; an Anki application import has not been exercised for this example.

## 1. Prepare a source you can verify

Number paragraphs or use transcript timestamps. Keep definitions and examples together, but separate scheduling announcements from study material. Preserve the original so you can investigate a card whose answer sounds plausible but was never taught.

For an audio lecture, use the Whisper asset's linked setup instructions, then listen to relevant passages while correcting names, technical terms, and numbers. A transcription can be wrong; converting its mistakes into cards makes those mistakes harder to notice.

The TokRepo card prompt is designed for transcripts. Using typed lecture notes is an adaptation: paste the notes as the source text, keep paragraph anchors, and explicitly tell the assistant not to supply missing context. This adaptation has not been runtime-tested. Check whether your course allows sharing lecture material with an external assistant before doing so.

## 2. Choose an atomic question

Our excerpt defines observation, inference, and hypothesis. A weak card asks, “Explain the whole scientific process.” A useful card asks, “What does this unit call an observation?” Its answer points directly to line L1.

| Front | Back | Check |
| --- | --- | --- |
| What does this unit call an observation? | A recorded result or event. | L1 |
| What is an inference in this unit? | An explanation drawn from observations. | L2 |
| What makes a hypothesis checkable? | It is a claim that can be checked against new observations. | L3 |
| In the pavement example, what is observed and what is inferred? | Wet pavement is observed; rain as its cause is inferred. | L6 |

These wording choices are scoped to the excerpt. They do not pretend to replace a textbook definition or prove a study technique improves exam scores.

## 3. Preserve gaps and ambiguity

The excerpt does not define “controlled variable.” Put that item in the gap log and locate the assigned source before making its answer. Do not add a familiar definition from memory and label it as lecture-derived.

If two source statements conflict, keep both references and flag the card for review. If the back needs a paragraph to answer several separate questions, split the card. A date about tomorrow's room change is useful planning information, but not necessarily material for a study deck.

## 4. Import a few cards, then review

The downloadable TSV has no header: first column is the question, second is the answer with its source anchor. For an Anki Basic note, choose tab separation and map the two columns to Front and Back. Preview the fields before importing, especially if you edit the file in a spreadsheet. Use UTF-8 and keep literal tabs or line breaks out of individual fields. See [Anki's official text-import instructions](https://docs.ankiweb.net/manual/importing/text-files).

Before importing, check Anki's duplicate-handling settings: a matching first field can update an existing note of the same type. Use a separate profile for a trial if you need to protect an existing deck.

Try recalling the answer before turning the card over. Compare the back with its source, then revise confusing wording. The suggested review days are a starting plan, not a validated scheduling algorithm; use your study application's settings and your course timeline.

When the small set is useful, retrieve the [full source-constrained card prompt](https://tokrepo.com/en/workflows/turn-lecture-transcript-into-study-cards-585e76f2?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=flashcards-from-lecture-notes) and apply the same checks to the next section. Scale the source checking along with the card count.
