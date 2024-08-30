import wikipedia as wp
import wikipediaapi as wpa

SEARCH_LIMIT = 5
def search_wikipedia(search_string):
    user_agent = "Wikipedia-API for building knowledge base"
    wiki_api = wpa.Wikipedia(user_agent=user_agent)

    search_results = wp.search(search_string)
    print(search_results)

    if not search_results:
        return "No results found."

    results = []
    for result in search_results:
        if len(results) < SEARCH_LIMIT:
            page = wiki_api.page(result)
            print(page)
            if page.exists():
                results.append({"title" : page.title, "text" : page.summary})

    return results