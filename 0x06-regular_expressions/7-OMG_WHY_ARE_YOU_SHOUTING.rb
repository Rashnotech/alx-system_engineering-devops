#!/usr/bin/env ruby
# a script that matches capital letters
puts ARGV[0].gsub(/\s+/,'').scan(/[A-Z]/).join
