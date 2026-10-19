# Project State: talk-agent-runtime-goat

Phase: 1.2 Plan
Approved: pending

## Lifecycle
- [x] 1.1 Research
- [ ] 1.2 Plan  ← you are here
- [ ] 1.3 Approve
- [ ] 2.1 Test
- [ ] 2.2 Implement
- [ ] 2.3 Verify
- [ ] 3.1 Stage
- [ ] 3.2 Confirm CI
- [ ] 3.3 Promote

## Contracts
None yet.

## Current Plan
Talk: "Clearing the Runtime Confusion: Which Agent Runtime Is the GOAT?", KubeCon +
CloudNativeCon EU 2027, Barcelona, 2027-03-15 to 18. Security track, 30-minute session.

Abstract submitted on Sessionize before the main CFP closed (2026-10-11 23:59 CEST),
confirmed by Michael 2026-10-14. Submitted text is draft v6 in
`abstract/kubecon-eu-2027-session.md` and `abstract/sessionize-fields.md`.

Talk shape: runtime bake-off. Claude Code in kubernetes-sigs/agent-sandbox on runc,
gVisor, and Kata (QEMU, Firecracker), replaying the 2026 coding-agent escapes plus patched
through-the-boundary CVEs. Scoreboard of stopped, detected, or missed per attack, first
runtime alone, then with Kyverno, Cilium FQDN egress, and Falco. Harness, SandboxTemplates,
policies, and raw results to be published in a public repo before the talk.

Next steps:
1. Wait for CFP notification, due 2026-12-07.
2. On acceptance, plan the harness build (Phase 1.2 for the demo work).
   After the notification, file a 'Build the demo harness' issue and mark #5 blocked
   on it (GitHub's native blocked-by), per question 66. Until then #5 is held by
   Michael's `agent-stop` label, which comes off once the blocked-by link is in place
   (question 78).
3. Optional: Concept B (warm pool as credential cache) for a co-located event; that CFP
   closes 2026-10-18 23:59 CEST.
4. Lightning cut for the co-located Open Source SecurityCon (issue #11): submitted
   2026-10-18 (question 178), recorded in `abstract/securitycon-eu-2027-lightning.md`.
   Co-located notifications are due 2026-12-14. If the main session is accepted
   (2026-12-07), decide whether the lightning talk stays as a preview or is withdrawn.

## Branch & Tests
- Branch: staging
- Working tree: clean after the lightning-cut submission commit
- Last CI: none configured

## Phase History
- 2026-10-10T23:08:00Z 1.1 · repo initialized, research imported
- 2026-10-10T23:08:00Z 1.1 → 1.2 research complete, planning the abstract
- 2026-10-11T00:30:00Z 1.2 · research revalidated, abstract draft v1 written
- 2026-10-11T16:00:43Z 1.2 · reframed as runtime bake-off, retitled, abstract at draft v6
- 2026-10-14T21:15:19Z 1.2 · abstract confirmed submitted; awaiting notification
- 2026-10-16 1.2 · identity check (issue #1): README and AGENTS.md point at talks-knowledge and conference-knowledge; CLAUDE.md symlink still to add
- 2026-10-16 1.2 · heavy gate (issue #3): no E2E tests exist yet, so AGENTS.md states there is no E2E command until the demo harness lands
- 2026-10-16 1.2 · CLAUDE.md symlink (issue #4): CLAUDE.md links to AGENTS.md, checked by IdentityTest
- 2026-10-16 1.2 · E2E line (issue #5): no harness yet, so the `No E2E command yet:` line stays; the dispatcher's E2E sweep files once per repo and will not re-file #3
- 2026-10-16 1.2 · closing #1 (issue #6, question 70): Michael closes #1 by hand with a comment naming 96e7985 and 6750229; no wait for main
- 2026-10-16 1.2 · #5 waits (question 66): after the CFP notification, file 'Build the demo harness' and mark #5 blocked on it
- 2026-10-16 1.2 · #5 hold (question 78): Michael applies agent-stop on #5 until the notification; the blocked-by link to the harness issue then replaces it
- 2026-10-16 1.2 · #1 ladder (issue #7, question 65): settled by question 70; #1 is kept, not re-dispatched, and closed by Michael by hand
- 2026-10-16 1.2 · attribution (issue #9): question 32 was decided by the coordinator under Michael's standing rules, not by Michael; correction appended to decisions.md
- 2026-10-16 1.2 · attribution (issue #10): questions 66, 70 and 78 were decided by hecaton's research under Michael's standing rules, not by Michael; correction appended to decisions.md
- 2026-10-17 1.2 · lightning cut (issue #11): `abstract/securitycon-eu-2027-lightning.md` tracks the Open Source SecurityCon submission; abstract stays in talks-knowledge; not submitted as of 2026-10-17, awaiting Michael
- 2026-10-19 1.2 · lightning cut submitted (issue #11, question 178): Sessionize confirmation of 2026-10-18 16:27 UTC found; title and description as submitted recorded in `abstract/securitycon-eu-2027-lightning.md`
