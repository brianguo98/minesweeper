# DO NOT EDIT -----------------------------------------------------------
require_relative 'solver'
require_relative 'board'

def run_solver(n, num_mines, num_trials)
    wins = 0
    current_percentage = 0
    start = Time.now
    for i in 0...num_trials
        board = Board.new(n, num_mines)
        if solve board
            wins += 1
        end

        current_percentage = (i + 1) * 100 / num_trials
        print("\r#{current_percentage}% complete (#{i+1}/#{num_trials})")
    end
    finish = Time.now
    puts
    delta = finish - start
    puts "Time taken: #{delta.round(2)}s"
    percentage = wins * 100.0 / num_trials
    puts "Win percentage: #{percentage.round(2)}% (#{wins}/#{num_trials})"
end

def parse_args 
    args = {}
    args[:n] = (n = ARGV[0]) ? Integer(n) : 10 
    args[:num_mines] = (num_mines = ARGV[1]) ? Integer(num_mines) : 10
    args[:num_trials] = (num_trials = ARGV[2]) ? Integer(num_trials) : 100000
    args
end

def main
    args = parse_args
    run_solver(args[:n], args[:num_mines], args[:num_trials])
end

main

# DO NOT EDIT -----------------------------------------------------------
