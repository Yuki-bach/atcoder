a, b = gets.chomp.split.map{ |e| e.to_i }
puts (1*a <= b && b <= 6*a) ? "Yes" : "No"