class Solutions():
    def finish(self, effect, coffeeNum, bugTime):
        if coffeeNum > 8:
            coffeeNum = 8
        totalTime, totalSpend = 0, 0
        for x in bugTime:
            totalTime += x
        while coffeeNum != 0 and totalTime > 0:
            totalTime -= 60 * effect   # 工作一小时相当于减少了effect小时的工作量
            coffeeNum -= 1
            totalSpend += 60
        if coffeeNum == 0 and totalTime - (8 * 60 - totalSpend) > 0:
            return 0
        elif totalTime <= 0: # 说明提前完成了
            return totalSpend + totalTime // effect
        else:
            return totalSpend + totalTime

if __name__ == '__main__':
    bugNum, effect, coffeeNum = list(map(int, input().split()))
    bugTime = list(map(int, input().split()))
    solution = Solutions()
    print(solution.finish(effect, coffeeNum, bugTime))