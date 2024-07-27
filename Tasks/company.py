def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()
    return len(selected_items)


num_arr = int(input())

items = []
i = 0 

while i != num_arr :
    
    items.append(i+1)
    i = i + 1

my_list_prices = []

i = 0

while i != num_arr :
    
    my_list_prices.append(int(input()))
    i = i + 1
    
budjet = int(input())    

result = knapsack(items , my_list_prices , budjet)

if result > 4 :
    
    print(4)

else :
    
    print(result)