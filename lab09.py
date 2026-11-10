def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit


def max_subarray(nums):

    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0


def main():
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5 (buy at 1, sell at 6)
    print(max_profit([7, 6, 4, 3, 1]))  # 0 (no profit)
    is_balanced("()[]{}")   # returns True
    is_balanced("{[]}")     # returns True
    is_balanced("([)]")     # returns False   (closed in the wrong order)


if __name__ == "__main__":
    main()
