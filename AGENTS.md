# talk-agent-runtime-goat

Working repo for the talk "Clearing the Runtime Confusion: Which Agent Runtime Is the
GOAT?" by Michael Forrester, submitted to KubeCon + CloudNativeCon EU 2027, Barcelona.
`README.md` states what the talk argues and its status.

Test command: `python3 -B -m unittest discover -s tests`

No E2E command yet: the repo has no end-to-end or integration tests, only the file checks
above. The demo harness, which will run the attacks against a real cluster, is the first
thing that will need one; declare its heavy-gate command here when it lands.

## Rules

- Work on `staging`; `main` only moves by promotion from `staging` after tests pass.
- `decisions.md` is append-only. Correct an earlier entry with a new one, never by
  editing it.
- Read `PROJECT_STATE.md` first and update it when the phase or next steps change.
- No claim reaches the abstract or a slide until it is checked against its primary
  source. `research/2026-10-11-verification.md` is the record.
- The title must match across `README.md` and both files in `abstract/`; the tests
  check this and the Sessionize description limit.

## Where things live

- `talks/talks-knowledge` (`peopleforrester/talks-knowledge`): source of truth for the
  talks. It holds the register (`talks/register.md`), the research index, and the
  abstracts and talk scripts. Where the abstract here and the one there disagree,
  talks-knowledge wins.
- `conferences/conference-knowledge`: event state, meaning dates, CFPs, and
  acceptances. The key dates in `README.md` are a snapshot from the 2026-10-10 research.
- This repo: the talk's own research, abstract drafts, and, once built, the demo
  harness and deck.
