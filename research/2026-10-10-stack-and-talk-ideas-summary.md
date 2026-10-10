# Stack and Talk Ideas Summary

Condensed from the three 2026-10-10 research files in this directory.

## Best CNCF stack with agent-sandbox at the core

| Layer | Pick | CNCF status |
|---|---|---|
| Orchestration | agent-sandbox v1.0.x (Sandbox, SandboxTemplate, SandboxClaim, SandboxWarmPool) | Kubernetes SIG Apps |
| Container runtime | containerd + RuntimeClass | Graduated |
| Isolation boundary | gVisor or Kata (best options, not CNCF); KubeVirt / urunc / Confidential Containers are the CNCF-hosted alternatives | KubeVirt incubating, urunc sandbox, CoCo incubating |
| Workload identity | SPIFFE/SPIRE | Graduated |
| Credentials | Never in the sandbox; injected at the egress proxy. cert-manager for short-lived certs, External Secrets Operator for sync | cert-manager graduated, ESO sandbox |
| Egress | Cilium FQDN default-deny + Envoy or Istio ambient egress gateway | Graduated |
| Admission | Kyverno (enforce RuntimeClass, hostUsers: false, no hostPath/Docker socket, strip Kata annotations) | Graduated |
| Runtime detection | Falco | Graduated |
| Supply chain | in-toto + Notary on sandbox images | Graduated / incubating |
| Audit | OpenTelemetry GenAI spans → Jaeger, correlated with Falco events | Incubating / graduated |
| MCP isolation | Each MCP server in its own Sandbox, fronted by Kuadrant | Sandbox |
| Agent framework | kagent (agent loop outside the sandbox) | Sandbox |
| Multi-tenancy | Namespace per tenant + Capsule | Sandbox |

## Talk ideas built on what people are struggling with now

1. **Red Team the Sandbox.** None of the 2026 coding-agent escapes broke a hypervisor. They went around the sandbox through config files, symlinks, Docker sockets, allowlisted commands and DNS. The talk would replay each technique against a default agent-sandbox setup and a hardened one, with a live scoreboard showing which CNCF layer stopped, caught or missed each attack.

2. **Your Warm Pool Is a Credential Cache.** Warm pools and pod checkpoint/restore are how agent-sandbox gets sub-second starts. But a pre-warmed pod has no user identity until it's claimed, and a memory snapshot holds whatever secrets the agent had. The demo would pull a token from a restored checkpoint, then show the agent-loop-outside design leaving nothing to extract. Identity binding at claim time is still only planned upstream, and pod checkpoint/restore only just went alpha in Kubernetes 1.37.

3. **Egress Is the Real Boundary.** Assume the agent is already prompt-injected and the sandbox holds. The question is what still gets out: DNS tunnels, data sent to allowlisted hosts, credential replay. The talk would compare Cilium FQDN policy with an Envoy/Istio egress gateway, with the sandbox holding only a fake placeholder token that the proxy swaps for the real one.

4. **Blind Inside the Box.** This covers what Falco and Tetragon can and can't see inside gVisor and Kata guests, and how to close the gap. It's a known problem with little documentation.

5. **What Did the Agent Actually Do?** This builds one audit trail per sandbox session by joining OpenTelemetry GenAI spans with kernel events from Falco and egress logs from Cilium.

Ideas 1 and 2 address the most current pain points. Idea 1 makes the best live demo.
