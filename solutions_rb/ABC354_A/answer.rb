h = gets.chomp.to_i
p_h = 0
day = 0

while p_h <= h do
  p_h += 2**day
  day += 1
end

puts day