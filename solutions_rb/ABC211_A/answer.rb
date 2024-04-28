a, b = gets.chomp.split.map{ |e| e.to_i }
c = (a - b).to_f / 3 + b
puts c
