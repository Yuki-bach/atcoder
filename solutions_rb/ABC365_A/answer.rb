y = gets.to_i
is_leap_year = y % 4 == 0 && (y % 100 != 0 || y % 400 == 0)
puts is_leap_year ? 366 : 365