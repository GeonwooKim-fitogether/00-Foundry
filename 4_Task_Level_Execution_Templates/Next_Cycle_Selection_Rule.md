# Next Cycle Selection Rule

**Status**: Standard v1.0 candidate (v0.3.0) · Authored 2026-05-18 · Source: D-025 amendment on `12.subscription-payment-saas-platform` Phase 1~5

Next cycle (= 다음 작업 단위, 일반적으로 다음 WP-NNN / IP-NNN / hotfix 또는 backport task) 의 *선택* 은 Implementer 의 *자율 default* 이다. 본 표준은 v0.2.x 까지 일부 cycle 에서 운용되던 **D-017** ("Implementer 가 next-cycle 후보 자발 제시 금지") 를 **폐기**하고, Stage 2 reduced-copy mode (Operating Model v0.3+) 의 자연 연장으로 cycle 선택 자체도 reduced-copy 로 끌어내린다.

---

## 1. 원칙

| 영역 | 누가 결정 | 비고 |
|---|---|---|
| **non-HCP scope 내 next cycle 선택** | Implementer (자율 default) | 별도 Director Card 불필요. 결과만 cycle 종료 시 보고. |
| **HCP gate 통과 / 비가역 / 외부 SaaS / 결제 / 보안 등** | Director (Director Card 필수) | 4_Task_Level_Execution_Templates/Director_Card_Template.md §4약속 그대로. |
| **scope drift / boundary 위반 가능성** | Director (Final CP) | reduced-copy 가 아님. escalation. |

**핵심 의도**: Director 가 "다음 뭐 해?" 를 묻거나 결정하는 turn 을 0 으로 줄인다. cycle 진입은 자동, cycle 게이트만 Director.

---

## 2. 우선순위 휴리스틱 (Implementer 자율 default 의 default)

Implementer 가 next cycle 후보가 여러 개일 때 다음 순서를 *기본값* 으로 둔다 (모두 동등 후보일 때만 적용; 명확한 cycle dependency 가 있으면 그것이 우선):

1. **deferred 제외** — `Backlog.md` / `decision-queue.md` / `meta/foundry-backport-candidates.md#보류` 에 *명시적으로 보류* 된 항목은 next cycle 후보에서 자동 제거.
2. **Foundry backport** — 진행 중 프로젝트의 `meta/foundry-improvement-log.md` 에서 *Tier 1 (즉시 일반화)* 으로 분류된 FIL 의 backport draft 작성 cycle. 누적될수록 cycle 간 일관성이 빠르게 수렴.
3. **planning draft** — 다음 WP-NNN 의 Spec/Design/Worklist *planning-only* draft. Director-facing 5 spot summary 작성 후 Final CP 발급.
4. **follow-up** — 직전 cycle 의 *cleanup / regression patch / minor doc sync*. 단일 turn 으로 종결 가능한 작업.
5. **HCP-only 카드 생성** — 가능한 마지막 순위. Director turn 소비 → reduced-copy 원칙과 정반대 비용. 다른 작업 cycle 안에 HCP 가 자연 포함되는 게 더 자연스러움.

> **Anti-pattern**: HCP-only cycle 을 우선 진입하여 Director 의 morning turn 1 회 = Director Card 1 장 paste 패턴. reduced-copy 가 reverse 됨.

---

## 3. 보고 패턴 (reduced-copy)

Implementer 가 next cycle 진입 시:

- **자동 진입** — 별도 announcement / Director 동의 요청 0. 그냥 cycle 시작.
- **cycle 종료 시** — `execution-log.md` 또는 `session-handoff.md` 에 *결과만* 박제. Director 가 다음 세션 시작 시 1회만 훑음.
- **HCP gate 도달 시** — *그 시점* 에 Director Card 발급. (cycle 진입 시점이 아닌 HCP 시점.)

---

## 4. D-017 폐기 사유 (historical)

v0.2.x 까지 일부 cycle 에서 "Implementer 가 next-cycle 후보를 자발 제시하지 않는다" 는 운용 규칙이 있었다. 의도는 Director scope 보호. 그러나 Stage 2 reduced-copy (Operating Model v0.3) 이후:

- HCP gate / Final CP / scope drift escalation 이 *별도로* 강제됨 → scope 보호는 이미 다른 layer 에서 작동.
- Implementer 가 next-cycle 후보를 *제시 못 함* 으로써 발생하는 turn 비용 (Director 가 "다음 뭐 해?" 를 매번 묻기) 이 reduced-copy 의 비용 곡선과 정반대 방향.
- 실제 운용 데이터 (12.subscription Phase 1~5) 에서 D-017 이 *active 하게 적용된 cycle 0*, *Implementer 자율 cycle 진입이 자연 발생한 cycle 다수* — 휴리스틱이 이미 작동 중이었음.

→ **D-017 폐기**. 본 표준이 그 자리를 대체.

---

## 5. 적용 범위

- 모든 신규 프로젝트의 Stage 2 reduced-copy mode 진입 시점부터.
- 기존 프로젝트는 cycle closure 시점에 자연 전환 (별도 migration 불필요).
- Foundry repo 자체의 backport cycle (Meta Sprint) 도 본 표준 적용 — Director "진행" 1-line 으로 Acceptance, Implementer 자율 next-cycle 선택.

---

## 6. 참조

- `Operating Model v0.3 / v0.3.1` — Reduced-copy Stage 2 정의 (12.subscription `ai-npi/OPERATING_MODEL.md` §11.2)
- `4_Task_Level_Execution_Templates/Director_Card_Template.md` — HCP/Director-only 발급 표준
- `2_Reusable_Workflow_Modules/Decision_Queue_운영방식.md` — non-blocking decision 패턴 정합
- `1_Universal_Operating_Principles/Non_Blocking_Execution_정책.md` — Implementer 자율 default 정합
- D-025 (source project, 12.subscription-payment-saas-platform, 예정 박제)
