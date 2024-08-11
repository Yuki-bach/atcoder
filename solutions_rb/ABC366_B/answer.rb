n = gets.to_i
s = n.times.map { gets.chomp }
m = s.max_by(&:length).length

s.map! { |x| x.ljust(m, '*').chars }
rotated = s.transpose.map(&:reverse)
rotated.each { |x| puts x.join.sub(/\*+$/, '') }
