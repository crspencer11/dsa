def min_max_distance(stalls: list[int], cows: int):
    stalls.sort()
    l = 1
    r = stalls[-1] - stalls[0]

    def good(distance: int) -> bool:
        count = 1
        last_pos = stalls[0]

        for stall in stalls:
            if stall - last_pos >= distance:
                count += 1
                last_pos = stall
        return count >= cows

    while l < r:
        mid = (l + r + 1) // 2 
        if good(mid):
            l = mid
        else:
            r = mid - 1

    return l