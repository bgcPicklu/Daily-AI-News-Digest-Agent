from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def remove_duplicates(news):

    unique = []
    embeddings = []

    for article in news:

        embedding = model.encode(
            article["title"]
        )

        duplicate = False

        for existing in embeddings:

            score = cosine_similarity(
                [embedding],
                [existing]
            )[0][0]

            if score > 0.90:
                duplicate = True
                break

        if not duplicate:

            unique.append(article)
            embeddings.append(embedding)

    return unique