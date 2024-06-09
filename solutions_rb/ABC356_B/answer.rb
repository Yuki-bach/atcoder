n, m = gets.chomp.split.map { |e| e.to_i }
a = gets.chomp.split.map { |e| e.to_i }
sum_list = Array.new(m, 0)

n.times do |i|
  x = gets.chomp.split.map { |e| e.to_i }
  sum_list.each_with_index do |sum, i|
    sum_list[i] += x[i]
  end
end

all_exceed = sum_list.each_with_index.all? { |sum, i| sum >= a[i] }
puts all_exceed ? "Yes" : "No"