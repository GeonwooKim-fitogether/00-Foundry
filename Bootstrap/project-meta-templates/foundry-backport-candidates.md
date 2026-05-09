# Foundry Backport Candidates — `<project-name>`

> Meta Sprint 진입 시 [foundry-improvement-log.md](./foundry-improvement-log.md) 의 raw 항목을
> 4개 분류 (승인 / 보류 / 폐기 / 추가검토) 로 정제한 *결정-가능한* 후보 모음.
> 사용자 최종 승인은 본 문서의 `## 승인` 섹션 위에서 일어난다.

## 분류 정의

| 분류 | 의미 | Meta Sprint 액션 |
|---|---|---|
| **승인** (approve) | Foundry 에 반영해야 함이 명백. 다른 프로젝트도 영향. | 사용자 최종 승인 후 `00-Foundry` 에 commit. |
| **보류** (hold) | 가치 있으나 1개 사례만으로 결정 부족. | 재검토 트리거 조건 명시 후 다음 Meta Sprint 로 이월. |
| **폐기** (reject) | Foundry 룰 의도에 어긋남 / 본 프로젝트 특수 / 잘못된 진단. | 폐기 사유 1줄 + 원본 변경 0. |
| **추가검토** (review) | Critical Decision 성격. ChatGPT 또는 외부 의견 필요. | `ask-chatgpt-decision` 패키지 작성 → 회신 후 재분류. |

## 항목 형식

```markdown
### FBC-001 — <짧은 제목>
- **유래**: foundry-improvement-log.md#FIL-NNN (몇 개여도 OK — 같은 본질을 가리키면 묶음)
- **분류**: 승인 | 보류 | 폐기 | 추가검토
- **변경 대상 (Foundry)**: 어떤 파일 / 어느 섹션을 어떻게 바꿀지 (구체적으로).
- **호환성 영향**: 기존 Brief / runner schema / 다른 프로젝트가 깨지는가? Semver bump 후보 (major/minor/patch) 추정.
- **승인 사유 / 보류 사유 / 폐기 사유 / 추가검토 이유**: 한 단락.
- **사용자 응답** (Meta Sprint §4): `[APPROVED]` / `[DEFER]` / `[REJECT]` / `[SPLIT]` 중 하나 + 1줄 코멘트.
- **반영 결과** (사용자 승인 후): commit SHA + Foundry version (예: `abc1234 → v0.3.0`).
```

---

## 승인 (Approve)

> 사용자 최종 승인 게이트. 본 섹션의 항목만 `00-Foundry` 에 반영된다.

(아직 항목 없음.)

---

## 보류 (Hold)

> 1개 사례만으로 결정 부족. 재검토 트리거 명시 필수.

(아직 항목 없음.)

---

## 폐기 (Reject)

> Foundry 룰 의도에 어긋나거나, 본 프로젝트 특수 사정이거나, 진단 오류로 판명된 항목.

(아직 항목 없음.)

---

## 추가검토 (Review)

> Critical Decision 성격. ChatGPT / 외부 의견을 거쳐 *승인 / 보류 / 폐기* 중 하나로 재분류.

(아직 항목 없음.)

---

## Meta Sprint 운영 메타

- **Meta Sprint 시작일**: <YYYY-MM-DD>
- **사용자 최종 승인일**: <YYYY-MM-DD>
- **Foundry 반영 commit 범위**: `<sha-from>..<sha-to>`
- **Foundry version bump**: `<from> → <to>` (Semver 근거: …)
- **self-test (B-002 패턴) 재통과**: ✅ exit 0 / ❌ 실패 (사유)
