N, K, X = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)
ans = A.insert(K, X).join(' ')
puts ans
