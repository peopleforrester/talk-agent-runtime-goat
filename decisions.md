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

## 2026-10-11T15:29:02Z · 1.2 · Talk reframed as a runtime bake-off on agent-sandbox

Michael's intent was a runtime bake-off: Claude Code on runc, gVisor and Kata microVMs (QEMU, Firecracker) under kubernetes-sigs/agent-sandbox, scored against the 2026 escapes plus patched through-the-boundary CVEs, then with policy layers added. The default-versus-hardened layer scoreboard was a narrowing introduced in drafting. Title is now "Red Teaming the Agent Sandbox: MicroVMs, Containers and More". "Never broke a hypervisor" replaced by "none needed to break the isolation boundary", since most of those agents were not behind a hypervisor.

## 2026-10-11T15:54:26Z · 1.2 · Title changed

Michael chose "Clearing the Runtime Confusion: Finding the Ultimate Runtime", replacing "Red Teaming the Agent Sandbox: MicroVMs, Containers and More".

## 2026-10-11T15:57:24Z · 1.2 · Title changed to the GOAT framing

Michael chose "Clearing the Runtime Confusion: Which Agent Runtime Is the GOAT?". The title is intentionally ironic: the talk argues there is no single best runtime and no single sufficient layer. Value to the community now states that up front.

## 2026-10-11T16:00:43Z · 1.2 · GitHub repo renamed

peopleforrester/talk-redteaming renamed to peopleforrester/talk-agent-runtime-goat to match the title. Local folder unchanged. Still private.

## 2026-10-14T21:15:19Z · 1.2 · Abstract submitted; repo visibility recorded

Michael confirmed the session was submitted on Sessionize before the main CFP closed (2026-10-11 23:59 CEST). The abstract files, README, and PROJECT_STATE.md now say so. The README thesis and PROJECT_STATE plan were brought in line with the runtime bake-off framing. The GitHub repo reads as PUBLIC as of 2026-10-14, which supersedes "Still private" in the 2026-10-11 entry.

## 2026-10-16 · 1.2 · Repo identity and where things live

Per issue #1, the fleet standard for a talk repo. talks-knowledge is the source of truth for the register, research index, abstracts, and talk scripts; conference-knowledge holds event state. README and AGENTS.md now say so. Where the abstract here and the one in talks-knowledge disagree, talks-knowledge wins. The README no longer calls this the "third" EU 2027 submission; the register owns that count, and the 2026-10-10 entry above keeps the old wording because this log is append-only.

## 2026-10-16 · 1.2 · No E2E command until the demo harness exists

Issue #3 asks for an `E2E command:` line where the repo has end-to-end or integration tests against real services. It has none: the only suite checks the abstract files, README, and AGENTS.md. Pointing the heavy gate at that suite or at a placeholder would claim coverage that does not exist, so AGENTS.md states that there is no E2E command yet and why, and a test holds it to either that statement or exactly one declared command. The demo harness, run against a real cluster, is where the first E2E command comes from.

## 2026-10-16 · 1.2 · E2E declaration waits for the demo harness; the sweep will not re-file

Issue #5 asks for the `No E2E command yet:` line to become `E2E command: ` plus the harness command once the demo harness exists. It does not exist yet (its build is planned after the CFP notification, due 2026-12-07), so the line stays and #5 stays open until the harness lands. The sweep that filed #3 is the dispatcher's heavy gate (`hecaton.run.mainline._ask_for_e2e`). It does not read the explanation line: `command_line` matches only a line that starts with the label `E2E command:` and a backticked command, so `No E2E command yet:` declares nothing, and the light `Test command:` keeps gating `main`. It files at most one `e2e` issue per repo ever (`_open_gate_issue(..., ever=True)`), so it will not file #3 again, whatever that line says.
