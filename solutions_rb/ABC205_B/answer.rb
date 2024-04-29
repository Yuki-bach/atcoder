n = gets.to_i
a = gets.chomp.split.map{ |e| e.to_i }
a_sorted = a.sort
puts (1..n).to_a == a_sorted ? "Yes" : "No"