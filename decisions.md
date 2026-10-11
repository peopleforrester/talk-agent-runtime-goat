# Decisions

Append-only audit log for this repo, per the state-persistence rule.

## 2026-10-10T23:08:00Z · 1.1 · Repo is the primary home for the agent-substrate talk

Michael designated this repo as the primary location for "Red: Taming the Agent
Sandbox", his third KubeCon EU 2027 submission. The four 2026-10-10 research documents
were imported verbatim into `research/`, with one British spelling changed to American.
Working concept is Concept A (red-team replay, scored per CNCF layer). The research
ranks it first for acceptance odds and as the best live demo. Concept B (warm pool as
credential cache) is the runner-up and a candidate for a co-located event.

## 2026-10-11T00:30:00Z · 1.2 · Research revalidated; abstract v1 drafted

Three parallel checks against primary sources. Corrections that changed the abstract:
KEP-5823 missed v1.37 (targets v1.38), so checkpoint/restore is out of the abstract;
GitSpawn belongs to Manifold Security, not Adversa, and only secondary sources exist, so
it is out; AgentCore DNS tunneling was remediated 2026-04-15 and is described in the past
tense; Kata CVE-2026-44210 is Medium, not critical; the Red Hat build carries no
Technology Preview label. The NA 2026 schedule (57 matching sessions) has no talk that
replays the 2026 escape classes against agent-sandbox, so Concept A stands. Abstract style
follows the bakeoff and BurritoBot packets: second-person opening scene, live naive versus
hardened demo, CNCF projects with maturity, committee notes, and an unsubmitted source
table. Track: Security. Format: 30-minute session.

## 2026-10-11T15:12:21Z · 1.2 · Talk title corrected

The title is "Red Teaming the Agent Sandbox: Isolating Agents on Kubernetes". The earlier "Red: Taming the Agent Sandbox" was a mistranscription; prior entries keep the old string because this log is append-only.
