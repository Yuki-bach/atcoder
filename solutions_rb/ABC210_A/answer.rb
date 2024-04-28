n, a, x, y = gets.chomp.split.map{ |e| e.to_i }
sum = 0
(1..n).each { |i| sum += i <= a ? x : y }

puts sum