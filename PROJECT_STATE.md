# Project State: red-teaming-the-agent-sandbox

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
Talk: "Red: Taming the Agent Sandbox", KubeCon + CloudNativeCon EU 2027, Barcelona.
Concept A from `research/2026-10-10-cfp-landscape-and-concepts.md`: replay the 2026
coding-agent escape classes (config files, symlinks, Docker socket, allowlisted
commands, DNS exfiltration) against a default and a hardened agent-sandbox, and score
each CNCF layer as stopped, detected, or missed. Likely track: Security.

Open decisions for Michael:
1. Main CFP (closes 2026-10-11 23:59 CEST) or a co-located event (closes 2026-10-18).
   This is the third proposal; only one non-panel session can be accepted at the main
   event.
2. Track: Security or Agentic AI.
3. Co-presenter, if any (end user or agent-sandbox maintainer).

Next steps:
1. Draft the abstract in `abstract/kubecon-eu-2027-session.md`.
2. Verify the claims the abstract depends on against primary sources.
3. Check Sched for the "Detonation and Isolation" abstract, the main overlap risk.

## Branch & Tests
- Branch: staging
- Working tree: clean after the research import commit
- Last CI: none configured

## Phase History
- 2026-10-10T23:08:00Z 1.1 · repo initialized, research imported
- 2026-10-10T23:08:00Z 1.1 → 1.2 research complete, planning the abstract
