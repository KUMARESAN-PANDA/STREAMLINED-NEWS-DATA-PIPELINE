import streamlit as st
import requests

def app():
    st.title('Sports News')
    
    # Function to fetch business news from the News API
    def fetch_business_news(api_key, country='us'):
        url = 'https://newsapi.org/v2/top-headlines'
        params = {
            'country': country,
            'category': 'sports',
            'apiKey': api_key
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data.get('articles', [])
        else:
            st.error(f"Error fetching business news: {data.get('message', 'Unknown error')}")
            return []

    # API key for News API (replace 'your_api_key' with your actual API key)
    api_key = '19cb1b7415df4988877778789528fdda'

    # Fetch business news data
    business_articles = fetch_business_news(api_key)

    if business_articles:
        # Display business news headlines, images, and descriptions
        st.subheader('Top Sports News:')
        for article in business_articles:
            if article['urlToImage']:
                st.image(article['urlToImage'], caption=article['title'], use_column_width=True)
            st.write(f"**{article['title']}**")
            st.write(article['description'])
            st.write(f"Read more: [{article['source']['name']}]({article['url']})")
            st.write('---')
    else:
        st.warning('No business news articles found.')
