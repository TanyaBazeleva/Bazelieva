from collections import deque
import sys
def main():
    n = int(input())
    first_player = deque(map(int, input().split()))
    second_player = deque(map(int, input().split()))
    max_moves = 200000
    for i in range(max_moves):
        if not first_player:
            print("second", i)
            return
        if not second_player:
            print("first", i)
            return
        cartu1 = first_player.popleft()
        cartu2 = second_player.popleft()
        if (cartu1 > cartu2 and not (cartu1 == n - 1 and cartu2 == 0)) or (cartu1 == 0 and cartu2 == n - 1):
            first_player.append(cartu1)
            first_player.append(cartu2)
        else:
            second_player.append(cartu1)
            second_player.append(cartu2)
    print("draw")
if __name__ == "__main__":
    main()
