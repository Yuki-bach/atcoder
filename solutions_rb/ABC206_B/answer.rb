n = gets.to_i
sum = 0
d = 1

while sum < n
  sum += d
  d += 1
end

puts d - 1