#Author AHIRU

def is_integer(val):
	if val%2 == 0:
		return True
	else:
		return False

def get_mid_value(val_list, quartile_pos):
	index_mid_point_of_list = (len(val_list)+1)/quartile_pos
	if is_integer(index_mid_point_of_list):
		if quartile_pos > 0:
			return val_list[int(index_mid_point_of_list)-1]
		else: 
			return val_list[int(index_mid_point_of_list)]
	else:
		mid_index_2 = int(round(index_mid_point_of_list))
		mid_index_1 = mid_index_2 - 1
		return (val_list[mid_index_1] + val_list[mid_index_2]) / 2

def get_five_numbers(val_list):
	sorted_val_list = sorted(val_list)
	midian = get_mid_value(sorted_val_list, 2)
	first_quartile = get_mid_value(sorted_val_list, 4)
	third_quartile =  get_mid_value(sorted_val_list, -4)
	return [min(sorted_val_list), first_quartile, midian, third_quartile, max(sorted_val_list)]

def get_iqr(first_quartile, third_quartile):
	return third_quartile - first_quartile

def get_outlier_index(val_list, lower_bound, upper_bound):
	return [i for i, val in enumerate(val_list) if val < lower_bound or val > upper_bound]

def replace_outlier(val_list, outlier_index_list):
	val_list = [val for val in val_list]
	outlier_index_list = sorted(outlier_index_list, reverse=True)
	for index in outlier_index_list:
		val_list[index] = val_list[index - 1]
	return val_list

def remove_outlier(val_list, outlier_index_list):
	val_list = [val for val in val_list]
	outlier_index_list = sorted(outlier_index_list, reverse=True)
	for index in outlier_index_list:
		del val_list[index]
	return val_list

