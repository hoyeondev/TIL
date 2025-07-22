import random
import os

'''
그리디 알고리즘을 이용한 그리드 게임
1. 격자판에 숫자(1~5)와 시작점(S)이 무작위로 배치
2. 사용자는 현재 S 위치에서 가장 가까운 숫자를 추론해서 입력
3. 정답이면 해당 숫자는 제거되고 점수를 얻는다.
4. 오답일 경우 점수 차감(1점)
5. 모든 숫자를 제거하면 게임 종료!
'''

# 초기 설정
GRID_SIZE = 7 # 그리드 사이즈
NUMBERS = [1, 2, 3, 4, 5] # 게임 숫자

# 초기화
def clear():
    #os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls')

# 그리디 알고리즘 사용
def manhattan_distance(a, b):
    # abs 절대값 함수 사용
    # x축, y축끼리 계산
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 'S':
                print('\033[91mS\033[0m', end=' ')  # 빨간색
            elif cell.isdigit():
                print(f'\033[94m{cell}\033[0m', end=' ')  # 파란색
            else:
                print(cell, end=' ')  # 점(.)은 기본색
        print()
    print()

# 그리디 알고리즘 사용
# parm : s 위치, 숫자별 위치
def closest_number(pos, numbers):
    # 그리디하게 가장 가까운 숫자 선택
    closest = min(numbers.items(), key=lambda item: manhattan_distance(pos, item[0]))
    return closest

# 그리드 생성
def create_grid():
    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # 시작점 설정
    start_x, start_y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    grid[start_x][start_y] = 'S'
    start_pos = (start_x, start_y)

    # 숫자 배치
    positions = {}
    for n in NUMBERS:
        while True:
            
            x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            if grid[x][y] == '.':
                grid[x][y] = str(n)
                positions[(x, y)] = n
                break

    return grid, start_pos, positions

# 플레이 함수
def play():
    grid, start_pos, number_positions = create_grid()
    score = 0

    while number_positions:
        clear()
        print(f"현재 점수: {score}\n")
        print_grid(grid)

        guess = input("📌 S와 가장 가까운 숫자는 무엇일까요? (1~5, 종료하려면 q): ").strip()

        if guess.lower() == 'q':
            print("👋 게임을 종료합니다.")
            break

        if not guess.isdigit() or int(guess) not in NUMBERS:
            print("❌ 유효한 숫자를 입력해주세요.")
            input("엔터를 눌러 계속...")
            continue
        
        # print(start_pos, number_positions)
        # 출력형태 : (5, 0) {(2, 5): 1, (3, 2): 2, (5, 3): 3, (4, 6): 4, (0, 3): 5}
        closest_pos, correct_number = closest_number(start_pos, number_positions)

        if int(guess) == correct_number:
            print("✅ 정답입니다!\n")
            grid[closest_pos[0]][closest_pos[1]] = '.'
            score += correct_number # 맞춘 숫자만큼 score에 합산
            del number_positions[closest_pos]
        else:
            print(f"❌ 오답입니다. 가장 가까운 숫자는 {correct_number}였습니다.")
            score -= 1 # 틀리면 점수 차감

        input("엔터를 눌러 계속...")

    clear()
    print('🎉 게임 종료!\n')
    print(f"ㅁ 총 점수: {score}")

# 게임 실행
if __name__ == "__main__":
    play()
