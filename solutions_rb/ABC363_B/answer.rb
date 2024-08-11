n, t, p = gets.split.map(&:to_i)
l = gets.split.map(&:to_i)
target = l.sort.reverse[p - 1]
diff = t - target
pp diff.positive? ? diff : 0
