#!/usr/bin/env ruby
# a ruby script that accept on argument and pass it to a regular expression
puts ARGV[0].scan(/\School/).join
