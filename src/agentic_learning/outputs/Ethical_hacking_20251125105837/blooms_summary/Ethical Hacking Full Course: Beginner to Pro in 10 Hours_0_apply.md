# Applied Exercises — Handling "Transcript not available"

The following applied exercises (Wh-questions, MCQs, and scenario tasks) are designed to deepen practical understanding of managing missing or unavailable transcripts. Use them individually or in groups. Where required, practice filling metadata templates — empty data types are shown as `null` or `""` to represent missing values.

---

## Section 1 — Wh-Questions (Why / Who / What / How / When / Where / Which)

Use these prompts for reflection, group discussion, or short-answer practice. They focus on reasoning and decision-making around missing transcripts.

- **Why** might a transcript be unavailable? List technical, legal, and human causes, and prioritize them by likelihood for your environment.
- **Who** should be notified when a transcript is missing? (e.g., data owner, legal, IT, stakeholders) Explain the rationale.
- **What** immediate evidence sources would you consult to compensate for a missing transcript? Rank them by reliability.
- **How** would you reconstruct missing content ethically and reproducibly? Describe the method, labeling, and provenance you would attach.
- **When** is it acceptable to proceed with downstream analysis without a transcript? What documentation must accompany that decision?
- **Where** in your data pipeline should a `transcript_status` field be recorded and enforced?
- **Which** reconstruction methods (human summary, ASR re-run, AI imputation, timeline reconstruction) are appropriate in (a) legal, (b) academic, and (c) product contexts?
- **Why** is it important to record `retrieval_attempts` and an audit trail when a transcript is missing?
- **Who** is responsible for deciding to escalate a missing transcript to legal/privacy teams?
- **What** metadata fields are minimally required when marking a transcript as missing? Provide an example list.
- **How** would you quantify and communicate uncertainty for reconstructed text?
- **When** should downstream automation be blocked because `transcript_status = "missing"`?
- **Where** could missingness introduce bias in analysis? Give two examples and mitigation steps.
- **Which** mnemonics (e.g., MISSING, REACT, BACKUP) apply to your organization's SOP? Propose one small policy change using one mnemonic.

---

## Section 2 — Multiple Choice Questions (MCQs)

Instructions: choose the best answer. Answers and brief explanations follow each question.

1. When you encounter a file labeled `Transcript not available`, the first practical action is to:
   - A) Immediately reconstruct the transcript using AI.  
   - B) Assume the content is lost and proceed.  
   - C) Confirm the transcript is truly missing by checking file paths, permissions, and backups.  
   - D) Publish a summary without labeling it.
   - **Correct:** C  
     - *Explanation:* First verify missingness and check accessible evidence before any reconstruction or publication.

2. Which metadata field is most important to add immediately when a transcript is missing?
   - A) `transcript_confidence`  
   - B) `transcript_status`  
   - C) `speaker_emotion`  
   - D) `word_count`
   - **Correct:** B  
     - *Explanation:* `transcript_status` (e.g., `"missing"`) is a fundamental flag that should be propagated.

3. If a transcript is missing because of legal restrictions, the appropriate action is:
   - A) Reconstruct immediately and redact if necessary.  
   - B) Attempt unauthorized access to recover it.  
   - C) Escalate to legal/compliance and follow policy; do not reconstruct until approved.  
   - D) Ignore and continue.
   - **Correct:** C  
     - *Explanation:* Legal constraints must be honored; escalate and follow established policy.

4. Which of the following best describes a non-deceptive reconstruction?
   - A) Replacing missing sections with best-guess text and not labeling it.  
   - B) Using participant summaries and labeling them explicitly as *reconstructed summary — not verbatim*.  
   - C) Removing the missing section entirely with no note.  
   - D) Inserting AI-generated verbatim text without provenance.
   - **Correct:** B  
     - *Explanation:* Reconstructed content must always be labeled and provenance recorded.

5. A useful mnemonic for actions on discovering a missing transcript is:
   - A) MISSING — Metadata matters; Identify cause; State status; ...  
   - B) FAST — Fake, Assume, Skip, Transfer  
   - C) HIDE — Hide Important Data Everywhere  
   - D) NONE
   - **Correct:** A  
     - *Explanation:* MISSING is a helpful, positive mnemonic for handling missing transcripts.

6. Which is the best gating rule for accepting ASR output automatically?
   - A) Accept all ASR outputs.  
   - B) Accept ASR output only if segment-level confidence >= threshold (e.g., 0.85) and label it.  
   - C) Never accept ASR outputs.  
   - D) Accept only if ASR runtime is < 1 second.
   - **Correct:** B  
     - *Explanation:* Use confidence thresholds and label machine-generated text for transparency.

7. What is a primary risk when reconstructing transcripts with AI?
   - A) AI will always be too slow.  
   - B) AI may hallucinate content and produce plausible but false statements.  
   - C) AI cannot format timestamps.  
   - D) AI removes metadata automatically.
   - **Correct:** B  
     - *Explanation:* Hallucinations are a known risk and must be mitigated by human validation and labeling.

