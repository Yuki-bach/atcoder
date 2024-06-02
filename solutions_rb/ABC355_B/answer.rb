n, m = gets.chomp.split.map { |e| e.to_i }
a = gets.chomp.split.map { |e| e.to_i }
b = gets.chomp.split.map { |e| e.to_i }
c = (a + b).sort

ans = "No"
(n + m - 1).times do |i|
  if a.include?(c[i]) && a.include?(c[i+1])
    ans = "Yes"
    break
  end
end

puts ans