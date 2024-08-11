def find_intersection_length(a, b, c, d)
  [0, [b, d].min - [a, c].max].max
end

def check_intersection(diagonal1, diagonal2)
  dimensions = (0..2).map do |i|
    find_intersection_length(diagonal1[i], diagonal1[i+3], diagonal2[i], diagonal2[i+3])
  end
  dimensions.all?(&:positive?)
end

diagonal1 = gets.split.map(&:to_i)
diagonal2 = gets.split.map(&:to_i)
puts check_intersection(diagonal1, diagonal2) ? 'Yes' : 'No'
