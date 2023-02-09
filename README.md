
## Problem Statement

Recommended System
- To find the movie and books relevancy as reference for recommendation to user.


## Data Information

Get the data from : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset


## Demo

https://vaishnokmr-recommended-system-main-jocxtf.streamlit.app/



## Data Modeling
```
Data Collection: Collect data on movie preferences and ratings from a large number of users. This data can be obtained through surveys, social media, or movie-rating platforms.

Data Preprocessing: Clean and preprocess the data to remove any irrelevant or missing values and to ensure that the data is in a format that can be used for analysis.

Feature Engineering: Create features from the data that are relevant to movie recommendations, such as movie genre, director, actors, and user behavior.

Model Selection: Select an appropriate model for the recommendation system, such as collaborative filtering, content-based filtering, or a hybrid approach.

Model Training: Train the selected model using the data and features that have been created.

Model Fine-Tuning: Fine-tune the model by adjusting its parameters and features based on the results of the model evaluation.

Deployment: Deploy the fine-tuned model in the movie recommendation system and monitor its performance over time.

```

## Behind the Scene
For Movie Recommended uses content-based recommendation system uses features of the products, such as movie genre, director, and actors, to recommend similar items based on the similarity score. This approach is suitable for recommending products with well-defined features and attributes.
![alt text](https://github.com/Vaishnokmr/Recommended-System/blob/main/ContentBased.png)

As we can see that, There are various sport which is high similar score with each other rather than "3 Idiot" which movie content cause of low similar score to sports content. 

A collaborative-based recommendation system uses the behavior and preferences of similar users to recommend items. It calculates the similarity score between users based on their past interactions with the items and uses this score to make recommendations. This approach is suitable for recommending items in domains where user behavior and preferences are well-known, such as movie recommendations.
![alt text](https://github.com/Vaishnokmr/Recommended-System/blob/main/CollaborativeBased.png)

As we can see that, Person A likes Cricket with high similarity score and Person B likes as well. So based on Person A likes Football with similarity score their past interactions with the items and uses this score recommend to Person B.   

(*Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space. It is commonly used in recommendation systems to calculate the similarity score between two items or between a user and an item. The cosine similarity score ranges from -1 to 1, where 1 indicates that the vectors are identical, 0 indicates that they are orthogonal, and -1 indicates that they are completely dissimilar. This score is used to determine the relevance of the recommendations and to rank the items for a user. By using cosine similarity, recommendation systems can provide accurate and relevant recommendations to users based on their preferences.)
## Conclusion

- In conclusion, a recommendation system is a powerful tool that utilizes data science techniques to provide personalized recommendations to users based on their preferences. It can improve customer satisfaction, enhance the user experience, and drive growth and success for businesses. However, it is important to continuously monitor and maintain the system to ensure its effectiveness.

