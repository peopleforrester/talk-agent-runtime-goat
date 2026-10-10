# Red: Taming the Agent Sandbox

Working repo for Michael Forrester's third KubeCon + CloudNativeCon Europe 2027
(Barcelona) submission. This repo is the primary home for the agent-substrate talk:
research, abstract, demo, and deck.

**Working thesis:** none of the 2026 coding-agent sandbox escapes broke a hypervisor.
They went around the sandbox through config files, symlinks, Docker sockets,
allowlisted commands, and DNS. The talk replays each technique class against a default
and a hardened kubernetes-sigs/agent-sandbox deployment and scores which CNCF layer
stopped, detected, or missed each one (Concept A in the research).

Sibling talks, kept separate in scope:

| Talk | Repo | Boundary with this talk |
|---|---|---|
| Agentic guardrails (BurritoBot, with Whitney Lee) | `talks/Kubecon-NA-2026-Whitney-BurritoBot` | Admission policy and human approval. Here, admission gets one slide. |
| Context store comparison (with Jeremy Morgan) | `talks/Databases-bakeoff-kubecon-eu-2027` | RAG and data stores. None of that here. |

## Key dates (from the 2026-10-10 research, which cites the CNCF CFP page)

| Item | Date |
|---|---|
| Main CFP closes | Sunday 2026-10-11, 23:59 CEST |
| Co-located events CFP closes | Sunday 2026-10-18, 23:59 CEST |
| Notifications | 2026-12-07 |
| Cloud Native Rejekts EU 2027 CFP | 2026-12-07 to 2027-01-03 |
| Event | 2027-03-15 to 2027-03-18, Barcelona |

## Layout

| Path | What |
|---|---|
| `research/2026-10-10-substrate-state-of-the-art.md` | Isolation substrates, 2026 CVE record, agent escape catalog, orchestration options, defense in depth, reference architectures |
| `research/2026-10-10-cfp-landscape-and-concepts.md` | CNCF stack by layer, agent-sandbox roadmap, practitioner pain points, CFP logistics, six talk concepts ranked |
| `research/2026-10-10-competing-talks.md` | Competing talks March 2026 to March 2027 and the overlap matrix by angle |
| `research/2026-10-10-stack-and-talk-ideas-summary.md` | One-page summary of the stack and the five talk ideas |
| `research/2026-10-11-verification.md` | Primary-source recheck of every claim the abstract uses; supersedes the 2026-10-10 files where they disagree |
| `abstract/kubecon-eu-2027-session.md` | Session proposal: title, abstract, benefits, projects, committee notes, unsubmitted source table |
| `PROJECT_STATE.md` | Current phase, open decisions, next steps |
| `decisions.md` | Append-only decision log |

## Verification status

The research files are dated 2026-10-10 and carry their own caveats. Items flagged
there as unverified (several NA 2026 speakers, the "Detonation and Isolation" abstract,
agent-sandbox maintainer names, ToolHive's CNCF status, secondhand escape reports) must
be checked against primary sources before they appear in the abstract or on a slide.
