## A meeting-minutes template you can use immediately

Useful meeting minutes record decisions, actions, and open questions so someone who missed the meeting can see what happens next. Download the editable template below, fill it from your notes, and verify each decision before sharing. You can use it manually without an AI account.

For longer notes, **[get Meeting Notes to Decisions and Action Items on TokRepo](https://tokrepo.com/en/workflows/meeting-notes-decisions-action-items-e0ccfa90?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=meeting-minutes-template)**. It is the primary prompt asset for organizing evidence from your notes. The complementary [DOCX asset](https://tokrepo.com/en/workflows/claude-official-skill-docx-word-document-creation-6236da40?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=meeting-minutes-template) helps an appropriately configured agent turn the approved draft into a Word document. Formatting comes after fact checking.

| Asset | Role | Handoff |
| --- | --- | --- |
| Meeting Notes to Decisions and Action Items — primary | Draft decisions, actions, and unanswered questions from supplied notes | Notes → evidence-linked draft |
| DOCX — secondary | Create a readable Word document using its supported workflow | Approved draft → formatted minutes |

## Download the template and example

Use the [blank Markdown template](../../templates/meeting-minutes-template/meeting-minutes-template.md), [Word template](../../templates/meeting-minutes-template/meeting-minutes-template.docx), and [filled fictional example](../../templates/meeting-minutes-template/filled-example.md). The Word template is editable in a compatible word processor. The text version works as a starting point for Google Docs or your preferred notes app; inspect table formatting after pasting.

The template includes meeting details, a short outcome summary, a decisions table, an action register, and unresolved questions. Delete unused sections rather than filling them with invented information.

## Fill the record from evidence

First record the meeting date, purpose, attendees, and note taker if those details are known. Next identify what was actually agreed. “We might launch in May” is a proposal, not a decision; “We agreed to review the draft on May 6” can be a decision when the notes support it.

For each action, write an observable task, an owner, a due date, and a source reference. Use `UNKNOWN` when the owner or date is absent. A line number, paragraph, or timestamp helps a reviewer find the statement quickly. Keep conflicting accounts in open questions instead of choosing whichever sounds cleaner.

In the fictional example, Maya agrees to prepare an outline by October 12. The launch date remains undecided. Good minutes preserve that difference; they do not convert the outline deadline into a launch commitment.

## Use the TokRepo prompt for a draft

Open the primary asset, obtain its prompt, and follow its usage instructions with notes you are allowed to share with your chosen assistant. Keep the source notes alongside the result. The prompt's expected sections are a draft to inspect, not an authoritative meeting record.

Review each proposed decision and action against the original text. Remove unsupported owners, dates, and claims. Ask participants to resolve material ambiguity rather than asking the assistant to guess. No transcript or personal notes are uploaded through this static recipe page; any external assistant has its own data handling and access requirements.

After approval, use the DOCX asset only if you need its agent-based document workflow. It may require its documented runtime and tooling. Downloading the blank Word template does not require installing that asset or setting up an agent.

## Check before sharing

Every decision should be supported by a source note. Each action needs an owner and date or an explicit unknown. Separate proposals from commitments, verify names, and keep the document's review status visible. Check that the final Word copy retains all rows and does not lose unresolved questions during formatting.

**How detailed should minutes be?** Include enough context to understand decisions and follow-up; a full transcript is a different deliverable. Use links or references when the discussion detail matters.

**Can this be used for a formal board meeting?** This is a general working-meeting template. Formal organizations may require a specific process or format; use their approved requirements rather than assuming this template satisfies them.

For recurring meetings, keep the [primary TokRepo asset](https://tokrepo.com/en/workflows/meeting-notes-decisions-action-items-e0ccfa90?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=meeting-minutes-template) as the reusable note-processing step, then apply the same approval checks every time. The [official DOCX skill source](https://github.com/anthropics/skills/tree/main/skills/docx) documents the optional formatting workflow.
