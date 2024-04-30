n, k = gets.chomp.split.map { |e| e.to_i }
a = gets.chomp.split.map { |e| e.to_i }

base = k / n
remainder = k % n

a_sorted = a.sort
threshold = a_sorted[remainder]

a.each do |x|
  count = base + (x < threshold ? 1 : 0)
  puts count
end