#example main
original_list = [2.03,2.17,3.14,3.44,1.29,2.17,3.35,5.86,4.48,4.8,4.89,3.09,0.82,2.03,3.4,2.49,1.98,2.08,3.05,3.35,2.77,4.39,5.17,3.85,2.04,3.83,3.67,1.75,4.12,3.14,2.54,4.26,3.69,4.17,2.86,2.4,2.54,2.31,2.94,2.08,3.94,1.71,0.72,1.66,2.99,2.04,3.74,3.12,1.48,1.68,4.89,3.22,2.76,2.86,0.91,2.08,1.49,2.4,2.94,2.08,1.15,0.59,3.92,1.4,0.69,0.95,0.05,0.09,1.31,2.35,2.13,1.43,1.77,1.77,1.25,1.45,0.42,1.72,1.02,1.49,0.5,0.23,0.63,1.48,3.26,1.89,2.26,1.89,3.26,1.18,2.12,3.85,2.91,3.67,3.37,2.17,2.49,3.05,1.77,1.48,1.99,4.2,5.71,5.22,3.67,2.9,1.06,0.45,2.77,3.98,2.45,1.72,2.26,1.11,2.22,3.97,3.98,2.08,2.49,0.36,0.28,1,1.43,1.95,1.48,1.4,1.63,1.34,0.32,1.89,3.08,3.78,2.94,1.18,0.65,1.04,1.66,2.26,1.52,1.95,1.45,2.12,0.5,1.25,2.4,1.38,3.35,1.18,2.54,1.49,1.89,2.31,4.66,3.71,1.99,1.38,0.72,0,1.68,3,1.63,0.63,0.97,1.4,0.83,0.41,0.14,1.18,0.14,1.85,2.22,2.17,4.26,2.22,1.86,2.58,1.52,0.27,0.09,0,0,
0,0,0.28,1.18,2.54,3.08,0.97,0.91,0.27,0.05,0.18,0.51,0.82,1.29,1.31,1.18,1.57,3.85,3.05,3.12,4.15,0.86,3.42,2.99,1.98,1.99,2.67,5.12,1.58,2.72,3.17,3.97,2.31,1.81,2.95,2.99,1.94,1.63,3.09,5.52,5.39,1.2,0.5,1.8,3.03,3.69,2.94,3.22,4.85,6.79,3.69,4.98,1.8,2.76,4.94,2.63,3.89,2.68,5.62,5.95,3.58,3.08,3,5.71,3.42,3.17,3.37,4.12,4.17,2.49,1.95,2.03,1.81,2.31,2.31,2.72,3,1.71,2.63,3.67,2.91,1,1.77,4.34,5.16,2.31,0.91,3.23,3.35,2.86,4.89,3.09,2.72,5.03,2.12,1.54,0.6,2.4,4.57,6.61,2.72,2.86,3.71,1.8,2.08,2.82,1.27,2.31,5.16,4.57,2.68,1.54,2.31,2.9,2.26,2.31,2.26,2.82,4.08,4.38,5.93,5.54,3.17,3.74,5.43,1.45,1.34,0.83,3.62,7.65,3.05,4.89,4.39,4.21,4.21,6.18,4.85,4.15,3.8,5.54,3.17,4.25,2.17,3.17,3.23,4.62,1.38,5.39,5.19,5.68,4.24,1.95,1.45,4.71,2.76,3.18,4.94,2.81,4.94,5.25,4.2,5.51,2.7,3.75,1.44,4.8,6.7,4.36,7.2,4.8,4.8,21.6,4.03,3.58,4.34,4.57,3.46,4.12,3.12,1.98,2.9,3.92,3.17,5.63,2.63,2.68,2.85,3.65,3.8,4.57,3.78,0.91,5.35,3.08,3.78,3.58,4.39,1.2,3.89,4.34,3.98,3.32,3.03,2.76,2.68,4.21,1.06,5.16,2.31,2.76,3.09,3.49,1.75,2.63,2.17,2.91,5.16,6.55,3.58,2.58,4.66,4.94,3.55,2.94,3.51,2.86,3.71,3.17,3.46,4.53,5.26,3.31,3.89,3.51,5.52,2.94,4.98,4.75,3.14,2.04,4.02,2.08,2.81,1.34,0.59,2.03,2.35,1.38,0.32,2.4,2.67,6.09,2.08,6.29,4.29,3.08,3,2.58,1.94,1.77,2.49,1.94,0.41,3.37,2.13,2.58,3.8,2.17,4.06,3.89,3.83,4.12,2.86,3.67,1.81,2.12,1.54,3.37,2.9,3.42,3.03,2.17,3,1.9,4.29,2.72,1.52,4.17,4.17,1.52,1.99,0.92,1.27,1.8,1.86,0.18,1.45,3.67,3.55,1.58,2.68,2.9,3.78,2.45,2.04,1.29,1.95,2.03,1.72,3.05,2.54,3.23,1.49,1.04,2.35,3.12,1.62,2.04,2.31,2.67,2.26,2.08,2.81,2.58,2.22,2.08,2.63,1.86,0.88,1.36,1.48,1.31,1.71,2.45,1.11,1.72,1.45,0.78,0.82,2.54,0.68,0.72,1.85,1.49,1.06,1.99,1.25,1.68,1.04,1.38,1.58,1.43,1.45,0.8,1.03,1.59,1.62,1.8,2.68,1.08,1.22,0.69,0,0.68,0,0.05,0,0.88,1.04,0.14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0.14,0.97,0.05,
0,0,0.54,1.25,1.45,1.62,0,0.37,2.58,3.12,3,2.81,3,3.4,4.66,3.4,2.77,1.13,2.86,2.63,2.63,7.06,5.8,3.88,3.53,2.95,3.94,5.21,3,4.21,4.66,5.8,3.69,5.75,7.47,5.86,6.2,4.2,3.31,3.05,3.08,3.28,1.86,0.23,2.63,1.36,1.66,1.54,4.25,6.93,7.25,4.35,2.04,4.75,6.29,4.57,4.94,3.09,4.44,4.39,6.28,4.89,6.23,6.02,4.2,4.3,2.76,
3.55]
five_numbers = get_five_numbers(original_list)
print('Original list:\n', 'Lenght:', len(original_list),'\n', sorted(original_list))
print('\nFive numbers: [MIN, Q1, Midian, Q3, MAX] ->', five_numbers)
iqr = get_iqr(five_numbers[1], five_numbers[3])
print('IQR:', iqr)
lower_bound = five_numbers[1] - 1.5*(iqr)
upper_bound = five_numbers[3] + 1.5*(iqr)
print('Lower bound:', lower_bound, '\nUpper bound:', upper_bound)
outlier_index_list = get_outlier_index(original_list, lower_bound, upper_bound)
print('Outlier index list:', outlier_index_list)
outlier_fixed_list = replace_outlier(original_list, outlier_index_list)
print('\nNew list:\n', 'Lenght:', len(outlier_fixed_list),'\n', sorted(outlier_fixed_list))
