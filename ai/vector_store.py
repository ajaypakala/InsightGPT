import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


class VectorStore:

    def __init__(self):

        self.index = None

        self.documents = []


    def build(self, df):

        self.documents = [
            row.to_json()
            for _, row in df.iterrows()
        ]

        embeddings = model.encode(
            self.documents
        )

        embeddings = np.array(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            embeddings
        )


    def search(
        self,
        query,
        k=5
    ):

        query_embedding = model.encode(
            [query]
        )

        query_embedding = np.array(
            query_embedding,
            dtype="float32"
        )

        distances, indices = self.index.search(
            query_embedding,
            k
        )

        return [
            self.documents[i]
            for i in indices[0]
        ]