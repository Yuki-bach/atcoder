a, b, c = gets.chomp.split.map { |e| e.to_i }
if a == b
  puts c
elsif b == c
  puts a
elsif c == a
  puts b
else
  puts 0
end
