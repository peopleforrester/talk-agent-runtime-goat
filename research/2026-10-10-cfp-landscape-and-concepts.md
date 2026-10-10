# A Third KubeCon Talk on kubernetes-sigs/agent-sandbox: Stack, Landscape, Pain Points, and a CFP That Closes Tomorrow

**The most urgent finding: the KubeCon + CloudNativeCon Europe 2027 (Barcelona, 15–18 March 2027) CFP closes Sunday 11 October 2026 at 11:59 PM CEST — roughly 36 hours from now — and CNCF rules mean you can be listed on at most three proposals and selected for only one non-panel session, so a third talk competes directly with your two existing ones.** The strongest differentiated angle is an adversarial, measured "red team the sandbox" talk that treats agent-sandbox as necessary-but-insufficient and shows which CNCF layers actually stop the 2026 bypass classes; the "zero-trust reference architecture with agent-sandbox" angle is already taken at KubeCon NA 2026.

## TL;DR

- **Logistics dominate the decision.** EU 2027 main CFP closes 11 Oct 2026 (notifications 7 Dec, schedule 9 Dec); CNCF-hosted co-located events (Cloud Native AI + Inference Day, Agentics Day: MCP + Agents, Open Source SecurityCon, etc.) close 18 Oct 2026; Cloud Native Rejekts EU 2027 (13–14 March, Barcelona) CFP runs 7 Dec 2026 – 3 Jan 2027. Because only one non-panel session per speaker can be accepted at the main event, submit the third talk to the main CFP only if it is stronger than one of your existing two — otherwise aim it at a co-located event or Rejekts.
- **"Pure CNCF" breaks at the isolation layer.** agent-sandbox (a Kubernetes SIG Apps subproject, v1.0.x) delegates isolation to RuntimeClass; the two first-class backends, gVisor (Google) and Kata Containers (OpenInfra), are not CNCF projects. The only CNCF-hosted strong-isolation options are KubeVirt (incubating since 19 April 2022), urunc (sandbox, unikernels) and Confidential Containers, which cncf.io shows moved to Incubating on 8 July 2026 (it still runs on Kata). Say this out loud in the abstract — reviewers will respect the honesty more than a forced "100% CNCF" claim.
- **Best-chance concept:** "Red Team the Sandbox: Real 2026 Agent Escapes vs. a Naive and a Hardened agent-sandbox" (Security track), built around the fact that 2026's real coding-agent escapes went around sandboxes (config files, symlinks, sockets, allowlisted commands, DNS), with measured before/after results per CNCF layer. Underexplored runners-up: the warm-pool/snapshot identity-and-secrets problem, and egress-plus-credential-injection where the sandbox is assumed already compromised.

## Key Findings

