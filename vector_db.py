from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct


class QdrantStorage:
    def __init__(self, url="http://localhost:6333", collection="documents", dim=3072):
        self.client = QdrantClient(url=url)
        self.collection = collection
        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collection_name=self.collection,
                vector_config=VectorParams(
                    size=dim,
                    distance=Distance.COSINE
                )
            )
        
        

    def upsert(self, ids,vectors, payloads):
        points = [
            PointStruct(id=ids[i], vector=vectors[i], payload=payloads[i])
            for i in range(len(ids))
        ]
        self.client.upsert(
            collection_name=self.collection,
            points=points
        )

    def search(self, vector, top_k=5):
        result = self.client.search(
            collection_name=self.collection,
            query_vector=vector,
            limit=top_k
        )

        contexts = []
        sources = {}

        for res in result:
            payload = getattr(res, 'payload', {})
            text = payload.get('text', '')
            source = payload.get('source', 'unknown')

            if text:
                contexts.append(text)
                source.add(source)
                # if source not in sources:
                #     sources[source] = 0
                # sources[source] += 1
        return {"contexts": contexts, "sources": list(sources)}