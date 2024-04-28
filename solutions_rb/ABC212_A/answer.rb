a, b = gets.chomp.split.map{ |e| e.to_i }
if 0<a && b==0
  puts "Gold"
elsif a==0 && 0 < b
  puts "Silver"
else
  puts "Alloy"
end