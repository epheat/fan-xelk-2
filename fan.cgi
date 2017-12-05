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

def print_game(game_p, searchterm_p, win)
  if win
    puts "<div class='game win'>"
  else
    puts "<div class='game loss'>"
  end

  game_p.each do |value|
    if value[0] == searchterm_p
      puts "<span><b>#{value[0]}: #{value[1]}</b></span><br>"
    else
      puts "<span>#{value[0]}: #{value[1]}</span><br>"
    end
  end

  puts "</div>"
end

def print_results(season_file, searchterm_p)
  # puts "<p>season_file: #{season_file}</p>"
  # puts "<p>searchterm_p: #{searchterm_p}</p>"
  season_results = JSON.parse(open(season_file).read)
  puts "<h3>"
  season_results["comments"].each do |comment|
    puts "#{comment}"
  end
  puts "</h3>"

  wins = 0
  losses = 0

  puts "<div id='resultsList'>"
  season_results["games"].each do |game|
    if game["WinorLose"] == "W"
      wins += 1
      print_game(game, searchterm_p, true)
    else
      losses += 1
      print_game(game, searchterm_p, false)
    end
  end
  puts "</div>"

  puts "<div id='percentage'>"
  puts "<p>Wins: #{wins}</p>"
  puts "<p>Losses: #{losses}</p>"
  puts "<p>Percentage: #{(wins.to_f / (wins+losses)) * 100}%</p>"
  puts "</div>"

end

def print_report(sports, sport_p, season_p, searchterm_p)
  # puts "<p>sport: #{sport_p}</p>"
  # puts "<p>season: #{season_p}</p>"
  # puts "<p>searchterm: #{searchterm_p}</p>"
  foundResults = false
  sports["sport"].each do |sport|
    if sport["title"] == sport_p
      sport["results"].each do |season|
        if season[0] == season_p
          foundResults = true
          print_results(season[1], searchterm_p)
        end
      end
    end
  end

  if foundResults == false
    puts "Results were not found for that sport and season."
  end
end

# page header
puts "Content-type: text/html\n\n"
puts "<style>#form { outline: 1px solid} #percentage { background-color: rgb(232, 231, 139)} .game { margin-bottom: 10px } .win {background-color: rgb(162, 222, 170)} .loss {background-color: rgb(201, 129, 129)}</style>"

puts "<h1>fan-xelk-2</h1>"

# if the sport is missing or the season is missing, display the form
if cgi["sport"] == "" || cgi["season"] == ""
  print_form(sports)
else
  print_form(sports)
  searchterm = "none"
  if cgi["searchterm"] != ""
    searchterm = cgi["searchterm"]
  end
  print_report(sports, cgi["sport"], cgi["season"], searchterm)
end
