## Order(n^2)
def two_sum_nsquare(list1,target):
	for i in range(len(list1)):
		for j in range(i,len(list1)):
			if( (i!=j) and (list1[i] + list1[j])==target):
				return (i,j)

## Order(n)
def two_sum_n(list1,target):
	hash_map = {}
	for i in range(len(list1)):
		temp_sub = target - list1[i]
		if temp_sub in hash_map.keys():
			return (hash_map[temp_sub] , i)
		hash_map[list1[i]] = i


if __name__ == "__main__":
	list1 = list(map(int,input("Enter the list elements : ").split()))
	target = int(input("Enter the target element : "))
	print(two_sum_nsquare(list1,target))
	print(two_sum_n(list1,target))
	