1. **The CFP window is effectively closed for anything not already drafted.** The official CFP page states "Submissions are due by 11 October at 11:59 PM CEST (UTC+2)" and lists notifications on Monday 7 December and schedule announcement Wednesday 9 December. The same page says "You are allowed to be listed as a speaker on a maximum of three proposals submitted to the CFP, regardless of the format. You may only be selected to speak on one panel and one non-panel session per event (excluding any project benefits)." If your Whitney Lee and Jeremy Morgan talks are both being submitted to EU 2027 with you listed, a third submission uses your last slot and can, at best, displace one of them. The CFP also explicitly warns against "low-effort, AI-generated proposals."
2. **EU 2027 has a dedicated Agentic AI track** whose description explicitly asks for "identity and security, governance, observability, and production experiences running agentic workloads on Kubernetes" and encourages "interoperability across open source ecosystems." The Security track asks for "threat modeling… identity and credential management, multi-tenancy… incident post-mortems." A sandbox-security talk fits either; Security is the less crowded choice.
3. **Correction to your brief:** KubeCon NA 2026 is in **Salt Lake City (9–12 November 2026, Salt Palace)**, not Atlanta. Atlanta was NA 2025, where agent-sandbox launched. NA 2027 is New Orleans (8–11 November 2027); EU 2028 is Berlin (24–27 April 2028).
4. **agent-sandbox is real, moving fast, and still churning.** v1.0.0 shipped 2026-08-28; v1.0.2 (11 Sep 2026) already carried breaking changes (the sandbox-router `Authorizer` interface signature changed, and router manifests moved from `default` to `agent-sandbox-system`). Image promotion records show v1.0.6 promoted on 8 October 2026, so "v1.0.4 is latest" is already outdated. One independent tracker warns the project is "not for anyone expecting the 1.0 tag to mean a frozen API."
5. **The roadmap's security-relevant items are mostly still "Planned"**: Sandbox/Pod Identity Association at claim time, Network Policy "attach" at claim time (L4/L7 egress and FQDN allowlists), auto suspend/resume and scale-to-zero, a first-class router, and an Agent Sandbox MCP server. "Decouple API from Runtime (Portable Backend)" via KEP #597 and KEP #747 is in progress. These gaps are exactly what a security talk should exploit — and some may land before March 2027, which is both a risk (your demo could go stale) and an opportunity (you can demo the new features).
6. **Upstream Kubernetes moved under the project.** User Namespaces went GA in Kubernetes v1.36 (April 2026). Kubernetes v1.37 (released 26 August 2026) introduced alpha pod-level checkpoint/restore (KEP-5823, new CRI `CheckpointPod`/`RestorePod` RPCs, same-node only), while forensic container checkpointing (KEP-2008) remains beta. Runtime support in containerd and Kata was still being built as of August 2026. Snapshots of agent memory are a new place for credentials to leak — an angle almost no one is talking about.
7. **The talk landscape is filling up fast around "how to run agent-sandbox securely."** NA 2026 already has a sponsored keynote ("Sandbox Your Agents"), a kagent sandboxing lessons-learned talk, an agent-substrate deep dive, and a "production-validated zero-trust architecture using kubernetes-sigs/agent-sandbox with gVisor/Kata runtime enforcement, KRO for declarative abstractions, and GitOps provisioning." A generic reference-architecture talk in March 2027 will look like a rerun.

## Details

### 1. Best pure-CNCF stack for secure agent execution (as of October 2026)

Maturity labels below are CNCF levels unless noted. Items marked "verify" are from my knowledge and were not re-confirmed against cncf.io in this research pass — check the CNCF project page before putting them on a slide.

