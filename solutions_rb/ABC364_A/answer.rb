SWEET = 'sweet'

def valid?(n)
  prev_sweet = false
  feel_sick = false
  n.times do
    return false if feel_sick
    current = gets.chomp
    feel_sick = true if prev_sweet && current == SWEET
    prev_sweet = (current == SWEET)
  end
  true
end

n = gets.to_i
puts valid?(n) ? 'Yes' : 'No'
