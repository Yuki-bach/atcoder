hit_list = Array.new(4){ gets.chomp }
puts hit_list.sort == ["2B", "3B", "H", "HR"] ? "Yes" : "No"