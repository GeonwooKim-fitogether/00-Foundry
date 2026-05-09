# Foundry Improvement Log — `<project-name>`

> 본 프로젝트 진행 *중* 발견한 Foundry 개선 아이디어를 **그 자리에서** 박제하는 raw 로그.
> 정제된 후보로 격상은 [foundry-backport-candidates.md](./foundry-backport-candidates.md) 에서.
> Meta Sprint (프로젝트 종료 시) 의 1차 입력.

## 작성 규칙
1. 발견 즉시 1행 추가. 미루지 말 것 — 미루면 잊는다.
2. 항목별 ID 는 `FIL-NNN` (Foundry Improvement Log).
3. 각 행은 *증거 지향* — "왜 그렇게 느꼈는가" 의 맥락이 사라지면 Meta Sprint 가 진단 불가.
4. **즉시 Foundry 원본을 수정하지 않는다.** 본 로그에만 박제.

## 항목 형식

```markdown
### FIL-001 — <짧은 제목>
- **발견일**: YYYY-MM-DD
- **발견자**: <역할 또는 이름>
- **발견 맥락**: 어떤 작업 중 / 어떤 cycle 의 어느 단계에서.
- **증상 / 관찰**: 무엇이 어색했는가, 무엇이 부족했는가, 어떤 룰이 현실과 어긋났는가.
- **가설**: 본 항목이 Foundry 의 어떤 룰/템플릿/도구에서 유래한 것 같은가. (추정 OK)
- **제안 (1차 시안)**: 어떤 변경이면 해소되는가. (확정 아님 — Meta Sprint 에서 다시 본다)
- **영향 추정**: 본 변경이 다른 프로젝트에도 가치가 있을 가능성 (높음/중간/낮음 + 이유).
- **임시 대응**: 본 프로젝트에서 즉시 해야 할 우회가 있다면 1줄. *Foundry 원본 수정 금지*.
- **참조**: 관련 cycle / Brief / 파일 경로.
```

## 예시 (참고용 — 실 사용 시 삭제)

### FIL-001 — file_exists path 가 sibling 프로젝트 검증에서 어색
- **발견일**: 2026-05-08
- **발견자**: project-owner
- **발견 맥락**: 12.subscription-payment-saas-platform 의 NPI_Brief 를 verification-runner 로 검증할 때.
- **증상 / 관찰**: project_root 가 `00-Foundry/` 로 잡혀 path 를 `../12.subscription-payment-saas-platform/...` 로 써야 한다. cross-project 일 때 직관적이지 않음.
- **가설**: runner 의 `find_project_root` 가 `factory.yaml` 만 marker 로 본다. workspace 루트의 sentinel 이 없음.
- **제안 (1차 시안)**: workspace 루트에 `.foundry-root` sentinel 또는 minimal `factory.yaml` 포인터를 두는 옵션. v0.3.0 후보.
- **영향 추정**: 높음. 다중 프로젝트 워크스페이스를 쓰는 모든 사용자에게 영향.
- **임시 대응**: 본 프로젝트의 AC YAML path 에 `..` 접두사를 사용. Foundry 원본은 손대지 않음.
- **참조**: `12.subscription-payment-saas-platform/ai-npi/NPI_Brief.md` AC-1.

---

## 항목 누적 (이 아래에 새 항목 추가)
