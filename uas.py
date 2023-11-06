import vector_calc as vc

vector_dimension = int(input())

vector1 = list(map(int, input().split()))
vector2 = list(map(int, input().split()))

res = vc.dot(vector1, vector2)
res1 = vc.vector_length(vector1), vc.vector_length(vector2)
res2 = vc.angle(vector1, vector2)


print(res)
print(res1)
print(res2)
