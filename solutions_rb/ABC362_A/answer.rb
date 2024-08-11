r, g, b = gets.split.map(&:to_i)
c = gets.chomp
case c
when 'Red'
  puts [g, b].min
when 'Green'
  puts [r, b].min
when 'Blue'
  puts [r, g].min
end
