class Knapsack:

    def __init__(self):

        self.data = {}
        self.data['profit'] = [20, 30, 66, 40, 60]
        self.data['weight'] = [10, 20, 30, 40, 50]
        self.data['maxWeight'] = 100

    def getBestItem(self, candidates):
        best_ratio = -1
        best_item = -1

        for candidate in candidates:
            ratio = self.data['profit'][candidate] / self.data['weight'][candidate]
            if ratio > best_ratio:
                best_ratio = ratio
                best_item = candidate

        return best_item

    def isFeasible(self, best_item, freeWeight):
        return self.data['weight'][best_item] <= freeWeight

    def greedyKnapsack(self):
        n = len(self.data['profit'])
        candidates = set()
        result = [0] * n
        freeWeight = self.data['maxWeight']
        isSolution = False
        for i in range(n):
            candidates.add(i)

        while not isSolution and candidates:
            best_item = self.getBestItem(candidates)
            candidates.remove(best_item)
            if self.isFeasible(best_item, freeWeight):
                result[best_item] = 1.0
                freeWeight -= self.data['weight'][best_item]
            else:
                result[best_item] = freeWeight / self.data['weight'][best_item]
                isSolution = True

        return result

if __name__ == '__main__':
    k = Knapsack()
    sol = k.greedyKnapsack()
    print(sol)