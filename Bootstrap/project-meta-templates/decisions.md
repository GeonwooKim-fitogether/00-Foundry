# Decisions — `<project-name>`

> 본 프로젝트의 Critical Decision 시간순 로그.
> Foundry 와의 관계가 있는 결정 (예: factory_source version 선택, local_modifications 전환,
> Meta Sprint 의 사용자 최종 승인) 도 본 문서에 박제한다.
> Foundry-internal 결정은 `00-Foundry/CHANGELOG.md` 또는 `B-002_NPI_Worklist.md` 에.

## 항목 형식

```markdown
### D-NNN — <한 줄 결정 제목>
- **일자**: YYYY-MM-DD
- **종류**: scope | tech-stack | foundry-version | foundry-local-mod | meta-sprint-approval | …
- **결정 내용**: 무엇을 결정했는가 (한 단락).
- **근거**: 왜 그 결정을 내렸는가 (대안 비교 / 트레이드오프).
- **반대 의견 (있다면)**: steelman 으로 한 줄.
- **되돌리기 비용**: 낮음 / 중간 / 높음 + 이유.
- **승인자**: project-owner / sponsor / …
- **참조**: ask-chatgpt-decision 패키지 / Brief / cycle 번호.
```

## 누적 결정 목록

(예시 1행 — 실 사용 시 삭제)

### D-001 — Foundry 시작 version 으로 v0.2.0 채택
- **일자**: 2026-05-08
- **종류**: foundry-version
- **결정 내용**: 본 프로젝트는 `00-Foundry` repo 의 `v0.2.0` (commit `<sha>`) 에서 시작한다.
- **근거**: 최신 frozen version. validate-output runner 가 동작 확인된 첫 version.
- **반대 의견**: 없음.
- **되돌리기 비용**: 낮음 — factory.yaml 의 factory_source.version 만 바꾸면 됨. 단 실제 진행 산출물이 새 version 의 schema 에 맞게 갱신 필요.
- **승인자**: project-owner.
- **참조**: factory.yaml / NPI_Brief.md AC-5.

---

(이 아래에 새 결정 추가)