8. Which metadata entry helps detect partial missingness (gaps inside a transcript)?
   - A) `speaker_list`  
   - B) `missing_intervals`  
   - C) `word_count`  
   - D) `language`
   - **Correct:** B  
     - *Explanation:* `missing_intervals` records time ranges that are absent.

9. In a high-stakes legal setting, reconstructed transcripts are:
   - A) Equally admissible as original transcripts if labeled.  
   - B) Generally inadmissible unless strict chain-of-custody procedures are followed.  
   - C) Never to be used, even for internal review.  
   - D) Preferred over original audio.
   - **Correct:** B  
     - *Explanation:* Legal admissibility requires strict procedures and provenance.

10. Which action reduces the probability of future `Transcript not available` events?
    - A) Single local copy on one device.  
    - B) Multi-channel recording, backups, integrity checks, and monitoring.  
    - C) Relying solely on human memory.  
    - D) Deleting raw audio after transcription.
    - **Correct:** B  
      - *Explanation:* Redundancy and monitoring reduce risk.

11. If you must proceed with analysis despite a missing transcript, you should:
    - A) Make assumptions silently to fill gaps.  
    - B) Document assumptions, label reconstructed content, and quantify uncertainty.  
    - C) Remove all references to the missing period.  
    - D) Replace gaps with random text to keep structure.
    - **Correct:** B  
      - *Explanation:* Transparency and documenting assumptions preserves credibility.

12. Which of these is an appropriate audit log entry for a failed ASR job?
    - A) `{"timestamp":"...","actor":"system","action":"asr_run","outcome":"timeout","job_id":"asr-123"}`  
    - B) `{"message":"stuff happened"}`  
    - C) `{"actor":"unknown"}`  
    - D) `{}`
    - **Correct:** A  
      - *Explanation:* Structured, timestamped logs with outcome and job IDs are essential.

---

## Section 3 — Scenario-Based Exercises (Applied)

Each scenario includes tasks and a checklist of expected actions/output. Use these for hands-on practice, role-playing, or assessment.

### Scenario 1 — Product Team: Transcription Job Timeout
You are the product analyst. A scheduled ASR job for yesterday's customer interviews failed. The UI displays `Transcript not available` for the interview.

Tasks:
- List the first 6 steps you will take (short bullet list).
- Fill the minimal metadata record (use the JSON template below; leave unknowns as `null`).
- Decide whether to re-run ASR immediately or escalate. Explain why.

Expected steps (example):
- Check storage path and job logs.
- Verify raw audio exists and play a short segment.
- Inspect ASR job ID and error (timeout/CPU).
- Check backups and previous exports.
- Set `transcript_status = "missing"` and append audit log entry.
- If audio quality is good, schedule ASR retry; if audio poor, request human transcription.

Example metadata template (fillable):
```json
{
  "transcript_status": "missing",
  "missing_intervals": [],
  "provenance": "ASR job timeout; audio present: true",
  "retrieval_attempts": 1,
  "last_checked": "2025-11-__T__Z",
  "reconstruction_method": null,
  "reconstruction_confidence": null,
  "access_restrictions": null,
  "audit_log": [
    {"timestamp":"2025-11-__T__Z","actor":"system","action":"checked_asr_job","outcome":"timeout,job_id:asr-___"}
  ]
}
```
Evaluation criteria:
- Checks file existence and quality.
- Documents actions in metadata/audit log.
- Reasoned decision about re-run vs manual transcription.

---

### Scenario 2 — Academic Researcher: Missing Interviews for a Paper
You planned to quote participants from recorded interviews. One interview transcript is missing but audio exists. The submission deadline is in 48 hours.

Tasks:
- Create a prioritized plan (recover, reconstruct, or postpone).
- Draft the exact inline annotation you would include in the paper if you must include a reconstructed quote.
- Describe how you would quantify confidence in the reconstructed quote.

Expected plan:
- Re-run ASR and attempt manual transcribe of the key quoted segment.
- If time-constrained, create a labeled reconstructed summary and quote only short verbatim pieces verified from audio.
- Add inline annotation: **[TRANSCRIPT STATUS: missing — quote reconstructed from audio by researcher; not verbatim; see audit_log entry ID: xyz]**
- Confidence: use `confidence_scale` (e.g., 0.65) based on audio quality and ASR/human agreement.

Evaluation criteria:
- Ethical labeling of reconstructed content.
- Clear provenance included.
- Reasoned confidence estimate.

---

### Scenario 3 — Legal Discovery: Redaction vs Missing
During discovery, some transcripts are marked `Transcript not available` for specific hours. Legal believes they might be intentionally withheld.

Tasks:
- Outline the steps to determine whether unavailability is technical or legal.
- Propose an escalation path and required evidence to support legal requests.

Checklist:
- Check access control lists and legal hold flags.
- Review process logs to see if deletion or redaction occurred.
- Interview custodian and IT; request audit trail.
- Escalate to in-house counsel with documentation showing checks and timestamps.

