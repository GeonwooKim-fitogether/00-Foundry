# Director Card Template

**Status**: Standard v1.0 · Authored 2026-05-16 · Source: WP-004 T-25 retrospective on `12.subscription-payment-saas-platform`

Director Card는 Director가 HCP(High Consequence Point) 또는 Director-only 행동을 직접 수행해야 할 때 Implementer가 발급하는 단일 실행 카드다. **카드 한 장으로 Director가 PASS/FAIL 결론까지 도달**해야 한다.

---

## 4약속 — Director가 **안 해야 하는** 것

| # | 약속 | 의미 |
|---|---|---|
| 1 | **읽기 부담 0** | 카드 한 장이면 끝. 위로 스크롤 안 함. 일반 안내/배경 설명/메커니즘 설명 카드에 안 적힘. |
| 2 | **판단 부담 0** | 명령은 통째로 복붙. "이거 vs 저거" 고르기 0. 셸/OS 변종 분기 0. |
| 3 | **디버깅 부담 0** | 막히면 결과만 chat에 paste. Implementer가 새 카드를 보냄. |
| 4 | **메커니즘 부담 0** | "왜 Director가 직접 해야 하나"만 한 줄. "어떻게 작동하는가"는 안 적힘. |

> **카드는 메뉴판이지 조리법이 아닙니다.**

Implementer 책임은 정반대로 비대칭으로 늘어남: 셸/OS/PATH, 분기 판단, 메커니즘 이해, 환경 변동성 — 전부 카드 발급 **전에** 흡수해야 함.

---

## 표준 형식

```
# 🟦 [T-NN] [What] (예상 소요)

WHY: [Director가 직접 해야 하는 이유 — 1줄. HCP/Director-only 조건 명시]
PREQ: [선행 조건 — 예: "T-X PASS"]

[STEP 1 명령 — 한 덩어리 복붙 단위, fenced code block]
→ [성공 신호 1줄]

[STEP 2 명령 — 필요 시. 가능한 한 4단계 이하]
→ [성공 신호 1줄]

---

✓ PASS 보고: [정확한 한 줄 PASS phrase — Director가 chat에 그대로 paste]
✗ FAIL 시:   [무엇을 paste할지만. 디버깅 안내 금지]
❌ 금지:      [1~3개 보안 경계만]
```

**필수 섹션**: WHY (1줄) · PREQ · 명령 블록(들) · PASS 보고 · FAIL 보고 · 금지.
**선택 섹션**: 추가 정리 명령 (cleanup 등) — Step 종료 후.

---

## 안티패턴 (카드에 넣지 말 것)

| 안티패턴 | 예시 | 왜 안 됨 |
|---|---|---|
| **"왜 이렇게 동작하는가" 설명** | "PostgREST는 stateless여서..." | 메커니즘 부담 (약속 ④) |
| **분기 안내** | "X 안 되면 Y를 시도하세요" | 판단 부담 (약속 ②). Implementer가 한 가지로 통합 |
| **셸/OS 변종 옵션** | "PowerShell 5.1이면 X, 7+면 Y" | 판단 부담 (약속 ②). Implementer가 PS 5.1 호환으로 통일 |
| **다중 PASS phrase 옵션** | "이렇게 또는 저렇게 보고" | 판단 부담 (약속 ②) |
| **디버깅 가이드** | "FAIL이면 X 확인 후 재시도" | 디버깅 부담 (약속 ③). FAIL = paste만 |
| **§1 §2 §3 §4 §5 다중 섹션** | "§1 사전 점검, §2 실행, §3 검증..." | 읽기 부담 (약속 ①) |
| **그림/비유 설명** | "왜 창 두 개? 그림으로 보면..." | 읽기 부담 (약속 ①). 카드를 따랐을 때 자동으로 작동하면 그림 불필요 |

---

## Implementer 사전 self-audit 체크리스트

카드 발급 전 Implementer가 self-verify:

- [ ] 카드 한 장 안에 모든 정보 포함 (이전 대화 참조 0)
- [ ] 명령 블록이 한 덩어리 복붙 단위 (Director가 중간 편집 0)
- [ ] 셸/OS 변동성 사전 흡수 (PowerShell 5.1, Bash, zsh 다 OK)
- [ ] 환경 변수 의존 사전 감지 (예: PATH에 `pnpm` 없으면 `npm`으로 통일)
- [ ] Director가 메커니즘 모르고도 PASS/FAIL 판단 가능
- [ ] FAIL 출력이 자동으로 진단 정보 포함 (서버 콘솔 etc.)
- [ ] PASS phrase가 정확히 한 줄
- [ ] 금지 항목 1~3개로 압축 (일반 보안 reminder 제거)
- [ ] Secret/credential의 chat 노출 가능성 0 (`$secret` 직접 echo 금지)

체크 미통과 항목이 있으면 카드 발급 보류 + 흡수 → 재발급.

---

## 참고 — 안 좋은 카드 vs 좋은 카드 (T-25 retro)

### 안 좋은 (T-25 v1, 폐기)
- §1 사전 점검 / §2 명령 / §3 결과 / §4 PASS / §5 마치는 법 — 5섹션
- 창 ① 창 ② 패턴 + "왜 창 두 개?" 그림 설명
- pnpm vs npm fallback 안내
- 다중 보안 reminder 4줄

### 좋은 (T-25 v4, 채택)
- WHY 1줄 + 단일 복붙 블록 + PASS/FAIL/금지
- 단일창 자동 백그라운드 dev server + 동적 포트 감지 (Director 판단 0)
- npm으로 통일 (PowerShell 5.1 + curl.exe 사전 흡수)
- 금지 1줄

길이 비교: v1 ≈ 60줄 · v4 ≈ 35줄. Director 체감 부담: v4가 1/3 이하.

---

## 카드 라이프사이클

1. **발급** — Implementer가 chat에 카드 1장 paste
2. **실행** — Director가 카드 복붙 → 결과 확인
3. **보고** — Director가 PASS phrase 한 줄 OR FAIL 출력 paste
4. **다음 카드** — Implementer가 자동으로 다음 단계 카드 발급 (또는 cycle 종료)

Director의 평균 turn은 **1줄** (PASS phrase 또는 FAIL paste). 1줄 넘으면 카드가 잘못 설계된 것.

---

## 적용 범위

- WP-XXX 단위 모든 HCP/Director-only 작업
- T-NN 단위 self-execute 카드
- Hotfix 카드 (Director 승인 필요 시)
- Final CP / D-XXX 결정 요청 카드

신규 프로젝트는 `00-Foundry`의 본 template을 직접 reference하거나, 프로젝트 `meta/director-card-template.md`에 instance 노트로 발췌.
