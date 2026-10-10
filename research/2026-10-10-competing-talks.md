# Competing Talks for a March 2027 KubeCon Talk on Securing AI Agents with agent-sandbox

The general idea of a "secure CNCF stack for agents" is heavily covered. The sharper angles are not: no talk found from March 2026 to March 2027 replays real coding-agent escapes against agent-sandbox and scores each layer, treats warm pools or pod snapshots as a place credentials leak, tests DNS tunneling or exfiltration to allowlisted hosts, explains what Falco/Tetragon can see inside gVisor/Kata guests, or joins OpenTelemetry GenAI spans with Falco and Hubble events. The closest competition is at KubeCon NA 2026 in Salt Lake City, on November 9 co-located events and in the keynotes, and covers isolation, identity, MCP tool-layer red-teaming and MCP audit tracing.

## TL;DR
- **Angle 6 (reference architecture) is heavily covered.** Talks on layered security, identity, sandboxes and guardrails ran at KubeCon EU 2026. More are scheduled at KubeCon NA 2026: "Sandbox Your Agents" (keynote), "The Harness Is the New Runtime" (keynote), "License to Generate" (Keycloak/SPIRE/Envoy), "Platform-First AI Agent Security" and "Detonation and Isolation". A sixth angle on its own would repeat ground already covered.
- **Angles 1, 3 and 5 are only lightly covered.** The nearest overlaps are a red-team of the MCP tool layer (not sandbox escapes), gateway-level egress governance plus one KyvernoCon demo in which a nono-proxy swaps a phantom token for the real credential (no DNS tunneling or allowlisted-host exfiltration), and an MCP audit proxy that sends OpenTelemetry spans to Jaeger (no kernel or Hubble events).
- **Angles 2 and 4 are uncovered.** Snapshots and checkpoint/restore come up only for performance and state continuity (Alibaba's Sandbox Operator, Agent Substrate, the Harness keynote), never as a credential-leak surface. No talk found covers Falco/Tetragon visibility inside gVisor or Kata guests.

## Key Findings
- **One KubeCon talk in the window is built on kubernetes-sigs/agent-sandbox: "Platform-First AI Agent Security" at NA 2026.** Per the LF schedule, it "presents a production-validated zero-trust architecture using kubernetes-sigs/agent-sandbox with gVisor/Kata runtime enforcement, KRO for declarative abstractions, and GitOps provisioning". Its speakers are unverified. Outside KubeCon, "Off the Laptop, Into Production: An Open Source Stack for AI Agents on Kubernetes" by Brian Hammons and Nirmal Mehta (AWS) was delivered on October 7, 2026 at Open Source Summit Europe in Prague. Its "inner loop" runs on "the kubernetes-sigs Agent Sandbox CRD, gVisor, and FQDN-aware egress via Cilium".
- **The NA 2026 SIG Apps Maintainer Track session ("Managing Data at Scale: Best Practices and Evolution of SIG-Apps") has not been confirmed to cover agent-sandbox.** No separate agent-sandbox maintainer session was found.
- **Agent Substrate, not agent-sandbox, has the most dedicated talks at NA 2026.** It has at least three: Christian Posta on the main track, Alex Van Boxel at Agentics Day, and Tim Hockin and Dmitry Berkovich's "Kubernetes Solutions for Agent-Shaped Problems" (Nov 10, 4:40 PM, Hall DE). All frame suspend/resume and snapshots as density and scale features.
- **MCP isolation and red-teaming is the busiest security sub-theme, and it sits at the protocol and tool layer.** The SAFE-MCP runtime proxy talk reports red-team results (tool-poisoning success cut "from 74% to under 9%"). That is a different layer from sandbox escape replay.
- **Falco, Tetragon and Cilium talks in the window are general project updates or end-user stories.** None found addresses agent workloads in sandboxed runtimes.

## 1. Competing Talks by Event (chronological)

### KubeCon + CloudNativeCon Europe 2026 — Amsterdam, March 23–26, 2026 (all delivered)

| Date | Title | Speakers (affiliation) | Link | What it covers | Overlap |
|---|---|---|---|---|---|
| Mar 23 (co-located/Mon; time unverified) | Agentic Networking: Securing AI Agents on Kubernetes | Evaline Ju (IBM Research), Haiyan Meng (Google) | Slides: hosted-files.sched.co/kccnceu2026/…/agentic-networking-kubecon-eu-2026.pdf; IBM Research publication page | Introduces Kube Agentic Networking, a SIG-Network subproject that extends Gateway API to govern agent→MCP, A2A and agent→LLM traffic. Covers deny-by-default authorization policies and gateway guardrails against prompt-injection exfiltration of PII. | Angle 3: partial; Angle 6: partial |
| Mar 23–24 (time unverified) | Project Lightning Talk: Urunc: The New Kid In The Block Of Sandboxed Container Runtimes | Charalampos Mainas (urunc maintainer) | kccnceu2026.sched.com | Maintainer introduction to urunc as a sandboxed runtime. | Angle 6: partial (isolation layer only) |
| Week of event (Project Pavilion) | Project Demo: Urunc: Fine-Grained Sandboxing for AI Agents | Speaker not verified | kccnceu2026.sched.com | Pavilion demo of urunc for agent sandboxing. **Speaker and abstract not verified.** | Angle 6: partial |
| Mar 24, 12:00 CET | In Falco's Nest: The Evolution of Cloud Native Runtime Security | Iacopo Rozzo (Sysdig), Aldo Lacuku (Kong) | kccnceu2026.sched.com; falco.org/blog/kubecon-eu-2026 | Falco maintainer update and new features. No evidence it covers agents or gVisor/Kata guest visibility. | Angle 4: none |
| Mar 23 (lightning) | Project Lightning Talk: Forensics With Falco | Gerald Combs (maintainer) | falco.org/blog/kubecon-eu-2026 | Using Falco with Stratoshark for container forensics. | None |
| Mar 25, 11:00 CET | Sandbox Operator: Enabling Session-Aware, Efficient MCP Tool Execution in Kubernetes | Mingshan Zhao, Zhen Zhang (Alibaba) | kccnceu2026.sched.com/event/2CW1c (slides attached) | Session-lifecycle sandbox pods for MCP tools. Uses "community Checkpoint/Snapshot mechanisms to persist tool state" for efficiency and continuity, not security. | Angle 2: partial (snapshot mechanics, no secret-leak analysis) |
| Not verified | Least-Privilege for AI: Authorizing Agents and MCP Tools with Agentgateway and Kyverno | Luc Chmielowski (Nirmata), Nina Polshakova (Solo.io) | kccnceu2026.sched.com (Hall 8, Room F) | Enforcing least privilege on MCP tool calls with Agentgateway plus Kyverno policy. | Angle 6: partial |
| Not verified | When an Agent Acts on Your Behalf, Who Holds the Keys? | Mariusz Sabath, Maia Iyer (IBM Research) | kccnceu2026.sched.com | kagenti: cryptographically binds an agent's SPIFFE/SPIRE identity to the user's delegated identity. | Angle 2: partial (identity binding, not at claim time); Angle 6: partial |
| Not verified | Keeping Your Agents in Check: Layered Security for Agentic Platforms in Production | Evaline Ju (IBM Research), Kelly Abuelsaad (IBM) | kccnceu2026.sched.com | Layered security from identity and authorization through guardrails at the Envoy gateway, against prompt injection and unauthorized tool access. | Angle 6: partial; Angle 3: light |
| Not verified | Jailed-Agents: Restrict Your AI Coding Agents' System Access | Not verified | Mentioned in codecentric recap only | Nix-based tool that runs coding agents in a restricted sandbox. **Title from a secondary recap; speaker and abstract not verified.** | Angle 1: light |
| Mar 24 (sponsor-hosted, separate registration) | Securing Autonomous AI Agents in Production (workshop) | Tigera | Tigera blog | Zero-trust security for AI workloads. A sponsor workshop, not a CFP talk. | Angle 3: light; Angle 6: light |
| Mar 25 or 26, 15:15 CET | From Logs to Decisions: Autonomous AI Agents for Real-Time Kubernetes Threat Response | Willem Berroubache (Orange) | kccnceu2026.sched.com | Agents used as defenders for threat response; the reverse of the planned talk. | None |
| Not verified (lightning) | OpenFGA For Agents: Safe Delegation In 5 Minutes | Andres Aguiar (maintainer) | kccnceu2026.sched.com | Fine-grained authorization for agent delegation. | None/light |

**Not verified:** some recaps say Google "announced the Kubernetes Agent Sandbox" in Amsterdam. No dedicated agent-sandbox session title was found on the EU 2026 Sched.

### Open Source Summit Europe 2026 — Prague, October 7–9, 2026 (co-located events October 5–6)

| Title | Speakers | Status | Link | What it covers | Overlap |
|---|---|---|---|---|---|
| Off the Laptop, Into Production: An Open Source Stack for AI Agents on Kubernetes | Brian Hammons, Nirmal Mehta (AWS) | Delivered (Wed Oct 7, 2026, 13:30–14:10 CEST, Forum Hall) | osselceu2026.sched.com (Open AI & Data track listing) | Running agents on Kubernetes. The "inner loop" runs on the agent-sandbox CRD, gVisor and FQDN-aware Cilium egress. Covers production gotchas from small developer-sandbox fleets up to large RL-scale fleets. | Angle 6: heavy; Angle 3: partial |
| Title not verified | Dotan Horovits | Not verified | Same listing | The full lifecycle of running agents on Kubernetes with open source: source control, CI/CD, observability, memory and tool access. | Angle 6: light |

### KubeCon + CloudNativeCon North America 2026 — Salt Lake City, November 9–12, 2026 (all scheduled)

**Co-located events, Monday November 9** (source: LF CNCF-hosted co-located schedule)

| Time (MST) | Title | Speakers | Event | Link | What it covers | Overlap |
|---|---|---|---|---|---|---|
| 9:10 AM | Handing a Proxy the Keys to Your Pod: Inside Cilium's Sidecarless mTLS | Quang Nguyen, Robin Gögge | CiliumCon | co-located schedule ?id=1268376 | Cilium ztunnel-based mTLS and SPIFFE identity issuance. Live demo of SPIRE binding a certificate to the requesting process and refusing a stolen cert. Not agent-specific. | None (identity mechanics only) |
| 9:45 AM | An Agent Is Not a Function Call (lightning) | Shaghayegh Moradirad | Cloud Native AI + Inference Day | ?id=1269652 | Uses the OpenAI Codex SDK to argue that agent APIs need control-plane primitives, including "sandbox policies for workspace access". | Angle 6: light |
| 10:40 AM | Securing the Agentic Tool Layer: A Runtime Defense Framework for MCP Agent Deployments | Saurabh Yergattikar, Harshul Jain | Agentics Day | ?id=1269818 | Threat taxonomy from 80+ SAFE-MCP techniques plus an inline runtime proxy. Red-team results across five model backends: tool poisoning "from 74% to under 9%". | Angle 1: partial (red-team method at MCP layer, not sandbox escapes); MCP isolation: partial |
| 10:40 AM | Don't Lose Your Agent's Mind: Platform Patterns for Stateful Agents | Evaline Ju, Maia Iyer | Platform Engineering Day | ?id=1266322 | Running Claude Code and Hermes harnesses on Kubernetes: durable sessions, crash recovery, state governance and a reference architecture. | Angle 2: light (state, not secrets); Angle 6: partial |
| 11:15 AM | Agentic GitOps: Agent and Sandbox Guardrails with Flux | Leigh Capili, Tamao Nakahara | FluxCon | ?id=1269797 | Confining agents to reviewable PRs, kernel sandboxing with `nono`, managing agent sandboxes with Flux, and agents requesting extra network access via PR. | Angle 3: light; Angle 6: light |
| 11:15 AM | Building Governance for Hybrid Architectures for Agentic Systems | Valentina Rodriguez Sosa | Agentics Day | ?id=1269246 | Kuadrant routing tier with SPIFFE/SPIRE identities so "external API keys are never exposed" and only validated agents reach model endpoints. | Angle 3: partial (gateway-held credentials, close to phantom tokens) |
| 11:15 AM | Traffic Handling Patterns in the Agentic Era | Pradheep Shrinivasan, Boteng Yao | Agentics Day | ?id=1268232 | Envoy native MCP gateway, per-user tool filtering, OPA, "safe egress controls for agent traffic" and Google's egress agent gateway policy. | Angle 3: partial |
| 11:50 AM | Cloud Native Agentic Standards: A Progress Report from the CNCF AI TCG (panel) | Vincent Caldeira, Josh Halley, Nimisha Mehta, Nina Polshakova | Cloud Native AI + Inference Day | ?id=1249491 | Standards checklist: MCP/A2A, SPIFFE/SPIRE identity, observability and governance. | Angle 6: partial |
| 12:55 PM | The Agent Did What? Reconstructing MCP Tool-Call Attacks | Jie Wu | Agentics Day | ?id=1249143 | Reproduces an indirect-prompt-injection exfiltration through MCP. An MCP audit proxy emits OpenTelemetry spans to Jaeger, which are then joined to cloud audit logs. | Angle 5: partial (OTel and audit join, no kernel or Hubble); Angle 3: light |
| 2:05 PM | Introducing Agent Substrate, Scaling Thousands of Stateful AI Agents on Kubernetes Without the Waste | Alex Van Boxel | Agentics Day | ?id=1254201 | Running mostly-idle stateful agents efficiently with Agent Substrate (suspend/resume onto worker pods). | Angle 2: light (mechanics, no security) |
| 2:40 PM | License to Generate: Securing AI Agents with Keycloak, SPIRE, and Envoy | Maia Iyer, Hai Huang (affiliations not shown; IBM likely, unverified) | Open Source SecurityCon | ?id=1268158 | "A working vendor-neutral, open-source implementation built on Keycloak, SPIRE, and Envoy that shifts AI security down to the platform layer". Covers identity, sandboxes and guardrails against prompt injection, privilege escalation and impersonation. | Angle 6: heavy; Angle 2: partial (identity) |
| ~4:30 PM (unconfirmed) | Detonation and Isolation: Hardening Kubernetes Runtimes for Agents | Syeda Anjum, Kaslin Fields, Kavitha Rajendran (affiliations not shown) | Agentics Day, Grand Ballroom IG | co-located schedule (no ?id found) | **Abstract not retrieved; time unconfirmed.** The title points to runtime hardening and isolation for agents, likely gVisor/Kata/RuntimeClass and possibly agent-sandbox. | Angle 6: likely heavy; Angle 1: possibly partial (**unverified**) |
| 8:30 AM (sponsor, separate reg.) | Building, Scaling + Running Secure Agents on Kubernetes with AWS (workshop) | AWS | Off-site, Kimpton Monaco | Main schedule | Security model for agents on EKS: "trust and isolation when code generates and executes further code autonomously", blast radius and least privilege. | Angle 6: partial |
| 2:00 PM (sponsor, separate reg.) | Discovering and Securing AI Agents in Kubernetes (workshop) | Peter Kelly (CTO, Tigera) | Off-site, Le Méridien | Main schedule | Agent discovery, registration with identity, and tool/data-level policy run in observation mode before enforcement. | Angle 6: partial; Angle 3: light |

**Main conference, November 10–12**

| Date/Time | Title | Speakers | Track | What it covers | Overlap |
|---|---|---|---|---|---|
| Nov 10, 9:35 AM | Engineering Kubernetes for the Next Era of Compute (sponsored keynote) | Mike Stefaniak (affiliation not shown) | Keynote | containerd and scale fixes. Previews "how untrusted, ephemeral code can earn true VM-grade isolation at the level of a single pod". | Angle 6: light |
| Nov 10, 9:55 AM | Sandbox Your Agents (sponsored keynote) | Jessica Forrester (affiliation not shown) | Keynote | Isolating agentic workloads at scale with Confidential Containers, OpenShell and "secure, containerized sandboxes". | Angle 6: partial |
| Nov 10, 10:20 AM | The Harness Is the New Runtime (sponsored keynote) | Idit Levine, Keith Babo (affiliations not shown) | Keynote | Bringing agent harnesses onto clusters using Kubernetes primitives for "sandboxed execution, checkpoint/restore, scale, and security", plus CNCF identity, policy and observability. | Angle 6: partial; Angle 2: light |
| Nov 10, 11:30 AM | New Traffic, New Rules: Standardizing AI-Aware Networking in Kubernetes | Nir Rozenbaum, Keith Mattix | Maintainer Track (AI Gateway WG) | AI Gateway WG designs: payload processing, external model egress and Gateway API mapping. | Angle 3: light |
| Nov 10, 11:30 AM | Your Agent Needs a Platform: Cloud Native Infrastructure for Multi-Agent AI Systems | Soham Ghadge | AI Inference + Agentic | Agents as CRDs, Dapr durability, NATS messaging, "end-to-end observability using OpenTelemetry traces across agent hops" and audit logging. | Angle 5: light |
| Nov 12, 10:05 AM | The Identity Crisis: Who is the AI Agent in Your Cluster? (keynote) | Abdel Sghiouar (Google Cloud) | Keynote | The identity and resource crisis of non-deterministic agents running machine-generated code on Kubernetes. | Angle 2: light (identity); Angle 6: light |
| Date unverified, 2:20 PM | Pods Are Not Enough for AI Agents, Meet Agent-substrate | Christian Posta (affiliation not shown; Solo.io likely, unverified) | AI Inference + Agentic | Bursty, pausing agents need a runtime layer on top of Kubernetes. Agent Substrate actor/worker scheduling. | Angle 2: light |
| Date unverified, 4:40 PM | Lima as the Universal AI Sandbox | Akihiro Suda (NTT) | Maintainer Track (Lima) | Lima VMs for sandboxing AI agent workloads on any host OS. Local, not Kubernetes. | Angle 6: light (non-K8s) |
| Date/time/speakers unverified | Platform-First AI Agent Security: Zero-Trust Patterns for Kubernetes | **Speakers not verified** | Security | Running agents "that execute arbitrary code with shell access". KRO-based CRDs, and "treating AI agents as untrusted tenants—not trusted services". | Angle 6: heavy |
| Nov 12 (title unverified) | Falco Maintainer Track | Not verified | Maintainer Track | Abstract opens "Falco has never flown alone." **Title, speakers and agent coverage not verified.** | Angle 4: unknown |
| Date unverified | Managing Data at Scale: Best Practices and Evolution of SIG-Apps | Not verified | Maintainer Track | SIG Apps update. **Whether it covers agent-sandbox is not verified.** | Angle 6: unknown |
| Nov 12, 11:00 AM | Agentic + Cloud Native: Getting Started Contributing to Kagent | Not captured | Contribfest/tutorial | kagent contribution onboarding. | None |

### KubeCon China / Japan / India 2026; KubeCon EU 2027 (Barcelona); Rejekts; KCDs; CNCF webinars; SOSS Community Day; AI_dev; CNCF YouTube
No competing talks were identified for these events, and they were not fully searched (see Caveats). No public KubeCon EU 2027 schedule or accepted-talk list was found.

## 2. Overlap Matrix (coverage as of March 2027)

| Angle | Talks that touch it | Rating |
|---|---|---|
| 1. Red Team the Sandbox (replay real coding-agent escapes vs. naive/hardened agent-sandbox, score each CNCF layer) | Securing the Agentic Tool Layer (MCP-layer red team); Detonation and Isolation (title only, abstract unverified); Jailed-Agents (unverified) | **Lightly covered.** Nobody replays config-file, symlink, Docker-socket, allowlisted-command or DNS-exfil escapes against agent-sandbox. Detonation and Isolation is the one unknown that could change this. |
| 2. Warm pools / snapshots as credential caches; identity at claim time | Sandbox Operator (Alibaba, checkpoint for state); Agent Substrate ×2; Harness keynote (checkpoint/restore); Don't Lose Your Agent's Mind; identity talks (kagenti, License to Generate, Identity Crisis) | **Uncovered** for the security angle. Snapshots appear only as performance/state features, and identity talks don't address binding at SandboxClaim time. |
| 3. Egress as the real boundary (assume-compromised; DNS tunneling, allowlisted-host exfil, phantom tokens) | Agentic Networking (EU); Traffic Handling Patterns; Building Governance (keys never exposed); AI Gateway WG; Agentic GitOps; OSS EU AWS talk (FQDN Cilium egress); After Admission: Kernel Enforcement for Agents Kyverno Let In (Sal Kimmich, KyvernoCon, Nov 10, 3:15 PM; phantom-token swap by nono-proxy) | **Lightly covered.** Gateway governance and FQDN allowlisting are presented as solutions, and one live demo shows a phantom token being swapped for the real credential so "the agent never holds the credential". Bypassing the boundary (DNS tunneling, exfil via allowlisted hosts) is not covered. |
| 4. Detection inside gVisor/Kata guests (Falco/Tetragon visibility) | Falco maintainer tracks (EU 2026, NA 2026) | **Uncovered** |
| 5. Unified audit trail (OTel GenAI spans + Falco + Cilium/Hubble) | The Agent Did What? (OTel MCP spans + cloud audit logs); Your Agent Needs a Platform (OTel across hops) | **Lightly covered.** No kernel or network-flow join. |
| 6. Reference architecture on agent-sandbox | License to Generate; Platform-First AI Agent Security; Detonation and Isolation; Sandbox Your Agents; Harness keynote; Keeping Your Agents in Check; Least-Privilege for AI; AI TCG panel; OSS EU AWS agent-sandbox talk; AWS and Tigera workshops | **Heavily covered** as a theme. Two talks are explicitly built on agent-sandbox: Platform-First AI Agent Security at KubeCon NA 2026 ("using kubernetes-sigs/agent-sandbox with gVisor/Kata runtime enforcement") and the delivered OSS EU talk "Off the Laptop, Into Production" by Hammons and Mehta (AWS). |

## 3. KubeCon NA 2026 (Salt Lake City): What Is Scheduled and What It Will Establish

**Scheduled on these topics:** The densest cluster is the Nov 9 Agentics Day "Security + Trust + Reliability" track: Securing the Agentic Tool Layer, The Agent Did What?, Detonation and Isolation, plus the governance and traffic talks. It is joined by License to Generate at Open Source SecurityCon and three Nov 10 keynotes that put agent sandboxing on the main stage (Sandbox Your Agents, The Harness Is the New Runtime, and Engineering Kubernetes for the Next Era of Compute). Main-track sessions add Platform-First AI Agent Security, Pods Are Not Enough (Agent Substrate) and Lima as the Universal AI Sandbox, and the Nov 12 keynote The Identity Crisis.

**Projection: what will count as "already covered" by March 2027, based on the abstracts:**
- **"Agents are untrusted tenants and need sandboxed or VM-grade runtimes."** This will be stated from the keynote stage (Sandbox Your Agents, Next Era of Compute) and in Platform-First and Detonation and Isolation. An intro motivating runtime isolation will read as familiar.
- **"Identity for agents = SPIFFE/SPIRE + OAuth (Keycloak) + Envoy enforcement."** License to Generate gives a working implementation, and the Identity Crisis keynote frames the problem. Generic agent-identity material will be seen as covered.
- **"MCP tool poisoning is mitigated by an inline runtime proxy."** Quantified red-team numbers already exist (74% → under 9%). MCP isolation without a sandbox-layer angle will look derivative.
- **"OpenTelemetry spans can reconstruct an MCP attack."** The Agent Did What? sets this baseline. Angle 5 has to go beyond MCP spans plus cloud audit logs by adding Falco syscall events and Hubble flows.
- **"Suspend/resume and checkpoint/restore make idle agents cheap."** Two Agent Substrate talks and the Harness keynote cover the mechanics. No abstract examines what secrets persist inside those snapshots, so angle 2 stays open.
- **"Gateway-level egress governance for agents."** Traffic Handling Patterns and Building Governance cover allowlisting and gateway-held keys. Bypassing that boundary is not covered.
- **Main risk:** the Detonation and Isolation abstract is unverified. If it includes escape testing against hardened runtimes, angle 1 moves toward partial or heavy coverage.

## 4. What Remains Uncovered
- Replaying real 2026 coding-agent escape techniques (config files, symlinks, Docker socket, allowlisted commands, DNS exfiltration) against a naive vs. hardened agent-sandbox
- Per-layer scoring of which CNCF control stopped, detected or missed each technique
- SandboxWarmPool / pod snapshot memory as a credential cache; secrets in checkpoint/restore images
- Identity binding at SandboxClaim time (vs. pre-warmed pod identity)
- DNS tunneling out of an agent sandbox
- Exfiltration through allowlisted hosts (e.g., package registries, git hosts, model APIs)
- Phantom-token / credential injection at an egress proxy tested as an attack surface under assume-compromise. Sal Kimmich's KyvernoCon talk "After Admission: Kernel Enforcement for Agents Kyverno Let In" (Nov 10, 3:15 PM) demos the defensive pattern: the agent "calls the API server anyway, with a phantom token nono-proxy swaps for the real one, so the agent never holds the credential."
- What Falco and Tetragon can and cannot see inside gVisor and Kata guests
- A joined audit trail of OpenTelemetry GenAI spans + Falco kernel events + Cilium/Hubble egress flows
- A talk that treats agent-sandbox's own CRDs (SandboxTemplate/SandboxClaim/SandboxWarmPool) as the security core. Platform-First AI Agent Security uses kubernetes-sigs/agent-sandbox with gVisor/Kata, KRO and GitOps, but its abstract does not single out claim-time or warm-pool security.

## Caveats
- **Coverage gaps:** Search budget ran out before KubeCon China, Japan and India 2026, Cloud Native Rejekts (EU/NA 2026), KCDs, CNCF webinars/Online Programs, OpenSSF SOSS Community Day, Open Source Summit NA, AI_dev and the CNCF YouTube archive could be checked systematically. Talks at those events may exist.
- **Unverified items (flagged in the tables):** the Detonation and Isolation abstract and time; Platform-First AI Agent Security speakers, date and room; the dates of the Pods Are Not Enough and Lima sessions; several affiliations on the NA schedule; the Falco NA maintainer-track title; whether the SIG Apps session covers agent-sandbox; the urunc demo speaker; Jailed-Agents details; the title of Dotan Horovits's OSS EU 2026 session; and exact times for several EU 2026 sessions.
- **Schedules change:** the NA 2026 schedule is marked subject to change, and sponsor-hosted workshops are not CFP-reviewed talks.
- **Outside the window:** the FOSDEM 2026 Lima talk (February 2026) and the KubeCon NA 2025 agent-sandbox launch session were excluded.
