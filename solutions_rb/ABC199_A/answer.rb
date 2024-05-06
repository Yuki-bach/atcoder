a, b, c = gets.chomp.split.map { |e| e.to_i }
puts a*a + b*b < c*c ? "Yes" : "No"