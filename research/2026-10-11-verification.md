# Verification of the 2026-10-10 Research, 2026-10-11

Every claim the abstract depends on was rechecked against primary sources on
2026-10-11 (advisories, GHSA and CVE records, researchers' own posts, project release
notes, the CNCF landscape, the LF CFP page and the LF schedule data). Where a source
could only be found secondhand, the table says so.

Verdicts: **Confirmed**, **Corrected** (the 2026-10-10 research was wrong in a way that
matters; the corrected fact is given), **Not found** (searched, not located; not the same
as false).

## Coding-agent escapes (the attack catalog the talk replays)

| Claim | Verdict | Corrected or confirmed fact | Primary source (date) |
|---|---|---|---|
| Cymulate configuration-based sandbox escape (CBSE) | Confirmed | Sandboxed agent writes `.claude/settings.json` hooks or `.codex/config.toml`; the host runs them on next launch. Claude Code reported 2026-01-05, fixed v2.1.2, CVE-2026-25725 (2026-02-06). Gemini CLI unfixed, public 2026-04-07. Codex closed as Informational. | cymulate.com/blog/the-race-to-ship-ai-tools-left-security-behind/ ; GHSA-ff64-7w26-62rf (2026-02-06) |
| Claude Code CVE-2026-25723 | Confirmed | Piped `sed` and `echo` bypassed file-write restrictions. Needs accept-edits mode. Fixed v2.0.55. | GHSA-mhg7-666j-cqg4 (2026-02-06) |
| Wiz GhostApproval | Confirmed | Symlink following lands an approved write outside the workspace. Amazon Q, Claude Code, Augment, Cursor, Antigravity, Windsurf. CVE-2026-12958 (AWS), CVE-2026-50549 (Cursor). | wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants (2026-07-08) |
| Pillar Security "week of sandbox escapes" | Confirmed with nuance | Seven findings. Cursor CVE-2026-48124 (workspace hook config, fixed 3.0.0). Codex "GitPwned" via allowlisted `git show`, fixed v0.95.0. Gemini CLI appears only in the shared Docker-socket finding, which Google treats as documented behavior. | pillar.security/blog/the-week-of-sandbox-escapes (2026-07-20) |
| Accomplish Heapjack and Overpatch | Corrected | Reported 2026-08-12, **published 2026-09-15**. Heapjack is Codex Desktop (read-only escape). Overpatch is Codex CLI (`apply_patch` widened the write grant, fixed 0.149.0). | accomplish.ai/blog/escaping-the-openai-codex-sandbox-twice/ (2026-09-15) |
| AgentCore Code Interpreter DNS exfiltration | Corrected | Two disclosures: Unit 42 (2026-04-07) and BeyondTrust (2026-03-16). **AWS remediated Sandbox-mode DNS tunneling on 2026-04-15** (BeyondTrust update, read from search snippets because the page returned 403). Describe it in the past tense. | unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/ (2026-04-07) |
| "GitSpawn" | Corrected | Disclosed by **Manifold Security** (2026-09-01 or 02), not Adversa. Adversa's 2026-10-02 roundup aggregated it. Manifold's own post not found. Kept out of the abstract. | adversa.ai/blog/top-ai-coding-agent-security-resources-october-2026/ (secondary) |
| 79% classifier bypass | Corrected | arXiv 2609.19587 (2026-09-17): injection attacks against Claude Code Auto Mode and Codex Guardian succeeded in 79% of trials, not split by product. Not used in the abstract. | arxiv.org/abs/2609.19587 |
| Armadin, Claude Cowork | Corrected | Windows Cowork, a Hyper-V VM, not bubblewrap. Reported 2026-03-20, published 2026-07-01. Secondary sources only. Not used. | SiliconANGLE (2026-07-01) |
| NVIDIA AI Red Team guidance | Confirmed | "Block writes to configuration files, no matter where they are located", covering hooks, skills and local MCP configurations. | developer.nvidia.com/blog/practical-security-guidance-for-sandboxing-agentic-workflows-and-managing-execution-risk (2026-01-30) |
| OWASP Top 10 for Agentic Applications | Confirmed | Published 2025-12-09. ASI05 "Unexpected Code Execution" (name confirmed via BleepingComputer, not the OWASP page). | genai.owasp.org (2025-12-09) |

## Substrate CVEs (the "but what about real escapes" foil)

