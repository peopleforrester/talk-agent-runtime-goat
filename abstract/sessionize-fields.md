# KubeCon + CloudNativeCon EU 2027, Barcelona: Red: Taming the Agent Sandbox (Sessionize fields)

Status: draft v3, 30-minute session, not submitted. Field order follows the Sessionize form. Description limit: 1,000 characters (this text is 977). Source: abstract/kubecon-eu-2027-session.md in peopleforrester/talk-redteaming.

## Session Title

Red: Taming the Agent Sandbox

## Description

Your coding agent runs in a Kubernetes sandbox with gVisor underneath. A prompt hidden in a README gets it to write one hook into `.claude/settings.json`. Nothing escapes the sandbox. The next developer to open the repo runs the hook.

The best-known coding-agent escapes of 2026 (Cymulate, Wiz GhostApproval, Pillar Security, AWS AgentCore DNS tunneling) never broke a hypervisor. They went around it through config files, symlinks, Docker sockets, allowlisted commands and DNS.

Michael Forrester red-teams two kubernetes-sigs/agent-sandbox clusters, replaying each technique against the default template and one hardened with gVisor or Kata, user namespaces, Kyverno, Cilium FQDN egress, an Envoy credential proxy, SPIRE and Falco. A live scoreboard shows which layer stopped, detected or missed every attack.

For platform and security engineers running coding agents on Kubernetes. Attendees leave with the harness, policies and raw results to rerun on their own clusters.

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

Agent sandboxes are being adopted on the strength of the isolation boundary, and the published 2026 escapes show the boundary was rarely the thing that failed. This session gives platform and security teams a reproducible test instead of a reference diagram: a harness that replays publicly disclosed technique classes, two pinned agent-sandbox configurations, and a scoring method that records stopped, detected or missed for each CNCF layer. The harness, Kyverno policies, Cilium network policies, Falco rules and raw results are published in a public repository before the talk, so anyone can rerun the scoreboard against their own cluster or add a technique.

All techniques are public and replayed against patched releases or isolated lab clusters. Gaps the runs expose in agent-sandbox itself are filed upstream with SIG Apps rather than saved for the stage.

The session is honest about where the CNCF stack ends. agent-sandbox (Kubernetes SIG Apps), Kyverno, Cilium, Envoy, SPIRE and Falco carry the control plane, policy, network, identity and detection layers. The isolation boundary underneath is a RuntimeClass, and its two strongest options, gVisor and Kata Containers, are open source projects outside the CNCF.

## Case study?

No

## Talk presented before?

No

## Relevant CNCF/Open Source Projects

Kubernetes (kubernetes-sigs/agent-sandbox, RuntimeClass, user namespaces), Kyverno, Cilium, Envoy, SPIFFE/SPIRE, Falco, gVisor (not CNCF), Kata Containers (not CNCF)

## Additional resources

https://github.com/kubernetes-sigs/agent-sandbox

## Co-speakers

None

## Speaker profile (already set in Sessionize, no change needed)

Bio, title, company and prior talks come from the profile. Prior talks listed: two KubeCon EU 2026 Amsterdam sessions on the CNCF YouTube channel. Check once: the profile marks Accenture as an end user organization.
