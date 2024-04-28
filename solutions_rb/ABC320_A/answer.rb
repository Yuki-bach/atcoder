a, b, c = gets.split.map(&:to_i)
if a % c == 0
  first_multiple = a
else
  first_multiple = c * (a / c + 1)
end

if first_multiple <= b
  puts first_multiple
else
  puts(-1)
end