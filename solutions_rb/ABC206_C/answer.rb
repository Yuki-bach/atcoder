n = gets.to_i
a = gets.chomp.split.map { |e| e.to_i }

element_count = Hash.new(0)

a.each do |e|
  element_count[e] += 1
end

same_pair_cnt = 0
element_count.each do |_, cnt|
  same_pair_cnt += cnt * (cnt - 1) / 2
end

puts n * (n-1) / 2 - same_pair_cnt