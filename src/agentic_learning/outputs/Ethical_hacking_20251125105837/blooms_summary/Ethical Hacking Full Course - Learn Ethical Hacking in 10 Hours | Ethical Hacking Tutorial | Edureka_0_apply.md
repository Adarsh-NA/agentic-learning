# Applied Exercises: *Transcript not available* (concepts & application)

Use the transcription chunk: `Transcript not available`. These exercises train practical decision-making, documentation, and workflow design when encountering missing transcripts. Work through the Wh-questions, MCQs, and scenario-based tasks below. Where data is missing, use empty placeholders (`""`, `null`, or `<placeholder>`).

---

# 1. Wh-Questions (Why/Who/What/How/When/Where/Which)

Answer each question in writing, using examples where useful.

- Why might a chunk be labeled `Transcript not available`? List at least five distinct causes and explain how you'd detect each.
- Who should be notified or assigned when you encounter `Transcript not available` in a compliance-critical dataset?
- What immediate checks should you run to triage a missing transcript? Provide a checklist in order.
- How would you decide between running ASR and commissioning a human transcription for this chunk?
- When is it inappropriate to attempt to recreate a transcript (even if audio exists)?
- Where in your data catalog or metadata model should the `Transcript not available` status be recorded?
- Which metadata fields are essential to capture when logging a missing-transcript event? Explain why each is necessary.
- Why is provenance important for a chunk marked `Transcript not available`? Give two examples of problems that provenance prevents.
- How would you document that a reconstructed transcript was *inferred* (not verbatim)?
- Who is responsible for verifying the quality of an ASR-generated provisional transcript in your organization?
- What legal or consent checks must be performed before running ASR on an audio file that produced `Transcript not available`?
- How would you prioritize multiple missing-transcript chunks across a large corpus for remediation?
- When should you add a permanent `redacted` note instead of attempting transcription?
- Which mnemonics (e.g., NAPRC, CAPTD, TRACE, SAFE, CLEAR) apply to your workflow, and how would you integrate them into your SOP?
- What metrics would you track to measure improvements in handling `Transcript not available` events (e.g., mean time to restore, percent resolved)?
- How would you explain to an end user (non-technical) why the transcript is unavailable and what they can do next?
- Which stakeholders need to sign off before attempting human transcription of recorded meetings containing sensitive information?
- How would you use neighboring transcript chunks to infer missing content while minimizing risk of misinformation?
- What technical remediation steps can you try if ASR fails due to noisy audio?
- How would you version and store a transcript that was created after the `Transcript not available` event?
- Which automated alerts or dashboards would you build to surface recurrent `Transcript not available` issues?
- When training an ML model with transcripts, how should you treat chunks labeled `Transcript not available`?
- How would you redact a transcript to remove PII and still keep an informative summary for users?
- What ethical concerns arise if you use third-party transcription services for sensitive audio labeled `Transcript not available`?
- How would you audit a past incident where many chunks were labeled `Transcript not available` with no follow-up?

---

# 2. Multiple-Choice Questions (MCQs)

Choose the best answer. Answers are provided in the Answer Key section.

1. `Transcript not available` most directly indicates:
   - A) The audio file is corrupted
   - B) The text representation of the audio is missing
   - C) The audio contains no speech
   - D) The audio is in a foreign language

2. Which acronym lists likely causes of a missing transcript?
   - A) SAFE
   - B) CAPTD
   - C) NAPRC
   - D) TRACE

3. CAPTD stands for:
   - A) Check, Analyze, Protect, Transcribe, Document
   - B) Capture, Audit, Persist, Translate, Deliver
   - C) Confirm, Access, Process, Test, Deploy
   - D) Create, Approve, Publish, Tag, Delete

4. Before attempting transcription, which gating acronym reminds you to check privacy/permission constraints?
   - A) TRACE
   - B) CLEAR
   - C) SAFE
   - D) NAPRC

5. When using ASR as a provisional step, you should:
   - A) Publish the transcript and remove the `Transcript not available` label without annotations
   - B) Include confidence scores and mark the transcript as provisional
   - C) Always accept ASR output as final
   - D) Never show ASR output to end users

6. Provenance metadata should include:
   - A) Who created or modified the transcript
   - B) Which ASR model or human transcriber was used
   - C) Timestamps of actions and notes about errors
   - D) All of the above

7. A chunk is intentionally labeled `Transcript not available` due to redaction. Correct next action:
   - A) Attempt to run ASR anyway
   - B) Request speaker notes from anyone
   - C) Respect redaction and document reason; do not transcribe
   - D) Publish inferred content from neighboring chunks

8. Which is a recommended threshold approach for deciding when ASR output is acceptable without human review?
   - A) Use average segment confidence above an agreed threshold (e.g., >0.85)
   - B) Randomly sample words for manual check
   - C) Always require human review
   - D) Use length of audio as the only factor

