import math

# masukan vector dapat bertipe list atau semacamnya 
# menggunakan library math

def dot(vector1, vector2):

	result = []	

	for i in range(len(vector1)):
		result.append(vector1[i] * vector2[i])

	return sum(result)

def length(vector):

	dot_product = dot(vector, vector)
	result = round(math.sqrt(dot_product), 3)

	return result

# angle
def angle(vector1, vector2):

	formula = math.acos(dot(vector1, vector2) / (length(vector1) * length(vector2)))

	return "{} derajat".format(round(math.degrees(formula), 3))
