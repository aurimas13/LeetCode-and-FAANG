n_english = int(input())
n_roll = set(map(int,input().strip().split()))
b_french  = int(input())
b_roll = set(map(int,input().strip().split()))
both_subscriptions = n_roll.intersection(b_roll)
print(both_subscriptions)
print(len(both_subscriptions))

