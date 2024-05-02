n, k = gets.chomp.split.map { |e| e.to_i }
h_place = (1..n).sum * 100 * k
o_place = (1..k).sum * n
puts h_place + o_place