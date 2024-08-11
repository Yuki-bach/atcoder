n = gets.to_i
a = gets.split.map(&:to_i)
puts a.index(a.max(2).min) + 1