| Claim | Verdict | Fact | Primary source (date) |
|---|---|---|---|
| Firecracker CVE-2026-5747 | Confirmed | virtio-pci OOB write, opt-in `--enable-pci` only, needs guest root. Fixed 1.14.4, 1.15.1. Credited to Anthropic. | AWS bulletin 2026-015-AWS (2026-04-07) |
| Firecracker CVE-2026-1386 | Confirmed, reframed | Jailer symlink; attacker is a **local host user**, not a guest. Not a guest escape. | AWS bulletin 2026-003-AWS (2026-01-23) |
| Cloud Hypervisor CVE-2026-45782 | Confirmed | virtio-block async I/O UAF, defaults affected, fixed v51.2/v52.0. | GHSA-f47p-p25q-83rh (2026-05-14) |
| Kata CVE-2026-47243 | Confirmed | CVSS 4.0 9.2, runtime-rs standalone virtio-fs only; virtiofsd as root with sandbox and seccomp off. Fixed 3.31.0. | GHSA-2gv2-cffp-j227 (2026-05-21) |
| Kata CVE-2026-44210 | Corrected | Annotation argument injection (`virtio_fs_extra_args`), default-enabled. **CVSS 4.0 5.8, Medium**, not critical. Fixed 3.31.0. | GHSA-rr59-xxvx-96qr (2026-05-20) |
| KVM Januscape CVE-2026-53359 | Confirmed | Shadow-MMU UAF, Intel and AMD, kvmCTF 0-day by Hyunwoo Kim. Public PoC only panics the host. | seclists.org/oss-sec/2026/q3/64 (2026-07-06) |
| gVisor CVE-2026-96812 | Confirmed | Host root via CUSE; needs CUSE on the host and image-deployment privilege. | google/gvisor commit 573a9e73cf844f (2026-09-25) |
| gVisor CVE-2026-95702 | Confirmed, reframed | Code execution inside the Sentry, still confined by host seccomp and namespaces. Not a full escape. | CVE record (2026-10-09) |
| runc CVE-2025-31133, 52565, 52881 | Confirmed | Published 2025-11-05; fixed 1.2.8, 1.3.3, 1.4.0-rc.3. | opencontainers/runc GHSAs (2025-11-05) |
| Andronchik and Lokhmakov sandbox study | Corrected | arXiv:2606.08433, **submitted 2026-06-07**, not 2026-05-24. No overall ranking. | arxiv.org/abs/2606.08433 |

## agent-sandbox and Kubernetes

