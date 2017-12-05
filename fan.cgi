#!/usr/bin/ruby

# Evan Heaton & Robert Cala
# fan-xelk-2

require 'cgi'
require 'json'
cgi = CGI.new

# read the sports.json file
sports = JSON.parse(open("Sports.json").read)

def print_form(sports)
  puts '<form id="form" action="fan.cgi" method="get">'
  puts '  <label>Select a sport:</label>'
  puts '  <select name="sport">'
  sports["sport"].each do |sport|
    puts "  <option value='#{sport["title"]}'>#{sport['title']}</option>"
  end
  puts '  </select><br>'
  puts '  <label>Select a season:</label>'
  puts '  <select name="season">'
  sports["sport"].each do |sport|
    sport["results"].each do |season|
      puts "  <option value='#{season[0]}'>#{season[0]}</option>"
    end
  end
  puts '  </select><br>'
  puts '  <label>Select a searchterm:</label>'
  puts '  <select name="searchterm">'
  sports["sport"].each do |sport|
    sport["searchterms"].each do |searchterm|
      puts "  <option value='#{searchterm}'>#{searchterm}</option>"
    end
  end
  puts '  </select><br>'
  puts '  <input type="submit" value="Search!"/>'
  puts '</form>'
end

def print_report(sport, season, searchterm)
  puts "<p>sport: #{sport}</p>"
  puts "<p>season: #{season}</p>"
  puts "<p>searchterm: #{searchterm}</p>"
end

# page header
puts "Content-type: text/html\n\n"
puts "<h1>fan-xelk-2</h1>"

# if the sport is missing or the season is missing, display the form
if cgi["sport"] == "" || cgi["season"] == ""
  print_form(sports)
else
  searchterm = "none"
  if cgi["searchterm"] != ""
    searchterm = cgi["searchterm"]
  end
  print_report(cgi["sport"], cgi["season"], searchterm)
end
