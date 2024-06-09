n, l, r = gets.chomp.split.map { |e| e.to_i }
ans = (1..n).to_a
ans[l-1...r] = ans[l-1...r].reverse
puts ans.join(' ')