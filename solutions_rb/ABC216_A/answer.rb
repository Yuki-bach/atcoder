x, y = gets.split(".").map{ |e| e.to_i }
if y <= 2
  puts "#{x}-"
elsif y <= 6
  puts "#{x}"
else
  puts "#{x}+"
end