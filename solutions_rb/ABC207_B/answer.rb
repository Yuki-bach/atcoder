a, b, c, d = gets.chomp.split.map{ |e| e.to_i }

if b >= c * d
  puts(-1)
else
  n = 0
  n += 1 while a + (b * n) > c * n * d
  puts n
end
