def max_score(m, tracks, current_sum=0, index=0):
    global best_sum
    if current_sum > m:
        return
    best_sum = max(best_sum, current_sum)
    if index == len(tracks):
        return
    max_score(m, tracks, current_sum + tracks[index], index + 1)
    max_score(m, tracks, current_sum, index + 1)

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().split("\n")
    for line in input_data:
        data = list(map(int, line.split()))
        m, n = data[0], data[1]
        tracks = data[2:]
        best_sum = 0
        max_score(m, tracks)
        print(f"sum:{best_sum}")
