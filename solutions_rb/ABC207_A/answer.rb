card = gets.chomp.split.map{ |e| e.to_i }
sorted_card = card.sort
sorted_card.shift
puts sorted_card.sum