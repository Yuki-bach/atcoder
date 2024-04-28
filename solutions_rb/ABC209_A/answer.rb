a, b = gets.chomp.split.map{ |e| e.to_i }
puts a <= b ? b - a + 1 : 0