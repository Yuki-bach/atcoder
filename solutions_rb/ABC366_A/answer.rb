n, t, a = gets.split.map(&:to_i)
projected = [t, a].max > n / 2
puts projected ? 'Yes' : 'No'