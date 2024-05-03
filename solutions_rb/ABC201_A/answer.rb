a = gets.chomp.split.map { |e| e.to_i }
a_sorted = a.sort()
checker = a_sorted[1] - a_sorted[0] == a_sorted[2] - a_sorted[1]
puts checker ? "Yes" : "No"