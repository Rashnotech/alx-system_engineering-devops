#!/usr/bin/env ruby
# a ruby script that accepts on arguments and match repitition
puts ARGV[0].scan(/h(b|t){1,}n/).join
