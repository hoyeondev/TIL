import time

# 슬라이딩 윈도우를 활용한 타자 훈력 분석기
''' 동작방식
1. 샘플 문장 출력 → [Enter] 누르면 타이머 시작
2. 사용자 입력(타자 훈련)
3. 통계 계산
4. 오타 비교 및 출력
5. 슬라이딩 윈도우 분석 및 결과 출력
'''

# 슬라이딩 윈도우 정확도 분석
# parm : 샘플 텍스트, 유저 입력텍스트, 슬라이딩 윈도우값
def sliding_window_analysis(target: str, typed: str, window_size: int = 10):
    results = []
    # 샘플과 유저 입력값의 정확도를 체크(구간별로 슬라이딩 이동)
    for i in range(0, min(len(target), len(typed)) - window_size + 1, window_size):
        target_window = target[i:i+window_size]
        typed_window = typed[i:i+window_size]
        correct = sum(1 for a, b in zip(target_window, typed_window) if a == b)
        accuracy = correct / window_size * 100
        results.append((i, accuracy))
    return results

# 오타 시각화
# parm : 샘플 텍스트, 유저 입력텍스트
def print_mismatch(target: str, typed: str):
    print("\n🔎 오타 분석:")
    result = []
    for i in range(len(target)):
        if i < len(typed) and target[i] == typed[i]:
            result.append(target[i])
        else:
            result.append("_" if i < len(typed) else " ")
    print("정답   :", target)
    print("입력값 :", typed)
    print("오타표시:", "".join(result))

### 메인 실행함수 ###
def main():
    sample_text = "The quick brown fox jumps over the lazy dog."
    print("😀️  타자 훈련을 시작합니다.\n")
    print("✍️  아래 문장을 그대로 입력하세요:\n")
    print(f"📌  {sample_text}\n")

    input("⏳ 준비되면 Enter 키를 누르세요...")

    start_time = time.time() # 입력 시작
    user_input = input("\n🧑 입력 > ")
    end_time = time.time() # 입력 종료

    elapsed_time = end_time - start_time
    char_count = len(user_input)
    speed = char_count / elapsed_time * 60  # 타자 속도 (CPM)
    
    # 전체 정확도 체크
    correct_chars = sum(1 for a, b in zip(sample_text, user_input) if a == b)
    accuracy = correct_chars / len(sample_text) * 100

    print("\n📊 결과 요약:")
    print(f"- 입력 시간: {elapsed_time:.2f}초")
    print(f"- 타자 속도: {speed:.2f} CPM (문자/분)")
    print(f"- 정확도: {accuracy:.2f}%")
    
    # 오타 시각화 함수 호출
    print_mismatch(sample_text, user_input)

    print("\n🪟 슬라이딩 윈도우 분석 (10글자 단위 정확도):")
    windows = sliding_window_analysis(sample_text, user_input)
    # print(windows)
    # windows 출력 결과 : [(0, 100.0), (10, 100.0), (20, 100.0), (30, 100.0)]
    for i, acc in windows:
        print(f"  [{i:02d}~{i+9}] : {acc:.1f}%")

if __name__ == "__main__":
    main()
