import mediacloud
import json
mc = mediacloud.api.MediaCloud()

# query mentions of civic hacking
res = mc.sentenceList('("civic hacking" OR "civic hackathon" OR "civic hacker")', '+publish_date:[2000-01-01T00:00:00Z TO 2014-05-12T00:00:00Z] AND (media_sets_id:1 OR media_sets_id:26 OR media_sets_id:7125 OR media_sets_id:16955)')
#print "found " + res['response']['numFound'] + " sentences"

story_ids = []
[story_ids.append(i) for i in [y["stories_id"] for y in res["response"]["docs"]] if not story_ids.count(i)]

stories = [mc.story(i) for i in story_ids]


for (i, story) in enumerate(stories):
  stories[i]["publisher"] = mc.media(stories[i]["media_id"])

#stories = mc.storyList('("civic hacking")', '+publish_date:[2000-01-01T00:00:00Z TO 2014-05-12T00:00:00Z] AND (media_sets_id:1 OR media_sets_id:26 OR media_sets_id:7125)',0,100)


print json.dumps(stories)

#civic_hacking_articles
#hackathon_stories
