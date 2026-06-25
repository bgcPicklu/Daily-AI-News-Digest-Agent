def generate_digest(articles):

    digest = ""

    for article in articles:

        digest += f"""

Title:
{article['title']}

Score:
{article['score']}

Summary:
{article['summary']}

Read More:
{article['url']}

-----------------------------------
"""

    return digest