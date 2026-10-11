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
Talk: "Clearing the Runtime Confusion: Which Agent Runtime Is the GOAT?", KubeCon + CloudNativeCon EU 2027, Barcelona.
Concept A from `research/2026-10-10-cfp-landscape-and-concepts.md`: replay the 2026
coding-agent escape classes (config files, symlinks, Docker socket, allowlisted
commands, DNS exfiltration) against a default and a hardened agent-sandbox, and score
each CNCF layer as stopped, detected, or missed. Likely track: Security.

Open decisions for Michael:
1. Track: Security or Agentic AI.
2. Co-presenter, if any (end user or agent-sandbox maintainer).

Next steps:
1. Michael reviews `abstract/kubecon-eu-2027-session.md` (draft v1) and submits on
   Sessionize by 2026-10-11 23:59 CEST.
2. Research revalidated 2026-10-11: `research/2026-10-11-verification.md` supersedes the
   2026-10-10 files wherever they disagree.

## Branch & Tests
- Branch: staging
- Working tree: clean after the research import commit
- Last CI: none configured

## Phase History
- 2026-10-10T23:08:00Z 1.1 · repo initialized, research imported
- 2026-10-10T23:08:00Z 1.1 → 1.2 research complete, planning the abstract
- 2026-10-11T00:30:00Z 1.2 · research revalidated, abstract draft v1 written
