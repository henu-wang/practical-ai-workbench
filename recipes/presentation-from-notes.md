## Quick answer

Turn notes into a presentation by deciding the audience and the decision first, grouping the notes into one message per slide, then checking an editable deck against the source. The useful intermediate result is an approved outline—not six paragraphs pasted onto six slides.

Start with [the reusable writing brief on TokRepo](https://tokrepo.com/en/workflows/reusable-draft-final-writing-prompt-3128c956?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=presentation-from-notes), then use [the PPTX presentation skill](https://tokrepo.com/en/workflows/claude-official-skill-pptx-powerpoint-presentations-01b1713e?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=presentation-from-notes) to build from the reviewed outline. The first asset helps define what to say; the second provides the deck-creation workflow. This page supplies an original planning template and worked example; the complete reusable assets stay on TokRepo.

## Download the planning pack

- [Presentation brief](../../templates/presentation-from-notes/presentation-brief.md): audience, purpose, constraints, source notes, and output checks.
- [Example source notes](../../templates/presentation-from-notes/source-notes.md): a fictional onboarding proposal.
- [Six-slide example outline](../../templates/presentation-from-notes/six-slide-outline.md): each message mapped to a source note.
- [Deck review checklist](../../templates/presentation-from-notes/deck-review-checklist.md): fact, sequence, layout, and sharing checks.

These are editable Markdown documents, not an uploaded-notes-to-PowerPoint service. You can also copy the outline into a presentation editor manually. No finished PPTX or executed model output is claimed here.

## 1. Make the request specific

Fill in the brief before using the writing asset. “Make this look professional” leaves the audience and purpose unspecified. For our example, the audience is a small support team; the purpose is to approve a two-week onboarding experiment; the deck should have six slides and fit a five-minute conversation.

Label source notes `N1`, `N2`, and so on. Separate observed facts from proposals and unknowns. “Add a shared checklist” is a proposal, not an already implemented improvement. A percentage improvement with no source belongs in the missing-information list, not a chart.

Provide only material you are allowed to share with the assistant. Check its data-handling terms before pasting client notes. The guide's downloads are fictional examples, not private business data.

## 2. Review an outline before generating slides

Use the writing brief asset to request slide messages, supporting evidence, and speaker notes. Keep detailed explanations in speaker notes so the slides remain readable. If an item cannot be traced to the source, mark it as an open question or remove it.

Our six-slide example makes this structure visible:

| Slide | Main message | Source |
| --- | --- | --- |
| 1 | Approve a two-week checklist trial | N3, N4 |
| 2 | Current instructions are spread across three places | N1 |
| 3 | Repeated setup questions are the reported problem | N2 |
| 4 | Test a single checklist before broader change | N3 |
| 5 | Use the same question log to compare the trial | N5 |
| 6 | Confirm owner and review date before starting | N4, N6 |

Notice what the deck does not claim: a proven productivity gain, a financial return, or an assigned owner. The source does not establish those facts.

## 3. Turn the approved outline into an editable deck

Open the PPTX asset on TokRepo and follow its linked upstream instructions for your supported assistant and environment. Give it the approved outline, the source notes, any permitted brand template, and the required slide count. Ask for an editable `.pptx` and a list of assumptions.

Avoid blindly copying an installer command from an old article. The [current upstream PPTX skill](https://github.com/anthropics/skills/tree/main/skills/pptx) describes its creation and validation workflow; the environment must supply those capabilities. A writing prompt alone cannot create or verify a PowerPoint file.

## 4. Check the file you will actually share

Open the exported deck in your target presentation application. Verify all six slide messages against the outline, then check any number, name, deadline, and source reference. Inspect every slide for clipped text, overlaps, weak contrast, and fonts substituted by another computer.

Do not approve a deck from extracted text alone: correct words can still overflow. If the audience needs PDF, export it and inspect that version too. Save the editable deck, original notes, and review checklist together.

For your next presentation, reuse the [TokRepo writing brief](https://tokrepo.com/en/workflows/reusable-draft-final-writing-prompt-3128c956?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=presentation-from-notes) and [PPTX asset](https://tokrepo.com/en/workflows/claude-official-skill-pptx-powerpoint-presentations-01b1713e?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=presentation-from-notes). This walkthrough was manually checked against its fictional notes; the assistant-to-PPTX chain has not been run for this example.
