import heapq
def process(data):
    heap = []
    priors = {}
    res = []
    count = 0
    for line in data:
        parts = line.strip().split()
        if not parts:
            continue
        cmd = parts[0]
        if cmd == "ADD":
            id_ = parts[1]
            priority = int(parts[2])
            priors[id_] = priority
            heapq.heappush(heap, (-priority, count, id_))
            count += 1
        elif cmd == "POP":
            while heap:
                neg_priority, _, id_ = heapq.heappop(heap)
                if id_ in priors and priors[id_] == -neg_priority:
                    res.append(f"{id_} {-neg_priority}")
                    del priors[id_]
                    break
        elif cmd == "CHANGE":
            id_ = parts[1]
            new_priority = int(parts[2])
            priors[id_] = new_priority
            heapq.heappush(heap, (-new_priority, count, id_))
            count += 1
    return res

if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        data = f.readlines()
        result = process(data)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(result))
