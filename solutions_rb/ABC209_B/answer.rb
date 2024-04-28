n, x = gets.chomp.split.map{ |e| e.to_i }
a = gets.chomp.split.map{ |e| e.to_i }
a.each_index { |i| a[i] -= 1 if (i+1).even? }
puts x >= a.sum ? "Yes" : "No"