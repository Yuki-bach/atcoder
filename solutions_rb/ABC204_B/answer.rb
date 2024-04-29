n = gets.to_i
a = gets.chomp.split.map{ |e| e.to_i }
sum = 0
a.each do |x|
  sum += x > 10 ? x - 10 : 0
end

puts sum