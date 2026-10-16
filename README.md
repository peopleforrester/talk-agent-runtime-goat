# Clearing the Runtime Confusion: Which Agent Runtime Is the GOAT?

Working repo for Michael Forrester's KubeCon + CloudNativeCon Europe 2027 (Barcelona)
submission. This repo is the primary home for the agent-substrate talk: research,
abstract, demo, and deck. The talk register in `talks/talks-knowledge` lists it with
Michael's other submissions.

**Speaker:** Michael Forrester, solo. No co-speakers listed.

**Target:** KubeCon + CloudNativeCon Europe 2027, Barcelona, 2027-03-15 to 18. Security
track, 30-minute session.

**Status:** submitted on Sessionize for the main CFP (closed 2026-10-11). Notifications
are due 2026-12-07.

**Built from:** the research in `research/` and the proposal in `abstract/`. The demo
builds on the upstream kubernetes-sigs/agent-sandbox project.

**Working thesis:** a runtime bake-off. Claude Code runs in kubernetes-sigs/agent-sandbox
on runc, gVisor, and Kata microVMs (QEMU and Firecracker). Each runtime faces the public
2026 coding-agent escapes, which went around the isolation boundary through config
files, symlinks, Docker sockets, allowlisted commands, and DNS, plus patched kernel and
runtime CVEs that go through it. A scoreboard marks each attack stopped, detected, or
missed, first with the runtime alone and then with Kyverno, Cilium, and Falco added. The
title is ironic: no single runtime or layer stops everything.

Sibling talks, kept separate in scope:

| Talk | Repo | Boundary with this talk |
|---|---|---|
| Agentic guardrails (BurritoBot, with Whitney Lee) | `talks/Kubecon-NA-2026-Whitney-BurritoBot` | Admission policy and human approval. Here, admission gets one slide. |
| Context store comparison (with Jeremy Morgan) | `talks/Databases-bakeoff-kubecon-eu-2027` | RAG and data stores. None of that here. |

## Where things live

| Repo | Holds |
|---|---|
| `talks/talks-knowledge` | Source of truth for the talks: the register (`talks/register.md`), the research index, and the abstracts and talk scripts |
| `conferences/conference-knowledge` | Event state: dates, CFPs, acceptances |
| This repo | The talk's own research, abstract drafts, and, once built, the demo harness and deck |

## Key dates (from the 2026-10-10 research, which cites the CNCF CFP page)

conference-knowledge is authoritative for these. This table is a snapshot.


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
| `abstract/kubecon-eu-2027-session.md` | Session proposal: title, abstract, benefits, projects, committee notes, unsubmitted source table (submitted as draft v6) |
| `abstract/sessionize-fields.md` | The same proposal in Sessionize form field order |
| `AGENTS.md` | Repo rules for coding agents, test command, where things live |
| `CLAUDE.md` | Symlink to `AGENTS.md`, so Claude Code loads the same rules |
| `tests/test_abstract.py` | Checks title agreement, the Sessionize description limit, this table, the talks-knowledge pointers, and the `CLAUDE.md` symlink |
| `PROJECT_STATE.md` | Current phase, open decisions, next steps |
| `decisions.md` | Append-only decision log |

## Verification status

The research files are dated 2026-10-10 and carry their own caveats. Items flagged
there as unverified (several NA 2026 speakers, the "Detonation and Isolation" abstract,
agent-sandbox maintainer names, ToolHive's CNCF status, secondhand escape reports) must
be checked against primary sources before they appear in the abstract or on a slide.
