n = gets.to_i
a = gets.chomp.split.map{ |e| e.to_i }
point = a.sort.reverse[1]
puts a.index(point) + 1

## alternatives
# n = gets.to_i
# a = gets.split.map(&:to_i).each_with_index.sort
# puts a[-2][1] + 1
