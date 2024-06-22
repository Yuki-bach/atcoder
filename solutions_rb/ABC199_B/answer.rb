n = gets.chomp.to_i
a = gets.chomp.split.map(&:to_i)
b = gets.chomp.split.map(&:to_i)

ans = a.max > b.min ? 0 : b.min - a.max + 1
puts ans