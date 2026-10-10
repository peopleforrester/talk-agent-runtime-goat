# KubeCon + CloudNativeCon EU 2027, Barcelona: Red: Taming the Agent Sandbox

Status: draft v1, not submitted. Target: KubeCon + CloudNativeCon EU 2027, Barcelona,
2027-03-15 to 18. Track: Security. Format: 30-minute session presentation. Speaker:
Michael Forrester. CFP closes 2026-10-11, 23:59 CEST.

## Title

Red: Taming the Agent Sandbox

## Abstract

Your coding agent runs in a Kubernetes sandbox. gVisor sits between it and the node, every task gets a fresh pod, and the security review signed off. Then a prompt hidden in a README asks the agent to tidy the repository's settings, and it writes one hook into `.claude/settings.json`. Nothing escapes the sandbox. The next developer to open that repository runs the hook on their laptop.

That is not hypothetical. The best-known coding-agent sandbox escapes of 2026 did not break a hypervisor. Cymulate's configuration escapes, Wiz's GhostApproval symlinks, Pillar Security's week of sandbox escapes and DNS tunneling out of AWS AgentCore all went around the sandbox: through config files, symlinks, a reachable Docker socket, allowlisted git commands and DNS. Meanwhile platform teams are standardizing on kubernetes-sigs/agent-sandbox, now at v1.0, with gVisor or Kata underneath.

In this session, Michael Forrester red-teams that stack. Each 2026 technique is replayed against two agent-sandbox clusters. One runs the default template. The other is hardened with a gVisor or Kata RuntimeClass, user namespaces, Kyverno admission, Cilium FQDN default-deny with DNS locked to the cluster, an Envoy egress proxy that holds the real credentials so the sandbox never does, SPIRE workload identity and Falco. A live scoreboard records, for every attack, which layer stopped it, which only detected it, and which missed it. The scores come from the runs, including the ones that make the hardened cluster look bad.

Attendees leave knowing which controls earn their place around an agent sandbox, which gaps are still open upstream (identity and network policy bound at claim time are both on the agent-sandbox roadmap as planned), and with the attack harness, policies and raw results to replay against their own clusters.

The bars of the cage held every time. This talk is about the door.

## Benefits to the Ecosystem

Agent sandboxes are being adopted on the strength of the isolation boundary, and the published 2026 escapes show the boundary was rarely the thing that failed. This session gives platform and security teams a reproducible test instead of a reference diagram: a harness that replays publicly disclosed technique classes, two pinned agent-sandbox configurations, and a scoring method that records stopped, detected or missed for each CNCF layer. The harness, Kyverno policies, Cilium network policies, Falco rules and raw results are published in a public repository before the talk, so anyone can rerun the scoreboard against their own cluster or add a technique.

All techniques are public and replayed against patched releases or isolated lab clusters. Gaps the runs expose in agent-sandbox itself are filed upstream with SIG Apps rather than saved for the stage.

The session is honest about where the CNCF stack ends. agent-sandbox (Kubernetes SIG Apps), Kyverno, Cilium, Envoy, SPIRE and Falco carry the control plane, policy, network, identity and detection layers. The isolation boundary underneath is a RuntimeClass, and its two strongest options, gVisor and Kata Containers, are open source projects outside the CNCF.

## Case Study

No. This is a technical demonstration on purpose-built clusters. The incidents are public disclosures used as the attack catalog.

## Presented Before

No. This is original content for KubeCon EU 2027.

## CNCF and Open Source Projects

- Kubernetes: kubernetes-sigs/agent-sandbox (SIG Apps), RuntimeClass, user namespaces
- Kyverno (Graduated)
- Cilium (Graduated)
- Envoy (Graduated)
- SPIFFE / SPIRE (Graduated)
- Falco (Graduated)
- gVisor (Google, open source, not CNCF)
- Kata Containers (OpenInfra Foundation, not CNCF)

## Speaker Bio

Michael Forrester is a Principal Training Architect who creates cloud-native and Kubernetes training content reaching over 1,000,000 learners at KodeKloud, a CNCF Training Partner. He holds 12 AWS certifications, multiple CNCF certifications, and multiple NVIDIA certifications across 25+ years spanning CTO to IC roles at AWS, ThoughtWorks, Red Hat, and Honeywell. He once gave an AI agent cluster-level permissions and it deleted his cluster. He has been testing what agents can reach ever since.

## Why this one, for the committee

- Problem first: the Security track asks for threat modeling and incident post-mortems. This talk replays real 2026 disclosures and reports measured results per layer.
- Nothing like it on the NA 2026 program. Of 57 NA 2026 sessions matching sandbox, escape, red team, gVisor, Kata or agent-sandbox, none replays the 2026 escape classes against agent-sandbox and scores each layer. The agent-sandbox talks there (Detonation and Isolation; Platform-First AI Agent Security; the Untrusted Code on Secure Runtimes tutorial; Adobe's production story) show how to build and run it. This one tests the claims those talks make, including "prevents escape even with root access".
- Vendor-neutral: no product pitch, every component open source, and the non-CNCF pieces are named as such.

## Notes for Michael (not submitted)

Every claim in the abstract was checked against its primary source on 2026-10-11. Full
record: `research/2026-10-11-verification.md`.

| Claim in the abstract | Source |
|---|---|
| Agent writes a hook into `.claude/settings.json`; the host runs it on next launch | Cymulate CBSE; Claude Code CVE-2026-25725, GHSA-ff64-7w26-62rf (2026-02-06) |
| GhostApproval symlinks | Wiz, 2026-07-08 |
| Pillar "week of sandbox escapes": Docker socket, allowlisted `git show` | Pillar Security, 2026-07-20 |
| DNS tunneling out of AWS AgentCore (since remediated, 2026-04-15) | Unit 42 2026-04-07; BeyondTrust 2026-03-16 |
| None of these broke a hypervisor | All four disclosures above: each abuses files, symlinks, sockets, allowlists or DNS. The 2026 hypervisor and runtime CVEs (Firecracker, Cloud Hypervisor, Kata, KVM Januscape, gVisor) are separate research, not agent escapes |
| agent-sandbox at v1.0 | v1.0.0 2026-08-28; latest v1.0.6 2026-10-08 |
| Claim-time identity and network policy are Planned | agent-sandbox roadmap.md, read 2026-10-11 |
| "Prevents escape even with root access" | Platform-First AI Agent Security abstract, KubeCon NA 2026 schedule |
| CNCF statuses | cncf/landscape, read 2026-10-11 |

Open items:

- Sessionize character limits are not published. Check the description against the form before pasting (draft is about 330 words).
- The CFP page asks for the description in third-person sentences. The draft opens in second person ("Your coding agent") as the house style does and refers to Michael in the third person. Decide before pasting.
- The closing line is optional. Cut it if the form is tight.
- Prior recording: pick one (SREday Austin or LLMday Austin, May 2026).
- Co-presenter: none listed. The format allows two.
- Responsible replay: only public techniques, against patched releases or isolated lab clusters with pinned vulnerable versions. Coordinate anything new with the affected project before March.