| Layer | Recommended choice | Alternatives | CNCF / governance status | Honest note |
|---|---|---|---|---|
| Isolation runtime | gVisor (default) or Kata Containers via RuntimeClass, behind containerd | KubeVirt VMs; urunc (unikernels); Confidential Containers; Kata + Firecracker (`kata-fc`) | gVisor: Google OSS, **not CNCF**. Kata: OpenInfra, **not CNCF**. containerd and CRI-O: graduated. KubeVirt: incubating (cncf.io: accepted 6 September 2019, moved to Incubating 19 April 2022). urunc: sandbox (accepted 22 May 2025). Confidential Containers: incubating (cncf.io: moved to Incubating 8 July 2026; CNCF blog, 22 July 2026), runs on Kata | **This is where "pure CNCF" breaks.** KubeVirt is the only CNCF-hosted VM boundary, but agent-sandbox only orchestrates Pods today; issue #1650 proposes a separate pluggable layer for non-Pod sandboxes such as KubeVirt VMs. urunc is promising but early (173 GitHub stars, "Fair (60)" health score on cncf.io). |
| Orchestration | kubernetes-sigs/agent-sandbox v1.0.x (Sandbox, SandboxTemplate, SandboxClaim, SandboxWarmPool) | agent-substrate (actor multiplexing on gVisor checkpoints); kagent's substrate runtime | Kubernetes SIG Apps subproject (inherits Kubernetes' graduated governance; not a separate CNCF project). agent-substrate: standalone, **not SIG or CNCF** | Warm pools give sub-second claims; the upstream roadmap targets claim latency of 200 ms → 100 ms → 50 ms and 1,000+ claims/sec. Auto suspend/resume and scale-to-zero are still "Planned" upstream; GKE gets this today via Pod Snapshots. |
| Workload identity | SPIFFE/SPIRE | Kubernetes projected service-account tokens; cloud workload identity | SPIFFE and SPIRE: graduated | Multiple KubeCon EU 2026 talks built agent identity on SPIRE attestation (e.g., IBM Research's kagenti). The gap is identity at **claim time** for pre-warmed pods — upstream "Sandbox / Pod Identity Association" is still Planned. |
| Secrets and credential injection | Credentials stay outside the sandbox; inject at the egress proxy. External Secrets Operator to sync from the store; cert-manager for mTLS/short-lived certs | OpenBao (Vault fork) as the store; phantom-token proxies such as nono-proxy | cert-manager: graduated (announced by cert-manager on 12 November 2024). ESO: sandbox (cncf.io: accepted 26 July 2022; incubation application filed as cncf/toc issue #1486). OpenBao: Linux Foundation / OpenSSF, **not CNCF** | No CNCF-native secrets store exists; OpenBao is the open, non-HashiCorp option. The "brain outside, hands inside" pattern is already in production at kagent ("Credentials can be injected on egress from agentgateway"). |
| Network egress | Cilium (FQDN-aware network policy) default-deny, plus an L7 egress gateway for credential injection | Envoy / Envoy AI Gateway; Istio ambient waypoints; kgateway; agentgateway; Kubernetes Gateway API | Cilium, Envoy, Istio: graduated. Gateway API: Kubernetes SIG Network. kgateway: sandbox. Envoy AI Gateway: Envoy subproject. **agentgateway: Agentic AI Foundation / Linux Foundation, not CNCF** (v1.3.0 GA 2026-06-18, per your own repo's issue #388) | Note: the GKE Agent Sandbox hardening policy can block sandboxes that use service-mesh sidecars, so ambient/node-level enforcement is the safer bet with gVisor. Per-claim FQDN policy is still on the upstream roadmap. |
| Admission policy | Kyverno (enforce RuntimeClass, `hostUsers: false`, no hostPath/Docker socket, template pinning) | OPA Gatekeeper; built-in ValidatingAdmissionPolicy (CEL) | Kyverno: graduated (CNCF announced its graduation on 24 March 2026, at KubeCon EU Amsterdam). OPA: graduated. VAP: in-tree Kubernetes | Overlaps with your Whitney Lee guardrails talk — keep admission to one slide in the new talk. |
| Runtime detection | Falco (gVisor has a Falco integration) | Tetragon (eBPF; note that host eBPF sees less inside gVisor/Kata guests) | Falco: graduated. Tetragon: Cilium subproject | Detection inside gVisor/Kata is an under-documented gap; "propagate Falco configuration for gVisor sandbox" sat on the upstream backlog. Good demo material. |
| Supply chain | in-toto attestations + Notary/Sigstore signatures on sandbox images, SLSA provenance, verified at admission | — | in-toto: graduated. Notary: incubating. TUF: graduated. **Sigstore and SLSA: OpenSSF, not CNCF** | Cheap to add, low novelty on stage; one slide. |
| Observability and audit | OpenTelemetry (GenAI semantic conventions) → Jaeger, correlated with Falco/Tetragon kernel events | Prometheus metrics from the agent-sandbox controller (added via controller-runtime v0.25.0 in v1.0.2) | OpenTelemetry: incubating. Jaeger: graduated | OTel tracing of the sandbox runtime APIs is a roadmap item, not done. GenAI semconv is still evolving — mark it as unstable. |
| MCP isolation and gateways | Run each MCP server in its own Sandbox; front it with an MCP-aware gateway | agentgateway; Kuadrant MCP gateway; kagent/kmcp; ToolHive | Kuadrant: sandbox (accepted 19 June 2024). kagent: sandbox. agentgateway: AAIF/LF. ToolHive: vendor (Stacklok) OSS, **not CNCF** (verify) | The Agent Sandbox MCP server is still Planned upstream. |
| Agent frameworks on Kubernetes | kagent (CNCF sandbox, accepted 22 May 2025) for ops agents; OpenHands (integrated with agent-sandbox in v1.0.1) for coding agents | Dapr Agents; KServe and llm-d for model serving | kagent: sandbox. Dapr: graduated. KServe: incubating. llm-d: sandbox | Frameworks aren't security boundaries; keep them as the "brain outside." |
| Multi-tenancy | Namespace-per-tenant + agent-sandbox templates + default-deny network policy | Capsule; vCluster | Capsule: sandbox (cncf.io: accepted 13 December 2022). **vCluster: Loft Labs OSS, not CNCF** | Hard multi-tenancy for mutually untrusted tenants still needs a VM boundary (Kata/KubeVirt). |

**Interpretation:** a defensible "CNCF-first" claim is: *every control plane, policy, identity, network, detection and observability layer is CNCF-graduated or CNCF/Kubernetes-governed; the isolation boundary is a pluggable RuntimeClass where the best options are non-CNCF open source (gVisor, Kata) or a CNCF-incubating VM layer (KubeVirt) that agent-sandbox doesn't yet orchestrate natively.* Make that your thesis slide instead of hiding it.

### 2. State and roadmap of agent-sandbox

**Releases and status (as of 10 Oct 2026):**
- Launched by Google at KubeCon NA 2025 (Atlanta) as a SIG Apps subproject; Kubernetes blog introduction 20 March 2026 by Janet Kuo and Justin Santa Barbara.
- Core API went to v1beta1 in v0.5.0 (June 2026) according to a third-party write-up; v1.0.0 shipped 28 Aug 2026; v1.0.1 (3 Sep) added a TypeScript SDK and a first-class OpenHands workspace integration; v1.0.2 (11 Sep) added Ed25519 scoped-token v2 binding tokens to Sandbox UID, port, HTTP method and exact path, a direct in-cluster connectivity option in the Go SDK, and RL warm-pool adoption; v1.0.3 (17 Sep) added configurable TLS controls, sandboxd process-group cleanup, and "execution-scoped credentials and egress-policy blueprints" (per a third-party tracker); v1.0.4 (24 Sep); v1.0.6 image promoted 8 Oct 2026.
- Repo signals (third-party tracker, 27 Sep 2026): about 4,037 stars, 528 forks, 202 open issues and PRs, 24 releases since October 2025.
- Install paths: kubectl manifests, Helm, OLM/OperatorHub (publication readiness work in v0.5.3).

**Maintainers** (inferred from Prow approval comments, not read from the OWNERS file): root approvers **janetkuo (Janet Kuo), justinsb (Justin Santa Barbara), barney-s**; subdirectory approvers include aditya-shantanu, vicentefb and shruti6991. The project is Google-led — worth knowing because reviewers may read a talk that only uses GKE as vendor-flavored.

**Integrations and adoption signals:**
- **GKE Agent Sandbox** GA on 20 May 2026, claiming 16x sandbox growth in under five months and Langchain and Lovable as users (from Google's own blog, relayed by bex.co — vendor numbers).
- **Red Hat build of Agent Sandbox** (Tech Preview, July 2026) pairs it with OpenShift sandboxed containers (Kata). Notably, Red Hat's own article says agent-sandbox "does not by itself provide a hardened security boundary."
- **Kata Containers** blog announced the Kata integration; the repo ships a Firecracker example (`kata-fc`) behind a warm pool.
- **AWS** builder content documents agent-sandbox on EKS with gVisor and Kata+Firecracker.
- **kagent / Solo.io:** NA 2026 talk on sandboxing agents with OpenShell, agent-sandbox and Google's substrate.
- **Northflank, Cloudfleet, Pulumi** have published how-to guides (vendor content).
- I did **not** confirm a Coder integration — treat it as unverified.

**Likely state by March 2027 (my assessment, not project commitments):**
- More v1.x releases, probably including at least one of: per-claim network policy attach, claim-time identity association, or auto suspend/resume. These are the most-requested items and are already in progress or planned.
- Portable backend (KEP #597/#747, the "sandboxd" data-plane contract) is likely further along; non-Pod backends (KubeVirt) are unlikely to be production-ready.
- Kubernetes v1.38 is scheduled for release on Wednesday 16 December 2026 according to the kubernetes/sig-release release-1.38 schedule (code freeze 19 November 2026; v1.38.0-alpha.2 was tagged 7 October 2026), and it may advance pod-level checkpoint/restore. GPU checkpoint/restore (KEP-6274) is provisional, targeting alpha in v1.38.
- **Implication for you:** build the demo so it pins versions, and plan a "what changed since I submitted" slide. Reviewers like proposals that anticipate their own staleness.

### 3. What practitioners are struggling with

| Pain point | Evidence (dated) | Strength of evidence |
|---|---|---|
| Cold start vs. isolation strength | AWS Builder Center (2026): gVisor "added negligible launch latency" but Kata+Firecracker "cold start was around 5 seconds per sandbox," and EKS Managed Node Groups "do not work yet" for nested virtualization | Strong, first-party measurement |
| Many teams skip strong isolation entirely | codecentric KubeCon EU 2026 recap: "many teams simply run these agents as containers in their existing Kubernetes clusters" | Moderate, anecdotal |
| Sandbox ≠ security boundary | Red Hat (15 Jul 2026): agent-sandbox "does not by itself provide a hardened security boundary"; ARMO: prompt-injection exfiltration through permitted tools happens without escaping the container | Strong (Red Hat); ARMO is vendor marketing for behavioral detection |
| Egress control and per-session policy | Upstream roadmap: "Network Policy 'Attach' at Claim Time" is Planned; bex.co (24 Sep 2026): egress enforcement and FQDN allowlists are "what you still own" | Strong (primary roadmap) |
| Credential handling | kagent/Solo.io: credentials injected on egress via agentgateway; nono phantom-token proxy pattern being adopted by other projects; NA 2026 has a session on swapping a phantom token for the real one at the proxy | Strong signal of convergence on "brain outside" |
| Identity for pre-warmed sandboxes | Roadmap "Sandbox / Pod Identity Association" (Planned): identity must be bound when the claim happens, not when the pod boots | Strong (primary) |
| Density and idle cost | CNCF blog (Lin Sun, 7 Jul 2026): "Sandboxing your agents is necessary, but not sufficient"; agent-substrate claims 30x+ oversubscription; bex.co relays a community cost model of about $73k/month at E2B/Daytona rates vs. $5–15k self-hosted for 1,000 concurrent runs | Moderate; the cost model is unverified |
| GPU in sandboxes | bex.co (4 Sep 2026): gVisor GPU support "thins to an allowlisted proxy" while Kata passes the whole card through VFIO; GPU checkpoint/restore is only a provisional KEP | Moderate |
| Service mesh friction | GKE docs: sandboxes using an Envoy/Istio sidecar may be blocked by the hardening policy | Strong (primary) |
| Agent config and file tampering | NVIDIA AI Red Team guidance: block writes to agent configuration files and extensions, and sandbox hooks, MCP startup scripts and skills too | Strong; matches the 2026 escapes in your brief |
| API churn | v1.0.2 breaking changes; tracker warns 1.0 ≠ frozen API | Strong (primary release notes) |
| Detection inside sandboxes | Falco-for-gVisor configuration propagation sat on the backlog (issue #252) | Moderate |

I could not get Reddit r/kubernetes, Hacker News or Kubernetes Slack threads in this pass; the table relies on vendor, CNCF and project sources. Treat "what practitioners say" as partially inferred.

### 4. Competitive landscape of talks

| Event | Talk / session | Speakers | Angle |
|---|---|---|---|
| KubeCon NA 2025 (Atlanta) | Agent Sandbox launch / technical deep dive | Google (SIG Apps) | Introduction |
| KubeCon EU 2026 (Amsterdam) | Least-Privilege for AI: Authorizing Agents and MCP Tools with Agentgateway and Kyverno | Luc Chmielowski (Nirmata), Nina Polshakova (Solo.io) | MCP authz policy |
| KubeCon EU 2026 | Project Lightning Talk: Urunc: The New Kid In The Block Of Sandboxed Container Runtimes; Project Demo: Urunc: Fine-Grained Sandboxing for AI Agents | Charalampos Mainas (urunc maintainer) | CNCF-native runtime |
| KubeCon EU 2026 | Three Shades of Isolation: A Multi-tenancy Fortress | Braulio Dumba, Paolo Dettori (IBM) | Multi-tenancy |
| KubeCon EU 2026 | When an Agent Acts on Your Behalf, Who Holds the Keys? | Mariusz Sabath, Maia Iyer (IBM Research) | SPIFFE agent identity (kagenti) |
| KubeCon EU 2026 | First Agentics Day: MCP + Agents (co-located) | various | MCP |
| KubeCon Japan 2026 (Yokohama) | Kata-based agent sandbox (Xolis) on agent-sandbox + Kata 4.0 + PVM | Kata community members | Kata runtime |
| KubeCon NA 2026 (Salt Lake City) | Keynote: Sandbox Your Agents (sponsored) | Jessica Forrester | Confidential Containers + OpenShell |
| KubeCon NA 2026 | Keynote: The Harness Is the New Runtime | Idit Levine (Solo.io) | Harnessed agents, checkpoint/restore |
| KubeCon NA 2026 | Keynote: The Identity Crisis: Who is the AI Agent in Your Cluster? | (not retrieved) | Agent identity |
| KubeCon NA 2026 | Lessons Learned Sandboxing Agents with kagent | (Solo.io/kagent; names not retrieved) | OpenShell, agent-sandbox, substrate |
| KubeCon NA 2026 | Zero-trust architecture with agent-sandbox + gVisor/Kata + KRO + GitOps (title not retrieved) | (not retrieved) | **Reference architecture — your idea #2 is taken** |
| KubeCon NA 2026 | agent-substrate deep dive with kagent | (not retrieved) | Density |
| KubeCon NA 2026 | Phantom-token credential proxy (nono-proxy) for agents calling the API server (title not retrieved) | (not retrieved) | **Credential injection — partly overlaps idea "brain outside"** |
| KubeCon NA 2026 | Integrating Envoy AI Gateway and Kyverno Authz for Realtime Governance of LLM and MCP Traffic | (speaker attribution uncertain) | Gateway governance |
| NA 2026 co-located | Agentic GitOps: Agent and Sandbox Guardrails with Flux; Introducing Agent Substrate…; agentgateway patterns (Cisco, Google egress agent gateway); Backstage MCP token exchange (RFC 8693); CNCF AI TCG agentic standards progress report (Vincent Caldeira, Josh Halley, Nimisha Mehta, Nina Polshakova) | various | Guardrails, density, gateways, identity |
| NA 2026 sponsor events | AWS workshop "Building, Scaling + Running Secure Agents on Kubernetes"; Vultr "Agent Rush" sandboxed-agent hackathon | vendors | Hands-on |

I could not open the kccncna2026.sched.com schedule directly, so speaker names for several NA 2026 sessions are missing, and there may be more agent-sandbox talks than listed. Before submitting, spend 10 minutes searching Sched for "sandbox," "gVisor," "Kata," and "egress."

**Saturated angles:** "What is agent-sandbox," gVisor vs. Kata comparisons, zero-trust/GitOps reference architectures, kagent sandboxing, MCP authorization with gateways + Kyverno, SPIFFE-based agent identity.

**Underexplored angles:**
1. Adversarial, measured evaluation of agent-sandbox against the 2026 bypass classes (config, symlink, socket, allowlist, DNS).
2. Warm-pool and snapshot security — identity and secrets in pre-warmed pods and in pod checkpoints.
3. Detection *inside* gVisor/Kata guests (what Falco/Tetragon can and can't see).
4. Audit trails that join OTel GenAI spans to kernel and egress events into one "what did the agent actually do" record.
5. An honest "how CNCF-native can the isolation layer be?" look at KubeVirt/urunc vs. gVisor/Kata.

### 5. CFP logistics

| Venue | Date / location | CFP window | Status on 10 Oct 2026 |
|---|---|---|---|
| KubeCon + CloudNativeCon EU 2027 | 15–18 Mar 2027, Barcelona (venue reported as CCIB by a third-party site; official page didn't name it) | Opened ~10 Aug 2026; **closes Sun 11 Oct 2026, 23:59 CEST** | **Open ~36 hours.** Notifications 7 Dec, schedule 9 Dec. 30-min sessions for 1–2 speakers; 80-min tutorials; 5-min lightning talks |
| CNCF-hosted co-located events EU 2027 (Agentics Day: MCP + Agents; Cloud Native AI + Inference Day; Open Source SecurityCon; Platform Engineering Day; CiliumCon; Observability Day; Open Sovereign AI + Cloud Day, etc.) | Mon 15 Mar 2027, Barcelona | 2 Sep – **Sun 18 Oct 2026, 23:59 CEST** | Open; notifications 14 Dec, schedule 16 Dec |
| Cloud Native Rejekts EU 2027 | 13–14 Mar 2027, Barcelona | **7 Dec 2026 – 3 Jan 2027** | Not yet open; designed for talks rejected from KubeCon |
| KubeCon Japan 2027 | Expected around July 2027 (dates TBD) | Not announced; 2026's closed 29 Mar | Likely Q1 2027 by pattern (inference) |
| KubeCon India 2027 | TBD | Not announced; 2026's closed 1 Feb | Likely around Jan 2027 by pattern (inference) |
| KubeCon NA 2027 | 8–11 Nov 2027, New Orleans | Not announced; 2026's ran 6 Apr – 31 May | Likely Apr–May 2027 (inference) |

**Tactical note:** the "excluding any project benefits" clause means Maintainer Track slots don't count against your limit. Co-presenting with an agent-sandbox maintainer (Janet Kuo, Justin Santa Barbara or barney-s) in a maintainer-track session is a way around the one-session cap — but it's their slot to offer, and it would be a project-update talk, not your red-team talk.

### 6. Talk concepts

All six are differentiated from (a) agentic guardrails with Whitney Lee — policy/admission/human approval — and (b) agentic context/data stores with Jeremy Morgan. Rule of thumb: in the new talk, admission policy gets one slide, and no RAG/vector content at all.

**Concept A — "Red Team the Sandbox: 2026's Real Agent Escapes vs. agent-sandbox, Naive and Hardened"** (Security track)
- *Pitch:* None of 2026's notable coding-agent escapes (Cymulate, Wiz GhostApproval, Pillar, Codex Heapjack, AgentCore DNS exfiltration) broke a hypervisor; they went around the sandbox. We replay each technique class against two agent-sandbox deployments — default template vs. hardened (gVisor or Kata, `hostUsers: false`, Cilium FQDN default-deny, egress-proxy credential injection, SPIRE identity, Falco rules) — and score which CNCF layer stopped, detected, or missed each one.
- *Why timely in March 2027:* v1.x will be about six months into production use; the escape catalog will be a year old and well documented; the hypervisor CVEs from 2026 give a "but what about escapes?" foil.
- *Demo:* a live scoreboard — attack classes vs. layers — with the naive cluster turning red and the hardened one green or amber. Pre-record a fallback.
- *Reviewer appeal:* vendor-neutral, demo-driven, lessons-learned, maps cleanly to the track's "threat modeling" and "incident post-mortems" language.
- *Risk:* you must reproduce attacks responsibly (public techniques only, patched versions) and keep it to 30 minutes.

**Concept B — "Your Warm Pool Is a Credential Cache: Identity and Secrets in Pre-Warmed and Snapshotted Agent Sandboxes"** (Security or Agentic AI)
- *Pitch:* Warm pools and pod checkpoint/restore (KEP-5823 alpha in 1.37, GKE Pod Snapshots) are how agent-sandbox gets sub-second latency — but a pod booted before a claim exists has no user identity, and a memory snapshot contains whatever secrets the agent held. Show the failure modes and the fixes: claim-time SPIFFE identity binding, keeping secrets out of the sandbox, snapshot-scrubbing and encryption.
- *Why timely:* upstream identity association is still Planned; checkpoint/restore is newly alpha. Very few people are on this.
- *Demo:* extract a token from a restored checkpoint in the naive setup; show the brain-outside design leaves nothing to extract.
- *Risk:* depends on runtime support (containerd/Kata) maturing. Highest novelty, moderate feasibility.

**Concept C — "Your Agent Sandbox Is Only as Secure as Its Egress"** (Connectivity or Security)
- *Pitch:* Assume the agent is already prompt-injected and the sandbox is intact — what leaves? DNS tunnels, allowlisted-host exfiltration, and credential replay. Compare Cilium FQDN policy, an Envoy/Istio ambient egress gateway, and (non-CNCF, flagged) agentgateway, with credential injection so the sandbox only ever holds a phantom token.
- *Overlap warning:* the NA 2026 nono-proxy session covers credential swapping; differentiate on DNS and allowlisted-host exfiltration, and on measured results.

**Concept D — "A Threat Model for agent-sandbox"** (Security)
- *Pitch:* A STRIDE-style threat model of the controller, router (scoped tokens), sandboxd, warm pools, SDKs and runtimes, done in the open and submitted to SIG Security / TAG Security as an artifact.
- *Strength:* community deliverable, reviewer-friendly. *Weakness:* less demo-driven; works best with a maintainer co-presenter.

**Concept E — "Defense in Depth, Measured: What Each CNCF Layer Buys an Agent Sandbox"** (Operations + Performance or Security)
- *Pitch:* Add layers one at a time — runtime, user namespaces, network, identity, egress proxy, detection — and measure attack coverage alongside cold-start, claim latency, and cost per sandbox-hour. Give an honest cost/benefit for each.
- *Strength:* data-driven. *Weakness:* heavy benchmarking work in 4–5 months; overlaps with Concept A.

**Concept F — "How CNCF-Native Can Agent Isolation Get? KubeVirt, urunc, and the RuntimeClass Gap"** (Emerging + Advanced)
- *Pitch:* An honest look at running agent-sandbox workloads on CNCF-hosted isolation (KubeVirt via the proposed pluggable provisioning, urunc), compared with gVisor and Kata.
- *Weakness:* may be immature by March; best as a co-located or Rejekts talk.

**Honest ranking for acceptance:**
1. **Concept A** — best fit with what committees accept (demo, lessons learned, vendor-neutral, security track), and clearly different from your other two talks. Its main risk is that it reads like "guardrails" — frame it as attack → layer → evidence, not policy.
2. **Concept B** — most novel and the least-covered topic, but more dependent on upstream timing. Good for Cloud Native AI + Inference Day or Open Source SecurityCon (CFP 18 Oct).
3. **Concept C** — strong but partly pre-empted at NA 2026.
4. D, E and F are weaker standalone submissions this cycle.

## Recommendations

1. **Decide today whether the third talk goes to the main CFP.** If your two existing talks are both going to EU 2027, you're at three proposals already if you add this one, and only one non-panel session can be accepted. Submit Concept A to the main CFP only if you'd rather give it than one of the other two; otherwise:
2. **Submit Concept B (or a lightning version of A) to a CNCF-hosted co-located event by 18 Oct 2026** — Open Source SecurityCon or Cloud Native AI + Inference Day fit best.
3. **Hold Concept A or C for Cloud Native Rejekts EU 2027 (CFP 7 Dec – 3 Jan)** as the fallback if it isn't accepted, then KubeCon Japan 2027 and NA 2027.
4. **In whichever abstract you write:** say where "pure CNCF" ends (gVisor/Kata), name the versions (agent-sandbox v1.0.x, Kubernetes 1.37), promise measured results rather than adjectives, and avoid anything that sounds AI-generated — the CFP explicitly warns about it.
5. **Strengthen with a co-presenter who is either an end user or an agent-sandbox maintainer.** End-user co-speakers raise acceptance odds; a maintainer adds credibility to a threat model.
6. **Fix your repo's language now:** your own issue #388 already notes agentgateway is AAIF/Linux Foundation, not CNCF; carry the same precision into the abstract — reviewers will notice.

## Caveats

- KubeVirt, Kyverno, ESO, cert-manager, Capsule and Confidential Containers maturity levels in the stack table have now been checked against cncf.io, CNCF announcements or project announcements; ToolHive's status is still unverified, so check cncf.io before using it.
- GKE adoption numbers (16x growth, millions of agents, 300 sandboxes/sec) are Google's own claims relayed through a third-party blog; the E2B-vs-self-hosted cost model is a "community" model of unknown method.
- bex.co, Northflank, ARMO, Cloudfleet and Pulumi are vendors with commercial interests; their technical descriptions match primary sources, but their framing is promotional.
- Maintainer names are inferred from Prow bot approvals, not the OWNERS file.
- The NA 2026 schedule was read only partly through LF event pages; several titles and speakers are missing, and some attributions (e.g., the Envoy AI Gateway + Kyverno talk, "Lima as the Universal AI Sandbox") are uncertain.
- Roadmap items are statements of intent, not commitments; "likely by March 2027" assessments are my inference.
- Reddit, Hacker News and Kubernetes Slack were not sampled; the pain-point evidence leans on vendor and project sources.