9. Which metadata field best captures the reason for absence?
   - A) `status`
   - B) `cause`
   - C) `audio_exists`
   - D) `last_checked`

10. When reconstructing inferred content from neighbors, what must you always do?
    - A) Edit inferred content into the original transcript without note
    - B) Mark inferred segments as such and include confidence level
    - C) Replace the chunk entirely with your inference
    - D) Delete the neighboring chunks for consistency

---

## Answer Key (MCQs)

1. B
2. C
3. A
4. C
5. B
6. D
7. C
8. A
9. B
10. B

---

# 3. Scenario-Based Exercises

For each scenario, perform the requested tasks. Provide written answers, annotated templates, or code/JSON where asked.

Beginner — Identification & Logging

Scenario 1:
- You see `Transcript not available` for chunk ID `"<chunk_001>"`. Audio is listed in the catalog but you get a `ASR_TIMEOUT` error in logs.
  - Tasks:
    - List the immediate three actions (one-line each).
    - Fill the quick documentation template with placeholders.

Quick documentation template (fill with empty strings where unknown):

```text
- Chunk ID / Timestamp: "<chunk_001>"
- Original status: "Transcript not available"
- Audio/video present? (Yes / No / Unknown): "Yes"
- Likely cause (if known): "ASR_TIMEOUT"
- Actions taken:
  - Metadata/log checks (summary): ""
  - ASR attempt (Yes/No) — if yes, tool, date, confidence summary: ""
  - Human transcription requested (Yes/No): ""
- Outcome: ""
- Notes and provenance: ""
- Next steps: ""
```

Scenario 2:
- A user complains they cannot access transcript for a training module. Legal team indicates parts may be redacted.
  - Tasks:
    - Draft a one-paragraph user-facing message explaining `Transcript not available` and next steps.
    - Indicate which internal stakeholders to escalate to.

Intermediate — Decision-making & Workflow

Scenario 3:
- You manage a dataset for model training. 7% of chunks show `Transcript not available`. Audio exists for most. The model is sensitive to transcription errors.
  - Tasks:
    - Propose a remediation plan prioritizing chunks (three criteria and rationale).
    - Suggest whether to exclude or impute these chunks from training; justify.

Scenario 4:
- ASR yields a transcript with many low-confidence segments (average confidence 0.62). The content is non-sensitive and used for search indexing.
  - Tasks:
    - Decide: accept ASR as provisional or request human review? Explain with a short policy (2–4 bullets).
    - Draft how to present this transcript in the UI (one or two sentences) including a disclaimer.

Scenario 5:
- The `Transcript not available` cause is `permission_denied` in metadata for chunk `"<chunk_045>"`. A researcher requests access.
  - Tasks:
    - Draft the permission checklist the researcher must satisfy.
    - Write a short provenance log entry (use JSON code block) to record the access decision (use empty values where pending).

Example provenance JSON:

```json
{
  "chunk_id": "<chunk_045>",
  "status": "transcript_not_available",
  "cause": "permission_denied",
  "audio_exists": true,
  "requested_by": "",
  "requested_at": "",
  "decision": "",
  "notes": ""
}
```

Advanced — Ethics, Automation, & Design

Scenario 6:
- A platform displays `Transcript not available` with no reason. This causes user frustration and repeated support tickets.
  - Tasks:
    - Redesign the UI message to be informative while respecting privacy; include three optional user actions (buttons or links).
    - List the metadata keys your backend must return to drive that UI.

Scenario 7:
- ASR service fails on many files due to background noise. Propose an automated CAPTD-style pipeline (pseudocode) that:
  - Checks audio, evaluates permission, tries noise-reduction, retries ASR, and triggers human transcription if retries fail.
  - Provide the pseudocode block (concise, clear comments).

Scenario 8:
- You must train a quality-control auditor to decide when an ASR transcript is acceptable. Create a 5-item checklist they will use, including numeric thresholds and documentation requirements.

Scenario 9:
- You find a previously reconstructed transcript that was not labeled as such and now is in production. Outline a remediation plan (5 steps) to correct the record and assess downstream impacts.

Scenario 10:
- Privacy law requires that certain personal data be redacted before any transcription. Describe an automated pre-check flow (step-by-step) that prevents unapproved transcription and logs the event.

Creative/Application — Build & Implement

Scenario 11:
- Create a JSON schema (concise) for storing `transcript_status` metadata that captures status, cause, timestamps, allowed actions, and provenance. Use empty strings/booleans where values are not known. Provide an example JSON instance with placeholders.

Example schema (simplified) and instance:

```json
{
  "chunk_id": "<chunk_id>",
  "status": "transcript_not_available",
  "cause": "<not_requested|asr_failed|permission_denied|redacted|corrupted|pending>",
  "audio_exists": true,
  "last_checked": "",
  "error_code": "",
  "allowed_actions": ["retry_asr", "request_human", "request_notes"],
  "provenance": {
    "logged_by": "",
    "logged_at": "",
    "notes": ""
  }
}
```

