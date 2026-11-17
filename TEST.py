test = [4, 3, 4, 5, 1, 2]

test.append(5)

test[0] = 6

test.pop()

count = 0

for i in test:
    count += i

print(count)
print(sorted(test))
print(test)
test_tuple = tuple(test)
print(test_tuple)
print(test_tuple[0])
print(test_tuple[-1])