| Claim | Verdict | Fact | Primary source (date) |
|---|---|---|---|
| agent-sandbox v1.0.0 | Confirmed | 2026-08-28. | `gh release list -R kubernetes-sigs/agent-sandbox` |
| Latest release | Corrected | **v1.0.6, 2026-10-08.** Roughly weekly patches. | same |
| v1.0.2 breaking changes | Confirmed | Router `Authorizer` takes `AuthorizationTarget` (#1497); router manifests moved to `agent-sandbox-system` (#1537). | release notes v1.0.2 (2026-09-11) |
| CRDs and API version | Confirmed | `Sandbox` in `agents.x-k8s.io/v1beta1`; `SandboxTemplate`, `SandboxClaim`, `SandboxWarmPool` in `extensions.agents.x-k8s.io/v1beta1`. | `k8s/crds/*.yaml` |
| Stars | Corrected | 4,216 on 2026-10-11. | GitHub API |
| Roadmap items still Planned | Confirmed | Sandbox/Pod Identity Association at claim time; Network Policy attach at claim time; **Auto** Suspend/Resume (plain PVC suspend/resume is already Completed). | roadmap.md (last commit 2026-08-28) |
| Red Hat: agent-sandbox "does not by itself provide a hardened security boundary" | Confirmed | Verbatim. Authors Esposito and Freimann. | developers.redhat.com/articles/2026/07/15/red-hat-build-agent-sandbox-isolated-workload-management-kubernetes (2026-07-15) |
| Red Hat build is Technology Preview | Not found | The article names no support level. Call it a downstream build. | same |
| GKE Agent Sandbox GA | Confirmed | 2026-05-20, gVisor, GKE 1.35.2-gke.1269000+. | Google Cloud blog (2026-05-20) |
| User namespaces GA in v1.36 | Confirmed | KEP-127 stable in v1.36 (released 2026-04-22). | kubernetes/enhancements |
| Pod-level checkpoint/restore alpha in v1.37 | Corrected | **KEP-5823 missed v1.37.** Only the CRI `CheckpointPod`/`RestorePod` RPCs landed. Now targets alpha in v1.38 (planned 2026-12-16). | kubernetes/enhancements #5823 |

## CNCF status

| Project | Status | Date | Source |
|---|---|---|---|
| Kyverno | Graduated | announced 2026-03-24 | cncf.io announcement |
| Falco | Graduated | 2024-02-29 | cncf/landscape |
| Cilium | Graduated | 2023-10-11 | cncf/landscape |
| SPIFFE / SPIRE | Graduated | 2022-08-23 / 2022-08-22 | cncf/landscape |
| Confidential Containers | Incubating | 2026-07-08 | cncf/landscape; CNCF blog 2026-07-22 |
| KubeVirt | Incubating | 2022-04-19 | cncf/landscape |
| urunc | Sandbox | 2025-05-22 | cncf/landscape |
| gVisor, Kata Containers | Not CNCF | n/a | Google OSS; OpenInfra Foundation |

## CFP (KubeCon + CloudNativeCon Europe 2027)

| Item | Fact | Source |
|---|---|---|
| Event | Barcelona, 2027-03-15 to 18 | LF CFP page, read 2026-10-11 |
| Main CFP closes | Sunday 2026-10-11, 23:59 CEST | same, and Sessionize |
| Notifications / schedule | 2026-12-07 / 2026-12-09 | same |
| Tracks | 13, including "Security" and "Agentic AI" by those names | same |
| Session format | 30 minutes, 1 to 2 speakers; lightning talk 5 minutes, 1 speaker | same |
| Required fields | Title (title case), description (public if accepted, written in full third-person sentences per the page), benefits to the ecosystem, case study yes/no, presented before, projects covered, a prior recording | same |
| Character limits | Not found on any public page. Check inside the Sessionize form before pasting. | n/a |
| Co-located CFP (incl. Open Source SecurityCon, Agentics Day) | Closes 2026-10-18 | LF co-located CFP page |

## Competing talks, rechecked

Source: the schedule data embedded in the LF event pages for KubeCon NA 2026 (main
program and CNCF-hosted co-located events), read 2026-10-11. Of 57 sessions matching
sandbox, escape, red team, gVisor, Kata or agent-sandbox, **none replays the 2026
escape classes against agent-sandbox and scores each layer.**

| Talk | Speakers | When | What it does |
|---|---|---|---|
| Detonation and Isolation: Hardening Kubernetes Runtimes for Agents | Syeda Anjum, Kaslin Fields, Kavitha Rajendran | Agentics Day, 2026-11-09 16:30 | Defensive walkthrough of runtime isolation and syscall filtering. No escape replay. |
| Platform-First AI Agent Security: Zero-Trust Patterns for Kubernetes | Carlos Santana | 2026-11-12 15:30, Security | Architecture on agent-sandbox, gVisor/Kata, KRO, GitOps, credential proxies, warm pools. States syscall interception "prevents escape even with root access". |
| Untrusted Code on Secure Runtimes: Agent Sandboxes on Kubernetes | Rahman, Brown, Kaslin Fields, Bourgeois, West | Tutorial, 2026-11-12 13:50 | Hands-on agent-sandbox deployment. |
| Running Secure Agents at Scale | Carlos Sanchez (Adobe) | 2026-11-11 17:00 | End-user story on agent-sandbox in production. |
| After Admission: Kernel Enforcement for Agents Kyverno Let In | Sal Kimmich | 2026-11-10 15:15, Cloud Native Theater | One credential-theft scenario: kernel denial, nono-proxy phantom token, audit ledger. |
| License to Generate | Maia Iyer, Hai Huang | Open Source SecurityCon, 2026-11-09 14:40 | One attack blocked at several identity layers (Keycloak, SPIRE, Envoy). |
| Securing the Agentic Tool Layer | Saurabh Yergattikar, Harshul Jain | Agentics Day, 2026-11-09 10:40 | Red team at the MCP tool layer (74% to under 9%). Not runtime escapes. |
| Beyond Harnesses and Sandboxes: Runtime Protection for AI Agents with eBPF | Zheng, Cheng | 2026-11-11 13:20 | Detection layer. |

No accepted EU 2027 talks exist yet; notifications go out 2026-12-07.
