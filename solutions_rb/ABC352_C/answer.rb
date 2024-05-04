n = gets.chomp.to_i
max_head = 0
sum = 0

n.times do
  a, b = gets.chomp.split.map { |e| e.to_i }
  max_head = [b - a, max_head].max
  sum += a
end

sum += max_head
puts sum
