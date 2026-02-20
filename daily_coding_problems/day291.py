def max_boats(population: list[int], k: int) -> int:
    """
    An imminent hurricane threatens the coastal town of Codeville. 
    If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, 
    determine how many boats will be needed to save everyone.
    """
    population.sort()
    left, right = 0, len(population) - 1
    total_boats = 0

    while left <= right:
        if population[left] + population[right] <= k:
            left += 1
        right -= 1
        total_boats += 1
        
    return total_boats