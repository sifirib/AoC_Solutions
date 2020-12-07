f = open("20_05_inputs", "r")
passes = [pass_.strip() for pass_ in f.readlines()]

def decode_row_column(pass_):
	row_raw = pass_[:7]
	column_raw = pass_[7:]
	lower_lim = 0
	upper_lim = 127
	for i in row_raw:
		if i == "F":
			upper_lim = upper_lim - (((upper_lim + 1) - lower_lim) / 2) 
		if i == "B":
			lower_lim = lower_lim + (((upper_lim + 1) - lower_lim) / 2)
		
	if not upper_lim == lower_lim:
		print(f"{lower_lim} and {upper_lim} is not same number!")
	else:
		row = upper_lim

	lower_lim = 0
	upper_lim = 7
	for i in column_raw:

		if i == "L":
			upper_lim = upper_lim - (((upper_lim + 1) - lower_lim) / 2)
		if i == "R":
			lower_lim = lower_lim + (((upper_lim + 1) - lower_lim) / 2)
	if not upper_lim == lower_lim:
		print(f"{lower_lim} and {upper_lim} is not same number!")
	else:
		column = upper_lim

	return int(row), int(column)

def get_seat_id(row, column):
	return row * 8 + column
	
#part one
#highest_id = 0
#for pass_ in passes:
#	row, column = decode_row_column(pass_)
#	id_ = get_seat_id(row, column)
#	if id_ > highest_id:
#		highest_id = id_
#print(highest_id)


#part two
taken_seats = [get_seat_id(decode_row_column(pass_)[0], decode_row_column(pass_)[1]) for pass_ in passes]
seats = [seat for seat in range(1 * 8 + 0, 126 * 8 + 7)]
empty_seats = []
for seat in seats:
	if not seat in taken_seats:
		empty_seats.append(seat)
print(empty_seats) # the answer is grinning in this list...