Scenario 12:
- Design a short escalation policy (3 levels) for unresolved `Transcript not available` cases older than 7 days. Include triggers to escalate and responsible roles.

---

# 4. Suggested Answers / Rubric Highlights

Use this as guidance when reviewing learner responses.

- For Wh-questions: look for use of NAPRC causes, CAPTD actions, SAFE checks, TRACE provenance items.
- MCQs: correct answers in Answer Key above.
- Scenario rubrics:
  - Beginner responses should contain immediate triage steps: check audio, inspect logs, verify permissions.
  - Documentation template must include chunk ID, status, audio existence, cause, actions taken, and next steps.
  - Intermediate: remediation plans should prioritize criticality, frequency of use, or legal exposure. For training datasets, recommended to exclude unknown or low-confidence chunks or flag them with metadata.
  - Advanced: pipeline pseudocode should include permission gating, retry logic, noise reduction invocation, confidence evaluation, and escalation to human transcription with provenance logs.
  - JSON schema should include the keys shown in Scenario 11 and be extensible for `allowed_actions`, `error_code`, and provenance.

Example short answers:
- Immediate three actions (Scenario 1): (1) Confirm audio file exists and playable; (2) Inspect ASR logs for `ASR_TIMEOUT` details and timestamp; (3) Retry ASR or schedule human transcription based on criticality.
- UI message (Scenario 2): *"The transcript for this module is currently unavailable due to partial redaction. Contact training-administrator@example.com to request an excerpt or summary. If you need full access for accommodation, submit a request."* Escalate to Legal + Training Content Owner + Accessibility Team.
- CAPTD pseudocode (Scenario 7): see below.

Pseudocode example (compact):

```python
def handle_missing_transcript(chunk):
    meta = fetch_metadata(chunk)
    if not meta["audio_exists"]:
        log("No audio; notify content owner")
        return
    if not has_permission(meta):
        log("Permission denied; flag and document")
        return
    # Try ASR with preprocessing
    enhanced_audio = noise_reduction(meta["audio_path"])
    asr_result = run_asr(enhanced_audio)
    if asr_result["avg_confidence"] >= 0.85:
        save_transcript(asr_result, provisional=True)
    else:
        # Retry or escalate
        if meta["retry_count"] < MAX_RETRIES:
            meta["retry_count"] += 1
            schedule_retry(chunk)
        else:
            request_human_transcription(chunk)
    document_action(chunk, meta, asr_result)
```

---

# 5. Fill-in & Practice Templates (Use these in exercises)

- Quick log entry (plain text):

```text
Chunk ID / Timestamp: "<chunk_XXX>"
Status: "Transcript not available"
Audio exists: "Yes"
Cause: "<asr_failed|permission_denied|redacted|not_requested|corrupted>"
Action(s) taken: "<run_asr|request_human|none>"
Outcome: ""
Reviewer: ""
Review date: ""
Notes: ""
```

- Minimal UI copy examples (pick one):
  - Informative, non-sensitive: *"Transcript not available — we attempted automatic transcription but some segments failed. [Retry transcription] [Request human review] [View audio]"*
  - Privacy-preserving: *"Transcript not available — access restricted. Request permission or contact support."*

- Gap documentation snippet (for dataset):

```text
"transcript_status": {
  "chunk_id": "<chunk_012>",
  "status": "transcript_not_available",
  "cause": "asr_failed",
  "last_checked": "2025-11-25T00:00:00Z",
  "allowed_actions": ["retry_asr", "request_human"],
  "notes": "ASR crashed on heavy background music"
}
```

---

# 6. Extension Activities (for instructors/trainers)

- Ask learners to implement the CAPTD pipeline in a sandbox with mock metadata and simulated ASR responses. Evaluate logs, provenance, and UI changes.
- Create a role-play where learners act as product manager, legal counsel, transcriber, and accessibility user and resolve a redaction + missing transcript case.
- Have learners audit a small dataset and produce a remediation report (priority list, actions taken, and post-remediation metrics).

---

# 7. Quick Reference Mnemonics (for learners)

- NAPRC — Causes: No transcript / ASR failed / Permission / Redaction / Corruption
- CAPTD — Actions: Check / Analyze / Protect / Transcribe / Document
- SAFE — Gating: Security / Authorization / Fairness / Exposure
- TRACE — Provenance checks: Timestamp / Reason / Access / Creation history / Error logs
- CLEAR — Handling quality: Complete docs / Legal / Ethical / Accuracy / Recoverability

---

If you want, I can:
- Generate printable worksheets for each scenario with space for answers.
- Produce automated unit-testable pseudocode for the CAPTD workflow.
- Create a short quiz (with timer and scoring) based on the MCQs above.