Evaluation criteria:
- Distinguishes technical failure from access-control decisions.
- Includes chain-of-custody and audit record gathering.

---

### Scenario 4 — Product UX: User Sees "Transcript not available"
Your application shows `Transcript not available` to end users. This hurts user trust.

Tasks:
- Propose three UX improvements and the underlying metadata or checks required to support each improvement.
- Provide example user-facing message wording for (a) temporary processing delay and (b) permanently unavailable due to privacy.

Example UX improvements:
- Show reason and ETA: "Transcript processing delayed — retrying (ETA ~10 min)". Requires backend job state and ETA estimate.
- Offer alternate access to audio: "Transcript not available — play audio". Requires audio playback link and access check.
- Explain privacy hold: "Transcript unavailable due to privacy restrictions — contact admin." Requires `access_restrictions` metadata.

Evaluation criteria:
- UX is transparent and actionable.
- Backend metadata fields align with messages.

---

### Scenario 5 — Data Governance: Define Policy
You must draft a short policy (5 bullets) for handling missing transcripts across the organization.

Tasks:
- Write the policy in 5 concise bullets.
- Add one enforcement mechanism.

Example policy bullets:
- Always set `transcript_status` to `"missing"`/`"partial"`/`"redacted"` when applicable.
- Log all retrieval attempts and ASR job outcomes to an immutable audit log.
- Do not publish reconstructed content without `reconstruction_method` and `reconstruction_confidence`.
- Block downstream publication if `access_restrictions` present until clearance.
- Run nightly integrity checks of recording/transcription pipelines and alert on failures.

Enforcement mechanism:
- CI pipeline fails production release if any published transcript lacks `transcript_status` and provenance fields.

Evaluation criteria:
- Policy is actionable, concise, and includes enforcement.

---

### Scenario 6 — Practical Exercise: Fill Metadata and Audit Log
Use the following skeleton and fill with realistic values based on an imaginary ASR failure. Leave unknowns as `null`.

Skeleton:
```json
{
  "transcript_status": "",
  "missing_intervals": [],
  "provenance": "",
  "retrieval_attempts": 0,
  "last_checked": "",
  "reconstruction_method": null,
  "reconstruction_confidence": null,
  "access_restrictions": null,
  "audit_log": []
}
```

After filling, write two short audit log entries: one for initial discovery and one for the first recovery attempt.

Evaluation criteria:
- Filled fields are consistent and plausible.
- Audit log entries are timestamped, actor-specified, and show outcomes.

---

## Section 4 — Short Practical Tasks (Active Learning)

- Task A: From your last project, identify any transcript files and check for `transcript_status`. If missing, add a minimal metadata entry (use YAML or JSON) and commit it to version control. Record the commit ID and describe next steps.

- Task B: Create a one-page checklist (based on REACT mnemonic) for frontline staff to follow when they see `Transcript not available`. Include one checkbox per step.

- Task C: Given a short audio clip with heavy noise, propose a hybrid workflow (ASR + human + QA) and specify acceptance thresholds and expected turnaround times.

- Task D: Design a dashboard widget that shows missing-transcript rates by team and month. Sketch the 3 metrics you would show and why.

---

## Section 5 — Answer Keys & Rubrics (Short)

- Wh-questions: Learner answers should show cause diagnosis, clear provenance plans, and explicit labeling.
- MCQs: Correct answers and explanations are provided above.
- Scenarios: Evaluation focused on completeness (did the learner: check audio, review logs, document audit trail?), ethical labeling (did they label reconstructed content?), and governance (did they escalate when appropriate?).
- Metadata exercise: Accept any valid ISO timestamps, sensible `retrieval_attempts` > 0, and audit entries with actor + action + outcome.

---

## Section 6 — Quick Reference Templates (for practice)

- Minimal metadata (YAML):
```yaml
transcript_status: "missing"          # "missing" | "partial" | "redacted" | "reconstructed"
missing_intervals: []                 # list of {start, end}
provenance: "ASR job timeout; audio present"
retrieval_attempts: 1
last_checked: "2025-11-__T__Z"
reconstruction_method: null
reconstruction_confidence: null
access_restrictions: null
audit_log:
  - timestamp: "2025-11-__T__Z"
    actor: "system"
    action: "asr_job"
    outcome: "timeout, job_id: asr-xyz"
```

- Example inline annotation for deliverables:
  - **[TRANSCRIPT STATUS: missing — no verbatim record available for timestamps 00:00–00:10; audio present but partially corrupted.]**
  - **[RECONSTRUCTED SUMMARY: derived from participant notes and audio fragments; not verbatim.]**

---

## Closing guidance for instructors

- Use scenarios 1–3 as graded assignments (rubric: verification steps, documentation, decision rationale).
- Use MCQs as quick quizzes.
- Use metadata exercises to check learners can produce structured, machine-readable records.
- Encourage learners to practice labeling reconstructed content explicitly and to simulate audit log entries.

---

End of exercises. Apply these repeatedly with real or simulated examples to build habits: verify, document, label, and escalate.