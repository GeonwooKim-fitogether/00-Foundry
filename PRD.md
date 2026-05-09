# 📋 PRD — Foundry

**작성일**: 2026-05-02
**버전**: 0.1 (minimal — Kaizen 방향으로 진화)

---

## 1. 비전 한 줄

> 사용자가 *판단만* 하고 AI가 *조작* 하는 멀티 프로젝트 소프트웨어 공장의 운영체제.

## 2. 사용자 (단일)

- 페르소나: 공장주 (CEO) + 하드웨어 출신 + AI 작업자 운용
- 시간 자원 = 가장 희소한 자원, 보호 최우선
- *흐름·진척도·막힌 곳* 의 high-level visibility 만 필요

## 3. 핵심 기능 (현재)

| # | 기능 | 상태 |
|---|------|------|
| F1 | Backlog 누적·관리 | ✅ Backlog.md 운영 중 |
| F2 | Reading List 큐레이션 | ✅ Reading_List.md 존재 |
| F3 | 진행 중 즉시 반영 정책 (Compound Engineering) | ✅ 메모리 박제 (B21) |
| F4 | M01 Sprint 트리거 조건 | ✅ 메모리 박제 (B22) |
| F5 | 멀티 프로젝트 STATUS 대시보드 | ⏳ Backlog (B23 — 즉시 작업 후보) |
| F6 | Orchestration agent (사용자 대신 결정) | ⏳ Backlog (B24 — 사용자 제안) |

## 4. Non-Goals (의도적 제외)

- 학문적 framework 연구
- 산업공학·신경망 이론 깊이
- Toyota Production System 풀 구현
- 외부 사용자 / 팀 운영 지원 (단일 사용자만)

## 5. 진화 방향 (Kaizen)

이 PRD 는 *minimal*. 다음 항목들이 운영 데이터·실사용 경험 누적되면 채워질 예정:
- 멀티 프로젝트 통계 (cycle time, hotfix rate 등 — 데이터가 *모인 후* 추가)
- 하드웨어 라인 통합 (AI 도구 성숙 후)
- 외부 알림 채널 정책 (Channels 채택 후)

## 6. 구조 결정 기록 (ADR — 짧게)

- **2026-05-02**: 본 프로젝트를 `11-shopping-dashboard` 의 `Artifacts/01_Meta/` 에서 분리 → 별도 sibling 프로젝트로 운영. *진행 중 제품 / 메타 framework 의 관심사 분리 명확화*.
