# KubeCon + CloudNativeCon EU 2027, Barcelona: Red Teaming the Agent Sandbox: MicroVMs, Containers and More (Sessionize fields)

Status: draft v5, runtime bake-off, 30-minute session, not submitted. Field order follows the Sessionize form. Description limit: 1,000 characters (this text is 995). Source: abstract/kubecon-eu-2027-session.md in peopleforrester/talk-redteaming.

## Session Title

Red Teaming the Agent Sandbox: MicroVMs, Containers and More

## Description

You've probably heard that containers aren't the most secure boundary for an agent. You keep hearing about microVMs and gVisor, but microVMs cost the most and containers are the Kubernetes default. What do microVMs actually stop that containers don't?

In this session we run Claude Code in agent-sandbox on each runtime and replay the best-known public coding-agent escapes of 2026:
- Config-file hooks (Cymulate)
- Symlinks (Wiz GhostApproval)
- A Docker socket and allowlisted git (Pillar Security)
- DNS tunneling (AWS AgentCore)

Patched kernel and runtime CVEs that go through the boundary instead of around it run alongside. A live scoreboard shows which runtime stopped, detected or missed each attack, first alone, then with Kyverno, Cilium FQDN egress and Falco added.

For platform and security engineers choosing a substrate for coding agents. Attendees leave with the harness, SandboxTemplates and raw results to rerun on their own clusters to see whether these attacks get through.

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

Teams adopting kubernetes-sigs/agent-sandbox have to pick a RuntimeClass, and the choice is usually made from vendor claims about isolation strength. None of the best-known 2026 coding-agent escapes needed to break the isolation boundary, so the question of what a microVM buys over gVisor or runc is open and costly. This session gives platform and security teams a reproducible answer instead of a reference diagram: a harness that replays publicly disclosed technique classes against each runtime under the same agent-sandbox templates, and a scoring method that records stopped, detected or missed per runtime and per CNCF layer. The harness, Kyverno policies, Cilium network policies, Falco rules and raw results are published in a public repository before the talk, so anyone can rerun the scoreboard against their own cluster or add a technique.

All techniques are public and replayed against patched releases or isolated lab clusters. Gaps the runs expose in agent-sandbox itself are filed upstream with SIG Apps rather than saved for the stage.

The session is honest about where the CNCF stack ends. agent-sandbox (Kubernetes SIG Apps), Kyverno, Cilium, Envoy, SPIRE and Falco carry the control plane, policy, network, identity and detection layers. The isolation boundary underneath is a RuntimeClass, and its two strongest options, gVisor and Kata Containers, are open source projects outside the CNCF.

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
