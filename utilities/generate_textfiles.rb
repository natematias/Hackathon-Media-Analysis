require 'date'
require 'json'

json = JSON.load(File.open(ARGV[0]).read)

json.each do |row|
  File.open(File.join(ARGV[1], row["story_sentences"][0]["stories_id"].to_s + ".txt"), "w"){|file|
    file.write(row["story_text"])
  }
end
