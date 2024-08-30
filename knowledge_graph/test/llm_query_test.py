import llm.llm_query as llm_query
import json


def test_llm_query():
    data = [{'id': 'Social media in the fashion industry', 'text': 'Social media in the fashion industry refers to the use of social media platforms by fashion designers and users to promote and participate in trends. Over the past several decades, the development of social media has increased along with its usage by consumers. The COVID-19 pandemic was a sharp turn of reliance on the virtual sphere for the industry and consumers alike. Social media has created new channels of advertising for fashion houses to reach their target markets. Since its surge in 2009, luxury fashion brands have used social media to build interactions between the brand and its customers to increase awareness and engagement. The emergence of influencers on social media has created a new way of advertising and maintaining customer relationships in the fashion industry. Numerous social media platforms are used to promote fashion trends, with Instagram and TikTok being the most popular among Generation Y and Z. The overall impact of social media in the fashion industry included the creation of online communities, direct communication between industry leaders and consumers, and criticized ideals that are promoted by the industry through social media.'}]
    json_strs = llm_query.get_results_open_ai(data)
    assert(json.loads(json_strs[0])!=None)


test_llm_query()
