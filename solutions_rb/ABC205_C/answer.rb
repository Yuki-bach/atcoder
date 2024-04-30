a, b, c = gets.chomp.split.map { |e| e.to_i }
minimum_c = c.even? ? 2 : 1
a_powered = a.pow(minimum_c)
b_powered = b.pow(minimum_c)

if a_powered < b_powered
  puts "<"
elsif a_powered > b_powered
  puts ">"
else
  puts "="
end
