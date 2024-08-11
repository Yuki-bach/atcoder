DIRECTIONS = {
  'L' => [0, -1],
  'R' => [0, 1],
  'U' => [-1, 0],
  'D' => [1, 0]
}

def can_move?(grid, h, w, row, col)
  row.between?(0, h - 1) && col.between?(0, w - 1) && grid[row][col] == '.'
end

h, w = gets.split.map(&:to_i)
start = gets.split.map(&:to_i).map { |i| i - 1 }  # 0-indexed
grid = h.times.map { gets.chomp.chars }
moves = gets.chomp
# simulation
current = start
moves.each_char do |move|
  drow, dcol = DIRECTIONS[move]
  new_row, new_col = current[0] + drow, current[1] + dcol
  current = [new_row, new_col] if can_move?(grid, h, w, new_row, new_col)
end
final_position = current.map { |i| i + 1 }  # 1-indexed

puts final_position.join(' ')