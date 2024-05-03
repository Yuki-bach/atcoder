n = gets.to_i
mountains = (1..n).map { gets.chomp.split }
sorted_mountains = mountains.sort_by { |name, height| height.to_i }.reverse
puts sorted_mountains[1][0]