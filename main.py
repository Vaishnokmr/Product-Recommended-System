import streamlit as st
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_content(movie):
    movie_index = movies[movies['title']== movie].index[0]
    dist = similar[movie_index]
    movie_list = sorted(list(enumerate(dist)),reverse=True, key=lambda x:x[1])[1:6]
    movie_name = []
    for i in movie_list:
        movie_name.append(movies.iloc[i[0]].title)
    return movie_name
movie_dict = pickle.load(open('content_recommend/movie.pkl','rb'))
# similar = pickle.load(open('similar.pkl','rb'))
movies = pd.DataFrame(movie_dict)
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similar = cosine_similarity(vectors)

def recommend(book_name):
    index = np.where(pivot_final.index == book_name)[0][0]
    similar_item = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
    data = []
    for i in similar_item:
        temp_df =  book_dict[book_dict['Book-Title'] == pivot_final.index[i[0]]]
        item = []
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    return data
book_dict = pickle.load(open(r'collaborative_recommend/books.pkl','rb'))
similarity_scores = pickle.load(open(r'collaborative_recommend/similarity_scores.pkl','rb'))
pivot_final = pickle.load(open(r'collaborative_recommend/books_data.pkl','rb'))

st.title('Movie Recommend')
option = st.selectbox('How would yould like to ', movies['title'].values)
if st.button('Recommended Movies'):
    recommendations = recommend_content(option)
    for i in recommendations:
        st.write(i)


st.title('Book Recommend')
option = st.selectbox('How would yould like to ', pivot_final.index.values)
if st.button('Recommended Books'):
    recommendation = recommend(option)
    counter = 1
    for j in recommendation:
        st.write(counter)
        st.image((j[2]), width = 100)
        st.write('Book name :',j[0])
        st.write('Author name :',j[1])
        counter = counter + 1
