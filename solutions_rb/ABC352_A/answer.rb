n, x, y, z = gets.chomp.split.map { |e| e.to_i }
checker = (x < z && z < y) || (y < z && z < x)
puts checker ? "Yes" : "No"