x, y = gets.chomp.split.map{ |e| e.to_i }
puts x == y ? x : 3 - (x + y)