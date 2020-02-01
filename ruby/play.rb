require_relative 'board'

def main(n, num_mines)
    # TODO: Write commandline game
    raise NotImplementedError
end

# DO NOT EDIT--------------------------------------------

def parse_args 
    args = {}
    args[:n] = (n = ARGV[0]) ? Integer(n) : 10 
    args[:num_mines] = (num_mines = ARGV[1]) ? Integer(num_mines) : 10
    args
end

args = parse_args
main(args[:n], args[:num_mines])

# DO NOT EDIT--------------------------------------------
