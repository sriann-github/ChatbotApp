import pandas as pd
import pdb
import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy as np
import os

# Load data
print(os.path.abspath('Data Files/11-17-Incidents-dedupe/incidents_table.csv'))

# with open('Data Files/11-17-Incidents-dedupe/incidents_table.csv', 'r') as file:
    # print(file.read())
    
incidents_df = pd.read_csv('Data Files/11-17-Incidents-dedupe/incidents_table.csv', encoding='latin1')  # Or encoding='ISO-8859-1'
print(incidents_df.head(10))  # Displays the first 5 rows by default

#incidents_df = pd.read_csv('Data Files/11-17-Incidents-dedupe/incidents_table.csv')

# pdb.set_trace()

# Initialize BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Function to get BERT embeddings
def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    # Take the mean of the last hidden state
    embedding = torch.mean(outputs.last_hidden_state, dim=1).detach().numpy()
    return embedding

# Example: Data Cleaning - Duplicate Detection
def detect_duplicates(df, column_name, threshold=0.9):
    embeddings = np.stack(df[column_name].values)
    similarity_matrix = cosine_similarity(embeddings)
    duplicates = []
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            if similarity_matrix[i, j] > threshold:
                duplicates.append((i, j))
    return duplicates

# Example: Data Labeling using Clustering
def label_with_clustering(df, column_name, num_clusters=5):
    embeddings = np.stack(df[column_name].values)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42).fit(embeddings)
    df['cluster_label'] = kmeans.labels_
    return df

# Example: Data Augmentation - Nearest Neighbor Sampling
def augment_with_neighbors(df, column_name, num_neighbors=3):
    embeddings = np.stack(df[column_name].values)
    augmented_texts = []
    for idx, embedding in enumerate(embeddings):
        # Get neighbors
        similarity_scores = cosine_similarity([embedding], embeddings).flatten()
        neighbor_indices = np.argsort(similarity_scores)[-num_neighbors-1:-1]
        for neighbor_idx in neighbor_indices:
            if neighbor_idx != idx:  # Exclude self
                augmented_texts.append(df.iloc[neighbor_idx]['Incident_Description'])
    df['augmented_texts'] = augmented_texts
    return df

def main():
    print('main')
    # Generate embeddings for Incident_Description
    incidents_df['description_embedding'] = incidents_df['Incident_Description'].apply(lambda x: get_bert_embedding(x).flatten())
    
    duplicates = detect_duplicates(incidents_df, 'description_embedding')
    incidents_df = label_with_clustering(incidents_df, 'description_embedding')
    incidents_df = augment_with_neighbors(incidents_df, 'description_embedding')
    print("BERT-based text processing completed.")

    
if __name__ == "__main__":
    main()