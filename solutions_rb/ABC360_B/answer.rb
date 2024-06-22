n = gets.chomp.to_i
a = gets.chomp.split.map(&:to_i)
ans = 0
(n*2-2).times do |i|
  ans += 1 if a[i] == a[i+2]
end

puts ans