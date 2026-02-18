def max_boats(population: list[int], k: int) -> int:
    """
    An imminent hurricane threatens the coastal town of Codeville. 
    If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, 
    determine how many boats will be needed to save everyone.

    For example, given a population with weights [100, 200, 150, 80] 
    and a boat limit of 200, the smallest number of boats required will be three.
    """
    population.sort()
    total = 0
    idx = 0
    while idx < len(population)-1:
        while k - population[idx] > 0:
            subtracte = 
            idx += 1
         
    total += 1