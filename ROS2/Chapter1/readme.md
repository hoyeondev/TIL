# Chapter 1: ROS 2 기본 개념과 설치 (ROS 2 Humble, Ubuntu 22.04 기준)

## ✅ 사용 환경

| 항목 | 정보 |
|------|------|
| OS   | Ubuntu 22.04 |
| ROS2 | ROS 2 Humble Hawksbill |

---

## 📌 1. ROS 2란?

ROS 2는 로봇 소프트웨어 개발을 위한 **모듈형 미들웨어 프레임워크**입니다.

- ROS 1의 한계를 보완 (멀티 로봇, 실시간성, 보안 등)
- DDS(Data Distribution Service) 기반 통신
- 주로 C++, Python 사용

### ROS 1 vs ROS 2

| 항목                     | ROS 1                                | ROS 2                                |
|--------------------------|---------------------------------------|---------------------------------------|
| 출시 시기               | 2010년 (ROS Noetic: 2020)            | 2017년 (ROS 2 Humble: 2022)          |
| 지원 종료               | Noetic은 2025년까지 LTS              | 활발한 개발 중 (Humble, Iron 등)     |
| 통신 방식               | TCPROS (ROS 자체 프로토콜)          | DDS 기반 (표준 미들웨어 사용)        |
| 실시간성 지원           | 불안정하거나 제한적 지원              | RTOS와의 호환으로 실시간성 가능       |
| 멀티 로봇 시스템        | 직접 구현 필요                       | 기본적으로 멀티 로봇 지원            |
| 보안(Security)          | 내장 보안 없음                       | DDS 기반 보안 기능 제공 (암호화 등)  |
| 운영 체제               | 리눅스 중심 (Ubuntu)                 | 리눅스, Windows, macOS 지원           |
| 언어 지원               | C++, Python (주로 Python 2)          | C++, Python 3                         |
| 패키지 관리             | `rosbuild` → `catkin`                | `ament` 빌드 시스템                   |
| Launch 시스템           | XML 기반 `launch`                    | Python 기반 `launch.py`              |
| 공식 시뮬레이터         | Gazebo (통합 아님)                   | Gazebo / Ignition과 긴밀한 통합       |
| 생명주기 관리           | 미지원                              | 노드 생명주기 관리 지원 (`lifecycle`) |
| 노드 이름 공간(namespace) | 제한적 사용 가능                     | 체계적이고 유연한 네임스페이스 지원  |
| Action, Service 구조    | 동작은 있으나 느슨함                 | 명확한 타입 정의와 동기/비동기 API    |

> 📌 ROS 2는 ROS 1의 단점을 보완하고 산업용, 멀티 로봇, 실시간 애플리케이션까지 확장 가능하도록 설계된 차세대 로봇 운영체제입니다.


---

## ⚙️ 2. ROS 2 Humble 설치

https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html

