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

## 2026-10-16 · 1.2 · question 70: Michael closes #1 by hand; #6 closes as done

Question 70 (run 693 on issue #6): #6 asks a run to close #1 with a comment naming 96e7985
and 6750229, but governance forbids executors from sending or publishing, so no dispatched
run can post it. Who closes #1, and should that wait until both commits reach main?

Answer (Michael, 2026-10-16): "Michael closes #1 by hand now with the draft comment, and
closes #6 as done."

What it changes: closing #1 does not wait for main. That matches the fleet convention: when
a run merges into staging with outcome done, the dispatcher closes the issue straight away
and main follows once staging passes the heavy gate. The closing comment is the draft from
run 693: "Closing: the fleet standard for this talk repo is in place on staging. 96e7985
states the repo identity in README.md and AGENTS.md and points at talks-knowledge (source of
truth for the talk) and conference-knowledge (event state). 6750229 adds CLAUDE.md as a
symlink to AGENTS.md, checked by IdentityTest. Michael's answer to question 32 (ln -s
allowed generally) is why the symlink was kept rather than replaced." No repo file changes
for #1 or #6 beyond this entry; the GitHub writes are Michael's.

## 2026-10-16 · 1.2 · question 66: #5 waits on a 'Build the demo harness' issue

Question 66 (runs 668 and 688 on issue #5): #5 can only be done once the demo harness
exists, and that build waits on the CFP notification due 2026-12-07. Both runs that day
were dispatched and neither could change anything. How should #5 wait so it stops being
re-dispatched?

Answer (Michael, 2026-10-16): "After the CFP notification, file a 'Build the demo harness'
issue and mark #5 blocked on it, so #5 is dispatched only after the harness lands."

What it changes: once the notification arrives, a 'Build the demo harness' issue is filed
and #5 is marked blocked on it with GitHub's native blocked-by relationship (the fleet rule
is that dependencies are links, not text in the body). The scheduler then skips #5 until
that issue closes. Until the harness issue is filed and linked, nothing stops #5 from being
dispatched again; such a run has nothing to change. AGENTS.md keeps its `No E2E command
yet:` line until the harness exists, and no other repo file changes.

## 2026-10-16 · 1.2 · question 78: Michael holds #5 with agent-stop until the CFP notification

Question 78 (runs 722 and 726 on issue #5): the dispatcher's manifest gate fails any run
that reaches validation with no commits after its base, and that is how run 722 failed.
The question 66 decision says a run on #5 has nothing to change until a 'Build the demo
harness' issue is filed after the CFP notification (due 2026-12-07) and linked as #5's
blocker. Nothing stops dispatch until then, so each run on #5 either fails the gate or
makes a filler commit to pass it, and the fleet rejected filler commits in other-events
questions 64 and 71. How should #5 be held until the notification?

Answer (Michael, 2026-10-16): "Michael applies agent-stop on #5 now and releases it after
the CFP notification (due 2026-12-07), when the 'Build the demo harness' issue is filed and
linked as #5's blocker (same as other-events question 71)."

What it changes: this closes the gap question 66 left open. From now until the
notification, #5 is held by Michael's `agent-stop` label rather than by the system, so the
dispatcher stops re-running it. After the notification the 'Build the demo harness' issue
is filed and linked as #5's blocker with GitHub's native blocked-by, and only then is
`agent-stop` removed. The blocked-by link takes over the hold, so #5 is dispatched once the
harness lands. The manifest gate stays as it is, and no filler commits are made. The label
is Michael's to set on GitHub; no repo file changes beyond this entry and
PROJECT_STATE.md. AGENTS.md keeps its `No E2E command yet:` line until the harness exists.

## 2026-10-16 · 1.2 · question 65: #1 is kept and closed by hand, as question 70 answered

Question 65 (issue #7, filed when #1 reached step 6 of the failure ladder; research run
671): what should happen to #1, whose work is all on staging (96e7985, and 6750229 via #4)
but whose definition of done ends in closing the issue, which no executor run can do?
Run 671 recommended keeping #1 (disposition keep) and closing it either through one fresh
close-out run or by Michael by hand, and closing #6 alongside it.

Answer: already given in question 70 (Michael, 2026-10-16): "Michael closes #1 by hand
now with the draft comment, and closes #6 as done." That is run 671's option 2, so #7
needs no new decision.

What it changes: #1 is not re-dispatched, and no close-out run is made for it. The GitHub
writes (closing #1 with the question 70 comment, closing #6) are Michael's. #1 stays
`completed`, not `not planned`, because the identity check is done. Run 671's findings on
the dispatcher (an empty branch fails the manifest gate, follow-ups that ask for GitHub
actions, the no-progress rule tripping on read-only runs) belong to hecaton, not this repo.
Question 78 has already kept the manifest gate as it is. No repo file changes beyond this
entry and PROJECT_STATE.md.

## 2026-10-16 · 1.2 · Correction: question 32 was decided by the coordinator, not by Michael

Per issue #9 (requested by peopleforrester/hecaton#127). Runs on this repo recorded some
answers as Michael's that hecaton's coordinator decided under Michael's standing rules.
Hecaton records these with decided_by = coordinator. The decision below was decided by the
coordinator under Michael's standing rules, not by Michael:

- Question 32 (issue #1, run 306), 2026-10-16 02:46 UTC: "Allow it generally: hecaton is
  switching every run to all shell commands except sudo, su and pushing branches (in
  progress tonight). Re-dispatch #1 once that is deployed; ln -s will then be allowed."

The decision stands; only who made it is corrected. Where this log calls it Michael's, read
it as the coordinator's: the question 70 entry above quotes run 693's draft closing comment
for #1, which says "Michael's answer to question 32 (ln -s allowed generally)". The earlier
records of question 32 (run 315's 7f5a204 and run 671's a3cfa69, which said "Answer
(Michael, 2026-10-16)") never reached staging. Earlier entries are left as written because
this log is append-only.
