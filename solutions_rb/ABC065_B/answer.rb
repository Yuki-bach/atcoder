n = gets.to_i
a = n.times.map { gets.to_i }

if !a.include?(2)
  puts -1
else
  ans = -1
  cur = 1
  (1..n).each do |cnt|
    cur = a[cur - 1]
    if cur == 2
      ans = cnt
      break
    end
  end

  puts ans
end
