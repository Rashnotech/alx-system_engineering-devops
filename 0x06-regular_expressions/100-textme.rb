#!/usr/bin/env ruby
# a script that print sender, receiver and flags
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
