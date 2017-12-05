#!/usr/bin/ruby

# Evan Heaton & Robert Cala
# fan-xelk-2

require 'cgi'
cgi = CGI.new

puts "Content-type: text/html\n\n"
puts "<h1>fan-xelk-2</h1>"

# if the sport is missing or the season is missing, display the form
if cgi["sport"] == "" || cgi["season"] == ""
  puts "form"
else
  puts "report"
end
