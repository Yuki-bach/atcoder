n = gets.chomp.to_i
tax_added = (n * 1.08).floor

if tax_added < 206
  puts "Yay!"
elsif tax_added == 206
  puts "so-so"
else
  puts ":("
end