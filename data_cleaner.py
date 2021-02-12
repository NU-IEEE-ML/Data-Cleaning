import pandas as pd
import numpy as np
import re

def clean_data_v1(path):

       df = pd.read_csv(path)
       # print(df.columns)
       # print(df.shape)

       #Compute average review values on 10point scale
       df['average_review'] = df[[ 'review_scores_accuracy',
              'review_scores_cleanliness','review_scores_checkin',
              'review_scores_communication', 'review_scores_location','review_scores_value']].mean(axis = 1)
       #Since this is on a 100 scale, we convert it to be on a 10 points scale
       df['review_scores_rating'] = df['review_scores_rating']/10
       df['average_review'] = df[['average_review','review_scores_rating']].mean(axis = 1)

       #Right now we simply take the number of amenities
       df['amenities'] = len(df['amenities'].array)

       #Extract the number of bathrooms from the string
       df['bathrooms'] = df['bathrooms_text'].str.extract(r'([0-9]{1}.?[0-9]?)')
       df['bathrooms'] = pd.to_numeric(df['bathrooms'])

       #Drop columns that we don't currently use
       df = df.drop(columns = ['review_scores_accuracy',
              'review_scores_cleanliness','review_scores_checkin',
              'review_scores_communication', 'review_scores_location','review_scores_value','listing_url', 'scrape_id', 'last_scraped', 'name', 'description',
              'neighborhood_overview', 'picture_url', 'host_id', 'host_url',
              'host_name','host_thumbnail_url', 'host_picture_url',
              'host_neighbourhood', 'neighbourhood_group_cleansed','property_type', 'room_type','minimum_minimum_nights',
              'maximum_minimum_nights', 'minimum_maximum_nights',
              'maximum_maximum_nights', 'minimum_nights_avg_ntm',
              'maximum_nights_avg_ntm', 'calendar_updated', 'has_availability',
              'availability_30', 'availability_60', 'availability_90',
              'availability_365', 'calendar_last_scraped','license', 'instant_bookable',
              'calculated_host_listings_count',
              'calculated_host_listings_count_entire_homes',
              'calculated_host_listings_count_private_rooms',
              'calculated_host_listings_count_shared_rooms','calendar_last_scraped','number_of_reviews_l30d', 'first_review',
              'last_review','host_since', 'host_location', 'host_about', 'host_response_time',
              'host_response_rate', 'host_acceptance_rate','host_verifications', 'host_has_profile_pic', 'host_identity_verified',
              'neighbourhood', 'neighbourhood_cleansed', 'latitude', 'longitude','number_of_reviews_ltm', 'review_scores_rating',
              'reviews_per_month','bathrooms_text'], axis = 1)

       print(df.dtypes)
       cleaned_data = df.to_csv('cleaned_data.csv',index = False)

clean_data_v1('chicago_listings_full.csv')
