# KubeCon + CloudNativeCon EU 2027, Barcelona: Clearing the Runtime Confusion: Finding the Ultimate Runtime (Sessionize fields)

Status: draft v6, runtime bake-off, 30-minute session, not submitted. Field order follows the Sessionize form. Description limit: 1,000 characters (this text is 998). Source: abstract/kubecon-eu-2027-session.md in peopleforrester/talk-redteaming.

## Session Title

Clearing the Runtime Confusion: Finding the Ultimate Runtime

## Description

You've probably heard that containers aren't the most secure boundary for an agent. You keep hearing about microVMs and gVisor, but microVMs cost the most and containers are the Kubernetes default. What do microVMs actually stop that containers don't?

In this session we run Claude Code in agent-sandbox on each runtime and replay the public coding-agent escapes of 2026/2027:
- Config-file hooks (Cymulate)
- Symlinks (Wiz GhostApproval)
- A Docker socket and allowlisted git (Pillar Security)
- DNS tunneling (AWS AgentCore)
- Plus new ones that have arisen since Q4 of 2026

Patched kernel and runtime CVEs that go through the boundary instead of around it run alongside. A live scoreboard shows which runtime stopped, detected or missed each attack, first alone, then with Kyverno, Cilium FQDN egress and Falco added.

For platform and security engineers choosing a substrate for coding agents. Attendees leave with the harness, SandboxTemplates and raw results to rerun on their own clusters.

## Submitting for

KubeCon + CloudNativeCon

## Poster Session

No

## Track

Security (confirm it is on the EU 2027 track list; the form currently shows Emerging + Advanced)

## Session format

Session presentation (30 minutes)

## Audience Level

Intermediate

## Value to the community

Coding agents are moving off laptops and onto Kubernetes, and kubernetes-sigs/agent-sandbox, which reached v1.0 in August 2026, is the SIG Apps project built to host them. Every team adopting it has to pick a RuntimeClass, usually on the strength of vendor claims about isolation, and microVMs cost the most to run.

The best-known coding-agent escapes of 2026 went around the isolation boundary, through config files, symlinks, sockets, allowlisted commands and DNS. What a microVM buys over gVisor or runc is therefore an open and expensive question. This session answers it with measurements: the same attacks against each runtime under the same agent-sandbox templates, scored stopped, detected or missed, first with the runtime alone and then with Kyverno, Cilium and Falco added. The attack set is refreshed with escapes disclosed up to the event, so the results are current in March 2027.

The harness, SandboxTemplates, policies and raw results are published in a public repository before the talk, so anyone can rerun the scoreboard on their own cluster or add a technique. All techniques are public and run against isolated lab clusters, and gaps found in agent-sandbox are filed upstream with SIG Apps. gVisor and Kata Containers, the two strongest runtime options, are open source projects outside the CNCF, and the session says so.

## Case study?

No

## Talk presented before?

No

## Relevant CNCF/Open Source Projects

Kubernetes (kubernetes-sigs/agent-sandbox, RuntimeClass, user namespaces), Kyverno, Cilium, Envoy, SPIFFE/SPIRE, Falco, runc, gVisor (not CNCF), Kata Containers on QEMU and Firecracker (not CNCF)

## Additional resources

https://github.com/kubernetes-sigs/agent-sandbox

## Co-speakers

None

## Speaker profile (already set in Sessionize, no change needed)

Bio, title, company and prior talks come from the profile. Prior talks listed: two KubeCon EU 2026 Amsterdam sessions on the CNCF YouTube channel. Check once: the profile marks Accenture as an end user organization.
