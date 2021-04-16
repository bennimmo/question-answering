from sentence_transformers import SentenceTransformer


class SentenceTransformers:
    transformers = {}

    @staticmethod
    def get_transformer(name: str) -> SentenceTransformer:
        if name not in SentenceTransformers.transformers:
            SentenceTransformers.transformers[name] = SentenceTransformer(name)
        return SentenceTransformers.transformers[name]
