n = gets.chomp.to_i
players = n.times.map { |i| gets.split.tap { |arr| arr[1] = arr[1].to_i } }
players.sort_by! { |arr| arr[0].downcase }

t = players.map { |arr| arr[1] }.sum
winner_id = t % n
puts players[winner_id][0]