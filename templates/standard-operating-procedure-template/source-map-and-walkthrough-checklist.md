# SOP source map and walkthrough checklist

Original synthetic example; author manual paper walkthrough on October 18, 2026. Use with [the original notes, list L1 and corrected SOP](fictional-process-notes-and-filled-sop.md). This checks written logic. No filesystem task, model run, permission check, approval or distribution was performed.

## Source-to-action map

### Step 1 — obtain list and destination

**Original:** N1, “The coordinator supplies the current approved-file list and a destination packet folder.” L1 identifies the example list and folder.

**Role / input / result:** assistant receives coordinator's inputs; list orientation-list-A and destination Training/Packet-A identified. N1 supplies the inputs, not actual access or a required folder name.

### Step 2 — check source files before copying

**Original:** N3, “Before handoff, the assistant compares filenames and revision dates with the approved list.” N4, “If a listed file is missing or its revision differs, stop and ask the coordinator; do not substitute another version.” N1/L1 supply the list.

**Role / input / result:** assistant checks listed sources; each filename/revision matches, or stop. Checking before copying is a proposed ordering by the author. N3 itself requires the final comparison before handoff. Owner must review that proposal.

### Step 3 — copy listed files, preserving originals

**Original:** N2, “The assistant copies only listed files into the supplied folder without changing source files.”

**Role / input / result:** assistant uses matching listed files and supplied destination; listed copies present and originals unchanged. Source labels establish the instruction, not whether real copies or unchanged originals have been observed.

### Step 4 — compare packet before handoff

**Original:** N3, “Before handoff”; N2, “only listed files”; N4, “stop and ask the coordinator”.

**Role / input / result:** assistant compares packet/list filenames and revisions, checks for substitutes; matching packet or blocked handoff. The check does not verify document contents or confer approval.

### Step 5 — hand off location

**Original:** N5, “After checks, send the packet location to the coordinator, who handles distribution.”

**Role / input / result:** assistant gives checked location; coordinator handles distribution. N5 supports the handoff after checks. It supplies no approval authority, automatic distribution or acknowledgement requirement.

### Exception, access and policy gaps

**Missing / mismatch:** N4 blocks progress and prohibits substitution. Clarification contact: coordinator. Resume rule absent; keep UNKNOWN.

**Access:** no source establishes actual read/write permission. Resolve before use; do not count this as sourced access.

**Approval / naming / retention:** N5 explicitly leaves naming and retention unspecified, and none of N1–N5 supplies owner approval. Remove automatic approval and seven-day deletion. A folder label in L1 is not a general naming policy.

## Actual author paper walkthrough

The author followed the written steps mentally using the following stated fixtures, inspected each source relationship, and recorded these outcomes. No real files were opened, copied, compared or sent. These are paper observations rather than measured operational results.

### A — matching listed files

**Assumed paper state:** coordinator provides L1; both named source files are represented as present with revisions 2026-10-12 and 2026-10-14 respectively. Real access is outside this paper exercise.

**Trace:** step 1 identifies list/destination → step 2 matches both fixture entries → step 3 represents only those two copies, preserving originals → step 4 matches both packet entries, no substitute → step 5 gives location to coordinator.

**Observed written outcome:** sequence reaches location handoff. It supplies no approval receipt and performs no distribution. Actual access and owner decision still block operational adoption of this draft.

### B — missing second file

**Assumed paper state:** L1 unchanged; room-guide.txt absent at step 2.

**Trace:** step 1 identifies inputs → step 2 finds missing listed file → N4 stops. Do not enter step 3 or hand off a partial packet.

**Clarification question:** “room-guide.txt, revision 2026-10-14, is missing from the supplied source location. Please clarify the correct source and how to proceed.” This is a proposed question, not a sent message or new policy.

**Observed written outcome:** coordinator is the source-defined contact; no substitute or automatic restart follows. The draft contains no resume rule. Keep blocked pending clarification and owner decision about the procedure.

### C — wrong revision, including a late mismatch

**Assumed paper state:** L1 unchanged; room-guide.txt represented with revision 2026-10-13, whereas L1 requires 2026-10-14.

**Trace:** step 2 detects the different revision → N4 stops copying/handoff. Separately place the same discrepancy at step 4 after a hypothetical copy: N4 stops handoff there too.

**Clarification question:** “The room-guide.txt revision differs from the supplied list. Please identify the correct revision and clarify how to proceed.”

**Observed written outcome:** both check points route to stop/ask without substitution. No deletion, fallback version, approval or invented resume step appears.

## Reusable worksheet for your own process

Copy this block for every action, including imperative commands that a factual claim grid might omit:

```text
Step / action:
Role / actual access:
Required input:
Observable result:
Original source label AND exact excerpt:
Sequence basis: [Source instruction / proposal for owner review]
Exception and stop condition:
Clarifier / source-supported resume rule:
Gap or proposed correction:
Human decision / unresolved question:
```

Copy this block for each factual assertion:

```text
Exact claim:
Original source label AND exact excerpt:
Supported / conflicting / absent from supplied notes:
Limits of that source:
Human correction:
Final wording or unresolved question:
```

## Checklist before owner review

- [ ] All five primary inputs are nonempty, with original substantive notes.
- [ ] Complement receives the complete chosen draft, original excerpts, audience and purpose.
- [ ] Human compares the claim-grid findings with actual originals and makes edits.
- [ ] Every command, role, input, result, order and exception has a source or explicit proposal label.
- [ ] Matching, missing and mismatched cases are walked separately; record actual observations.
- [ ] Actual access, resume rules and all blocking inputs are resolved before use.
- [ ] Approval authority and owner decision are supplied, not inferred from a distribution role.
- [ ] No naming, retention, deletion, timing or permission rule has been invented.
- [ ] Owner reviews the proposed order and confirms the draft's accuracy before operational use.

Owner name: UNKNOWN
Decision / date / conditions: PENDING
Operational use authorized by this example: NO
