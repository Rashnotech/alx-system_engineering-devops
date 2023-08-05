#!/usr/bin/env ruby
# a script that accept one argument and pass it to a regular expression
puts ARGV[0].scan(/h.+n/).join
