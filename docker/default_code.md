# Docker 명령어 정리

## 이미지 관련 명령어

- `docker build`: Dockerfile을 사용하여 이미지 빌드
  - 예시: `docker build -t myapp:latest .`

- `docker pull`: Docker Hub 또는 레지스트리에서 이미지 다운로드
  - 예시: `docker pull nginx:latest`

- `docker push`: 이미지를 Docker Hub 또는 레지스트리에 업로드
  - 예시: `docker push myregistry.azurecr.io/myapp:latest`

- `docker images`: 로컬에 있는 이미지 목록 확인
  - 옵션: `-a` (모든 이미지 출력), `-q` (ID만 출력)

- `docker rmi`: 이미지 삭제
  - 예시: `docker rmi nginx:latest`

## 컨테이너 관련 명령어

- `docker run`: 새로운 컨테이너 실행
  - 옵션: `-d` (백그라운드 모드), `-p` (포트 매핑), `--name` (컨테이너 이름 지정)
  - 예시: `docker run -d -p 8080:80 --name webapp nginx:latest`

- `docker start/stop/restart`: 컨테이너 시작/중지/재시작
  - 예시: `docker start webapp`

- `docker ps`: 실행 중인 컨테이너 목록 확인
  - 옵션: `-a` (모든 컨테이너 출력)

- `docker logs`: 컨테이너 로그 확인
  - 예시: `docker logs webapp`

- `docker exec`: 실행 중인 컨테이너에서 명령어 실행
  - 예시: `docker exec -it webapp bash`

- `docker rm`: 컨테이너 삭제
  - 옵션: `-f` (실행 중인 컨테이너도 삭제)
  - 예시: `docker rm webapp`

## 볼륨 관련 명령어

- `docker volume create`: 새로운 볼륨 생성
  - 예시: `docker volume create mydata`

- `docker volume ls`: 모든 볼륨 목록 확인

- `docker volume rm`: 볼륨 삭제
  - 예시: `docker volume rm mydata`

## 기타 명령어

- `docker system prune`: 사용하지 않는 이미지, 컨테이너, 볼륨, 네트워크 등 삭제

- `docker version`: Docker 버전 확인

- `docker info`: Docker 시스템 정보 확인
