print("""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++MOVIE RECOMMENDER SYSTEM++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
___________________________________________________________
1. It is a sytem which would filter out the movies according to the user preferences and past
data.

this system works on two methoda:
1. collaborative filtering : filters out the data according to the oast data of the users
they mostly seeked for.
2. content based filtering : filtering out the data which maches accordingly to the user prferences.
""")
#importing dataset________________________________________
#++++++++REPRESENTATION OF DATA+++++++++++
def main():
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    cn=['user_id','item_id','rating','timestamp']
    path='https://media.geeksforgeeks.org/wp-content/uploads/file.tsv'
    df=pd.read_csv(path,sep='\t',names=cn)

#checkout the head of the data
    print("viewing data++++++++++++++++++++++++++")
    print(df.head())
    print(df.tail())

    print(df)

#Movietitles(mt)__________________________
    mt=pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/Movie_Id_Titles.csv')
#acessing seperate movie title
    print(mt['title'].loc[mt.index[50]])
    print("merged frames++++++++++++++++++")      
    data = pd.merge(df, mt, on='item_id') 
    print(data.head())
#calculating mean
    print(data.groupby('title')['rating'].mean().sort_values(ascending=False).head())
    # Calculate count rating of all movies
    data.groupby('title')['rating'].count().sort_values(ascending=False).head()
    # creating dataframe with 'rating' count values 
    ratings = pd.DataFrame(data.groupby('title')['rating'].mean()) 

    ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count()) 

    print(ratings.head())
    sns.set_style('white') 
   
    # plot graph of 'num of ratings column' 
    plt.figure(figsize =(10, 4)) 

    ratings['num of ratings'].hist(bins = 70)
    plt.show()
    # plot graph of 'ratings' column 
    plt.figure(figsize =(10, 4)) 

    ratings['rating'].hist(bins = 70)
    plt.show()
    
    # Sorting values according to 
    # the 'num of rating column' 
    moviemat = data.pivot_table(index ='user_id', 
			columns ='title', values ='rating') 

    print(moviemat.head(40)) 

    ratings.sort_values('num of ratings', ascending = False).head(10) 
    # analysing correlation with similar movies 
    starwars_user_ratings = moviemat['Star Wars (1977)'] 
    liarliar_user_ratings = moviemat['Liar Liar (1997)'] 
    print(starwars_user_ratings.head(40)) 
    # analysing correlation with similar movies 
    similar_to_starwars = moviemat.corrwith(starwars_user_ratings) 
    similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings) 

    corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation'])  
    corr_starwars.dropna(inplace = True) 

    corr_starwars.head()
    # Similar movies like starwars 
    corr_starwars.sort_values('Correlation', ascending = False).head(10) 
    corr_starwars = corr_starwars.join(ratings['num of ratings']) 

    print(corr_starwars.head()) 

    print(corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head())
    # Similar movies as of liarliar 
    corr_liarliar = pd.DataFrame(similar_to_liarliar, columns =['Correlation']) 
    corr_liarliar.dropna(inplace = True) 

    corr_liarliar = corr_liarliar.join(ratings['num of ratings']) 
    print(corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False).head(10))



    


main()
