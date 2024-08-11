p1 = gets.split.map(&:to_i)
p2 = gets.split.map(&:to_i)
p3 = gets.split.map(&:to_i)

def squared_distance(a, b)
  (b[1] - a[1])**2 + (b[0] - a[0])**2
end

ls_arr = [squared_distance(p1, p2), squared_distance(p2, p3), squared_distance(p3, p1)]
puts ls_arr.max == ls_arr.min(2).sum ? 'Yes' : 'No'
