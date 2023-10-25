import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('intfloat/multilingual-e5-large')
model = model.to("cuda")

def create_dataframe():
    df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/data/index.csv')

    return df

def npy_file_load():
    # raw_content_vector = np.load("data/raw_content_vector.npy", allow_pickle=True)

    # raw_content_vector = raw_content_vector.astype(np.float32)

    refine_content_vector = np.load("data/refine_content_vector.npy", allow_pickle=True)

    refine_content_vector = refine_content_vector.astype(np.float32)

    return raw_content_vector, refine_content_vector

# Dims Check
# print(refine_content_vector.shape)
# print(raw_content_vector.shape)

# Type Check
# print(refine_content_vector.dtype)

def set_vector_index(raw_content_vector, refine_content_vector):
    # raw_index = faiss.IndexFlatL2(1024)
    # raw_index.add(raw_content_vector)

    refine_index = faiss.IndexFlatL2(1024)
    refine_index.add(refine_content_vector)

    return raw_index, refine_index

def question_embedding(query):
    query_vector = model.encode(query)
    query_vector = np.array(query_vector).astype(np.float32)

    return query_vector

def vector_search(query_vector):

    query_vector = np.array(query_vector).astype(np.float32)

    distances, indices = refine_index.search(query_vector, 5)

    return distances, indices


def view_search_result(df, distances, indices):
    temp = df.iloc[indices[0]]

    temp['distances'] = distances[0]

    temp[['raw_title','raw_content','distances']].head(10)


if __name__ == '__main__':
    df = create_dataframe()

    raw_content_vector, refine_content_vector = npy_file_load()

    raw_index, refine_index = set_vector_index(raw_content_vector, refine_content_vector)

    query_vector = question_embedding(query='')

    distances, indices = vector_search(query_vector)

    view_search_result(df, distances, indices)
