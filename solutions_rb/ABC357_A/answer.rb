n, m = gets.chomp.split.map(&:to_i)
h = gets.chomp.split.map(&:to_i)

h.each_with_index do |hand, i|
  if m - hand < 0
    puts i
    exit
  else
    m -= hand
  end
end

puts n