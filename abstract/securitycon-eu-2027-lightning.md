# Open Source SecurityCon EU 2027 (co-located), Barcelona: lightning cut of Clearing the Runtime Confusion

Status: submitted on Sessionize 2026-10-18, before the co-located CFP closed (2026-10-18
23:59 CEST). Co-located reviews begin 2026-10-22; speaker notifications are due Monday
2026-12-14. Issue #11 tracks it.

Submitted: yes, 2026-10-18 16:27 UTC (18:27 CEST). Evidence: the Sessionize "We have
received your submission" mail from CNCF-Hosted Co-located Events Europe 2027
(cncf-hosted-co-located-events-europe-2027@events.sessionize.com) to
michaelrishiforrester@gmail.com, dated Sun, 18 Oct 2026 16:27:40 +0000 (question 178).

## What it is

A 10-minute lightning version of the main session, for the Open Source SecurityCon event
co-located with KubeCon + CloudNativeCon EU 2027. One speaker, Michael Forrester. Same
runtimes, attack catalog, scoring and policy layer as `abstract/kubecon-eu-2027-session.md`
draft v6, cut down to fit ten minutes. Entered as a session from the speaker profile, then
attached to the co-located CFP; topic "Leveraging + Preparing for AI in OSS Security",
level Intermediate.

## Title as submitted

Which Agent Runtime Is the GOAT? Coding-Agent Escapes Against runc, gVisor and Kata in Ten Minutes

## Description as submitted

Containers are the Kubernetes default and microVMs cost the most, so which one is safe enough for a coding agent? This lightning talk measures it. It runs a coding agent in kubernetes-sigs/agent-sandbox on runc, gVisor and Kata microVMs, replays the public coding-agent escapes of 2026, and shows the scoreboard: which runtime stopped, detected or missed each attack, first alone and then with Kyverno, Cilium egress policy and Falco added.

In ten minutes, attendees get the one-slide answer: which runtime buys what, and which attacks no runtime stops without a policy layer. The harness and raw results are public, so anyone can rerun the scoreboard on their own cluster.

## Where the abstract lives

The draft is in `talks/talks-knowledge` (`peopleforrester/talks-knowledge`) at
`abstracts/kubecon-eu-2027-colocated/securitycon-runtime-goat-lightning.md`, and the
field-by-field Sessionize entry, with the sources for the five 2026 escapes, is talk 5 in
`abstracts/kubecon-eu-2027-colocated/sessionize-fields.md`. talks-knowledge is the source
of truth and wins where this file disagrees with it.

The title above is the one in the Sessionize confirmation mail (98 characters, under the
100 limit). The description is copied from talk 5 of the talks-knowledge field sheet, the
text Michael entered from (674 characters). The confirmation mail carries only the title,
and this repo's runs cannot open the Sessionize dashboard, so the description has not been
checked against the dashboard. The CFP is closed, so the submitted text no longer changes.

## Next decision

Main session notifications are due 2026-12-07, a week before the co-located ones
(2026-12-14). If the main session is accepted, decide whether the lightning talk stays on
as a preview of it or is withdrawn.

## Speaker profile

Sessionize takes the bio from the speaker profile. The field sheet had Michael replace it
with the Accenture LearnVantage bio; his current short title is "AI Workforce
Transformation Lead, FDE and AI-Native Programs, Accenture LearnVantage"
(personal-knowledge#60, mrf-knowledge#26). The bio in `abstract/kubecon-eu-2027-session.md`
is the older KodeKloud version and is not the one to use.
