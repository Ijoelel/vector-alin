import math

def dot(vector1, vector2):

	result = []	

	for i in range(len(vector1)):
		result.append(vector1[i] * vector2[i])

	return sum(result)

def vector_length(vector):
	
	dot_product = dot(vector, vector)
	result = math.sqrt(dot_product)

	return result

# angle
def angle(vector1, vector2):

	formula = math.acos(dot(vector1, vector2) / (vector_length(vector1)*vector_length(vector2)))

	return "{} derajat".format(int(math.degrees(formula)))
