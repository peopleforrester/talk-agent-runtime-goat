# KubeCon + CloudNativeCon EU 2027, Barcelona: Clearing the Runtime Confusion: Which Agent Runtime Is the GOAT?

Status: draft v6, runtime bake-off, not submitted. Description is 998 characters against the 1,000-character Sessionize limit. Target: KubeCon + CloudNativeCon EU 2027, Barcelona,
2027-03-15 to 18. Track: Security. Format: 30-minute session presentation. Speaker:
Michael Forrester. CFP closes 2026-10-11, 23:59 CEST.

## Title

Clearing the Runtime Confusion: Which Agent Runtime Is the GOAT?

## Description (Sessionize field, max 1,000 characters)

You've probably heard that containers aren't the most secure boundary for an agent. You keep hearing about microVMs and gVisor, but microVMs cost the most and containers are the Kubernetes default. What do microVMs actually stop that containers don't?

In this session we run Claude Code in agent-sandbox on each runtime and replay the public coding-agent escapes of 2026/2027:
- Config-file hooks (Cymulate)
- Symlinks (Wiz GhostApproval)
- A Docker socket and allowlisted git (Pillar Security)
- DNS tunneling (AWS AgentCore)
- Plus new ones that have arisen since Q4 of 2026

Patched kernel and runtime CVEs that go through the boundary instead of around it run alongside. A live scoreboard shows which runtime stopped, detected or missed each attack, first alone, then with Kyverno, Cilium FQDN egress and Falco added.

For platform and security engineers choosing a substrate for coding agents. Attendees leave with the harness, SandboxTemplates and raw results to rerun on their own clusters.

## Value to the community

The title is deliberately glib. Teams choosing a runtime for coding agents want one answer: the GOAT runtime that is secure enough to stop thinking about. There isn't one, and this session takes that idea apart with data. The scoreboard shows the ranking changing with the attack, and it shows that no single layer, runtime or policy, stops everything on its own.

Coding agents are moving off laptops and onto Kubernetes, and kubernetes-sigs/agent-sandbox, which reached v1.0 in August 2026, is the SIG Apps project built to host them. Every team adopting it has to pick a RuntimeClass, usually on the strength of vendor claims about isolation, and microVMs cost the most to run. The best-known coding-agent escapes of 2026 went around the isolation boundary, through config files, symlinks, sockets, allowlisted commands and DNS, while kernel and runtime CVEs go through it. The session measures both against runc, gVisor and Kata microVMs under the same agent-sandbox templates, scored stopped, detected or missed, first with the runtime alone and then with Kyverno, Cilium and Falco added. Attendees leave knowing which runtime buys what, and which attacks no runtime stops without a policy layer. The attack set is refreshed with escapes disclosed up to the event, so the results are current in March 2027.

The harness, SandboxTemplates, policies and raw results are published in a public repository before the talk, so anyone can rerun the scoreboard on their own cluster or add a technique. All techniques are public and run against isolated lab clusters, and gaps found in agent-sandbox are filed upstream with SIG Apps. gVisor and Kata Containers, the two strongest runtime options, are open source projects outside the CNCF, and the session says so.

## Case study?

No. This is a technical demonstration on purpose-built clusters. The incidents are public disclosures used as the attack catalog.

## Talk presented before?

No. This is original content for KubeCon EU 2027.

## Relevant CNCF/Open Source Projects

- Kubernetes: kubernetes-sigs/agent-sandbox (SIG Apps), RuntimeClass, user namespaces
- Kyverno (Graduated)
- Cilium (Graduated)
- Envoy (Graduated)
- SPIFFE / SPIRE (Graduated)
- Falco (Graduated)
- runc (OCI)
- gVisor (Google, open source, not CNCF)
- Kata Containers (OpenInfra Foundation, not CNCF), on QEMU and Firecracker

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
| None of these needed to break the isolation boundary | All four disclosures above: each abuses files, symlinks, sockets, allowlists or DNS. The 2026 hypervisor and runtime CVEs (Firecracker, Cloud Hypervisor, Kata, KVM Januscape, gVisor) are separate research, not agent escapes |
| agent-sandbox at v1.0 | v1.0.0 2026-08-28; latest v1.0.6 2026-10-08 |
| Claim-time identity and network policy are Planned | agent-sandbox roadmap.md, read 2026-10-11 |
| "Prevents escape even with root access" | Platform-First AI Agent Security abstract, KubeCon NA 2026 schedule |
| CNCF statuses | cncf/landscape, read 2026-10-11 |

Open items:

- The CFP page asks for the description in third-person sentences. The draft opens in second person ("Your coding agent") as the house style does and refers to Michael in the third person. Decide before pasting.
- Prior recordings: the speaker profile already lists both KubeCon EU 2026 Amsterdam talks on the CNCF YouTube channel.
- Speaker bio: Sessionize uses the profile bio (Accenture LearnVantage). The bio in this file is the older KodeKloud version and is not pasted.
- Co-presenter: none listed. The format allows two.
- Responsible replay: only public techniques, against patched releases or isolated lab clusters with pinned vulnerable versions. Coordinate anything new with the affected project before March.
