import wiki.wiki_search as wiki_search
import llm.llm_query as llm_query
import json

def test_wiki_search():
    data = wiki_search.search_wikipedia('To what extent has social media influencer marketing affected consumer interactions in the beauty industry to attract sales from TikTok users in the United States during April 2020 versus August 2021')
    assert(data!=None)

test_wiki_search()




