## 1. The oldest businesses in the world
<p>This is Staffelter Hof Winery, Germany's oldest business, which was established in 862 under the Carolingian dynasty. It has continued to serve customers through dramatic changes in Europe such as the Holy Roman Empire, the Ottoman Empire, and both world wars. What characteristics enable a business to stand the test of time? Image credit: <a href="https://commons.wikimedia.org/wiki/File:MKn_Staffelter_Hof.jpg">Martin Kraft</a>
<img src="https://assets.datacamp.com/production/project_1383/./img/MKn_Staffelter_Hof.jpeg" alt="The entrance to Staffelter Hof Winery, a German winery established in 862." width="400"></p>
<p>To help answer this question, BusinessFinancing.co.uk <a href="https://businessfinancing.co.uk/the-oldest-company-in-almost-every-country">researched</a> the oldest company that is still in business in almost every country and compiled the results into a dataset. Let's explore this work to to better understand these historic businesses. Our datasets, which are all located in the <code>datasets</code> directory, contain the following information: </p>
<h3 id="businessesandnew_businesses"><code>businesses</code> and <code>new_businesses</code></h3>
<table>
<thead>
<tr>
<th style="text-align:left;">column</th>
<th>type</th>
<th>meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;"><code>business</code></td>
<td>varchar</td>
<td>Name of the business.</td>
</tr>
<tr>
<td style="text-align:left;"><code>year_founded</code></td>
<td>int</td>
<td>Year the business was founded.</td>
</tr>
<tr>
<td style="text-align:left;"><code>category_code</code></td>
<td>varchar</td>
<td>Code for the category of the business.</td>
</tr>
<tr>
<td style="text-align:left;"><code>country_code</code></td>
<td>char</td>
<td>ISO 3166-1 3-letter country code.</td>
</tr>
</tbody>
</table>
<h3 id="countries"><code>countries</code></h3>
<table>
<thead>
<tr>
<th style="text-align:left;">column</th>
<th>type</th>
<th>meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;"><code>country_code</code></td>
<td>varchar</td>
<td>ISO 3166-1 3-letter country code.</td>
</tr>
<tr>
<td style="text-align:left;"><code>country</code></td>
<td>varchar</td>
<td>Name of the country.</td>
</tr>
<tr>
<td style="text-align:left;"><code>continent</code></td>
<td>varchar</td>
<td>Name of the continent that the country exists in.</td>
</tr>
</tbody>
</table>
<h3 id="categories"><code>categories</code></h3>
<table>
<thead>
<tr>
<th style="text-align:left;">column</th>
<th>type</th>
<th>meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;"><code>category_code</code></td>
<td>varchar</td>
<td>Code for the category of the business.</td>
</tr>
<tr>
<td style="text-align:left;"><code>category</code></td>
<td>varchar</td>
<td>Description of the business category.</td>
</tr>
</tbody>
</table>
<p>Now let's learn about some of the world's oldest businesses still in operation!</p>


```python
# Import the pandas library under its usual alias 
import pandas as pd

# Load the business.csv file as a DataFrame called businesses
businesses = pd.read_csv('datasets/businesses.csv')

# Sort businesses from oldest businesses to youngest
sorted_businesses = businesses.sort_values('year_founded')

# Display the first few lines of sorted_businesses
sorted_businesses.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>business</th>
      <th>year_founded</th>
      <th>category_code</th>
      <th>country_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>64</th>
      <td>Kongō Gumi</td>
      <td>578</td>
      <td>CAT6</td>
      <td>JPN</td>
    </tr>
    <tr>
      <th>94</th>
      <td>St. Peter Stifts Kulinarium</td>
      <td>803</td>
      <td>CAT4</td>
      <td>AUT</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Staffelter Hof Winery</td>
      <td>862</td>
      <td>CAT9</td>
      <td>DEU</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Monnaie de Paris</td>
      <td>864</td>
      <td>CAT12</td>
      <td>FRA</td>
    </tr>
    <tr>
      <th>103</th>
      <td>The Royal Mint</td>
      <td>886</td>
      <td>CAT12</td>
      <td>GBR</td>
    </tr>
  </tbody>
</table>
</div>



## 2. The oldest businesses in North America
<p>So far we've learned that Kongō Gumi is the world's oldest continuously operating business, beating out the second oldest business by well over 100 years! It's a little hard to read the country codes, though. Wouldn't it be nice if we had a list of country names to go along with the country codes?</p>
<p>Enter <code>countries.csv</code>, which is also located in the <code>datasets</code> folder. Having useful information in different files is a common problem: for data storage, it's better to keep different types of data separate, but for analysis, we want all the data in one place. To solve this, we'll have to join the two tables together. </p>
<h3 id="countries"><code>countries</code></h3>
<table>
<thead>
<tr>
<th style="text-align:left;">column</th>
<th>type</th>
<th>meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;"><code>country_code</code></td>
<td>varchar</td>
<td>ISO 3166-1 3-letter country code.</td>
</tr>
<tr>
<td style="text-align:left;"><code>country</code></td>
<td>varchar</td>
<td>Name of the country.</td>
</tr>
<tr>
<td style="text-align:left;"><code>continent</code></td>
<td>varchar</td>
<td>Name of the continent that the country exists in.</td>
</tr>
</tbody>
</table>
<p>Since <code>countries.csv</code> contains a <code>continent</code> column, merging the datasets will also allow us to look at the oldest business on each continent! </p>


```python
# Load countries.csv to a DataFrame
countries = pd.read_csv("datasets/countries.csv")

# Merge sorted_businesses with countries
businesses_countries = pd.merge(sorted_businesses, countries, how='left', on='country_code')

# Filter businesses_countries to include countries in North America only
north_america = businesses_countries[businesses_countries['continent'] == 'North America']
north_america.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>business</th>
      <th>year_founded</th>
      <th>category_code</th>
      <th>country_code</th>
      <th>country</th>
      <th>continent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22</th>
      <td>La Casa de Moneda de México</td>
      <td>1534</td>
      <td>CAT12</td>
      <td>MEX</td>
      <td>Mexico</td>
      <td>North America</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Shirley Plantation</td>
      <td>1638</td>
      <td>CAT1</td>
      <td>USA</td>
      <td>United States</td>
      <td>North America</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Hudson's Bay Company</td>
      <td>1670</td>
      <td>CAT17</td>
      <td>CAN</td>
      <td>Canada</td>
      <td>North America</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Mount Gay Rum</td>
      <td>1703</td>
      <td>CAT9</td>
      <td>BRB</td>
      <td>Barbados</td>
      <td>North America</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Rose Hall</td>
      <td>1770</td>
      <td>CAT19</td>
      <td>JAM</td>
      <td>Jamaica</td>
      <td>North America</td>
    </tr>
  </tbody>
</table>
</div>



## 3. The oldest business on each continent
<p>Now we can see that the oldest company in North America is La Casa de Moneda de México, founded in 1534. Why stop there, though, when we could easily find out the oldest business on every continent? </p>


```python
# Create continent, which lists only the continent and oldest year_founded
continent = businesses_countries.groupby('continent')['year_founded'].agg([min])

# Merge continent with businesses_countries
merged_continent = pd.merge(continent, businesses_countries, how='left', left_on='min', right_on='year_founded')

# Subset continent so that only the four columns of interest are included
merged_continent.head()
subset_merged_continent = merged_continent[['continent', 'country', 'business', 'year_founded']]
subset_merged_continent
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>continent</th>
      <th>country</th>
      <th>business</th>
      <th>year_founded</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Africa</td>
      <td>Mauritius</td>
      <td>Mauritius Post</td>
      <td>1772</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Asia</td>
      <td>Japan</td>
      <td>Kongō Gumi</td>
      <td>578</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Europe</td>
      <td>Austria</td>
      <td>St. Peter Stifts Kulinarium</td>
      <td>803</td>
    </tr>
    <tr>
      <th>3</th>
      <td>North America</td>
      <td>Mexico</td>
      <td>La Casa de Moneda de México</td>
      <td>1534</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Oceania</td>
      <td>Australia</td>
      <td>Australia Post</td>
      <td>1809</td>
    </tr>
    <tr>
      <th>5</th>
      <td>South America</td>
      <td>Peru</td>
      <td>Casa Nacional de Moneda</td>
      <td>1565</td>
    </tr>
  </tbody>
</table>
</div>



## 4. Unknown oldest businesses
<p>BusinessFinancing.co.uk wasn't able to determine the oldest business for some countries, and those countries are simply left off of <code>businesses.csv</code> and, by extension, <code>businesses</code>. However, the <code>countries</code> that we created <em>does</em> include all countries in the world, regardless of whether the oldest business is known. </p>
<p>We can compare the two datasets in one DataFrame to find out which countries don't have a known oldest business! </p>


```python
# Use .merge() to create a DataFrame, all_countries
all_countries = businesses.merge(countries, on="country_code", how="right",  indicator=True)

# Filter to include only countries without oldest businesses
missing_countries = all_countries[all_countries["_merge"] != "both"]

# Create a series of the country names with missing oldest business data
missing_countries_series = missing_countries["country"]

# Display the series
missing_countries_series
```




    163                              Angola
    164                 Antigua and Barbuda
    165                             Bahamas
    166                  Dominican Republic
    167                             Ecuador
    168                                Fiji
    169     Micronesia, Federated States of
    170                               Ghana
    171                              Gambia
    172                             Grenada
    173           Iran, Islamic Republic of
    174                          Kyrgyzstan
    175                            Kiribati
    176               Saint Kitts and Nevis
    177                              Monaco
    178                Moldova, Republic of
    179                            Maldives
    180                    Marshall Islands
    181                               Nauru
    182                               Palau
    183                    Papua New Guinea
    184                            Paraguay
    185                 Palestine, State of
    186                     Solomon Islands
    187                            Suriname
    188                          Tajikistan
    189                        Turkmenistan
    190                         Timor-Leste
    191                               Tonga
    192                              Tuvalu
    193    Saint Vincent and the Grenadines
    194                               Samoa
    Name: country, dtype: object



## 5. Adding new oldest business data
<p>It looks like we've got some holes in our dataset! Fortunately, we've taken it upon ourselves to improve upon BusinessFinancing.co.uk's work and find oldest businesses in a few of the missing countries. We've stored the newfound oldest businesses in <code>new_businesses</code>, located at <code>"datasets/new_businesses.csv"</code>. It has the exact same structure as our <code>businesses</code> dataset. </p>
<h3 id="new_businesses"><code>new_businesses</code></h3>
<table>
<thead>
<tr>
<th style="text-align:left;">column</th>
<th>type</th>
<th>meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;"><code>business</code></td>
<td>varchar</td>
<td>Name of the business.</td>
</tr>
<tr>
<td style="text-align:left;"><code>year_founded</code></td>
<td>int</td>
<td>Year the business was founded.</td>
</tr>
<tr>
<td style="text-align:left;"><code>category_code</code></td>
<td>varchar</td>
<td>Code for the category of the business.</td>
</tr>
<tr>
<td style="text-align:left;"><code>country_code</code></td>
<td>char</td>
<td>ISO 3166-1 3-letter country code.</td>
</tr>
</tbody>
</table>
<p>All we have to do is combine the two so that we've got one more complete list of businesses!</p>


```python
# Import new_businesses.csv
new_businesses = pd.read_csv('datasets/new_businesses.csv')

# Add the data in new_businesses to the existing businesses
all_businesses = pd.concat([new_businesses, businesses])

# Merge and filter to find countries with missing business data
new_all_countries = pd.merge(all_businesses, countries, on='country_code', how = 'right', indicator=True)
new_missing_countries = new_all_countries[new_all_countries['_merge'] != 'both']

# Group by continent and create a "count_missing" column
count_missing = new_missing_countries.groupby('continent')['country'].agg(['count'])
count_missing.columns = ['count_missing']

count_missing
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count_missing</th>
    </tr>
    <tr>
      <th>continent</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Africa</th>
      <td>3</td>
    </tr>
    <tr>
      <th>Asia</th>
      <td>7</td>
    </tr>
    <tr>
      <th>Europe</th>
      <td>2</td>
    </tr>
    <tr>
      <th>North America</th>
      <td>5</td>
    </tr>
    <tr>
      <th>Oceania</th>
      <td>10</td>
    </tr>
    <tr>
      <th>South America</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



## 6. The oldest industries
<p>Remember our oldest business in the world, Kongō Gumi? </p>
<table>
<thead>
<tr>
<th style="text-align:right;"></th>
<th style="text-align:left;">business</th>
<th style="text-align:right;">year_founded</th>
<th style="text-align:left;">category_code</th>
<th style="text-align:left;">country_code</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:right;">64</td>
<td style="text-align:left;">Kongō Gumi</td>
<td style="text-align:right;">578</td>
<td style="text-align:left;">CAT6</td>
<td style="text-align:left;">JPN</td>
</tr>
</tbody>
</table>
<p>We know Kongō Gumi was founded in the year 578 in Japan, but it's a little hard to decipher which industry it's in. Information about what the <code>category_code</code> column refers to is in <code>"datasets/categories.csv"</code>: </p>
<h3 id="categories"><code>categories</code></h3>
<table>
<thead>
<tr>
<th style="text-align:left;">column</th>
<th>type</th>
<th>meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;"><code>category_code</code></td>
<td>varchar</td>
<td>Code for the category of the business.</td>
</tr>
<tr>
<td style="text-align:left;"><code>category</code></td>
<td>varchar</td>
<td>Description of the business category.</td>
</tr>
</tbody>
</table>
<p>Let's use <code>categories.csv</code> to understand how many oldest businesses are in each category of industry.</p>


```python
# Import categories.csv and merge to businesses
categories = pd.read_csv("datasets/categories.csv")
businesses_categories = businesses.merge(categories, on="category_code")

# Create a DataFrame which lists the number of oldest businesses in each category
count_business_cats = businesses_categories.groupby("category").agg({"business":"count"})

# Create a DataFrame which lists the cumulative years that businesses from each category have been operating
years_business_cats = businesses_categories.groupby("category").agg({"year_founded":"sum"})

# Rename columns and display the first five rows of both DataFrames
count_business_cats.columns = ["count"]
years_business_cats.columns = ["total_years_in_business"]
display(count_business_cats.head(), years_business_cats.head())
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
    </tr>
    <tr>
      <th>category</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Agriculture</th>
      <td>6</td>
    </tr>
    <tr>
      <th>Aviation &amp; Transport</th>
      <td>19</td>
    </tr>
    <tr>
      <th>Banking &amp; Finance</th>
      <td>37</td>
    </tr>
    <tr>
      <th>Cafés, Restaurants &amp; Bars</th>
      <td>6</td>
    </tr>
    <tr>
      <th>Conglomerate</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_years_in_business</th>
    </tr>
    <tr>
      <th>category</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Agriculture</th>
      <td>10669</td>
    </tr>
    <tr>
      <th>Aviation &amp; Transport</th>
      <td>36598</td>
    </tr>
    <tr>
      <th>Banking &amp; Finance</th>
      <td>70302</td>
    </tr>
    <tr>
      <th>Cafés, Restaurants &amp; Bars</th>
      <td>8532</td>
    </tr>
    <tr>
      <th>Conglomerate</th>
      <td>5671</td>
    </tr>
  </tbody>
</table>
</div>


## 7. Restaurant representation
<p>No matter how we measure it, looks like Banking and Finance is an excellent industry to be in if longevity is our goal! Let's zoom in on another industry: cafés, restaurants, and bars. Which restaurants in our dataset have been around since before the year 1800?</p>


```python
# Filter using .query() for CAT4 businesses founded before 1800; sort results
old_restaurants = businesses_categories.query('year_founded < 1800 and category_code == "CAT4"')

# Sort the DataFrame
old_restaurants = old_restaurants.sort_values("year_founded")
old_restaurants
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>business</th>
      <th>year_founded</th>
      <th>category_code</th>
      <th>country_code</th>
      <th>category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>142</th>
      <td>St. Peter Stifts Kulinarium</td>
      <td>803</td>
      <td>CAT4</td>
      <td>AUT</td>
      <td>Cafés, Restaurants &amp; Bars</td>
    </tr>
    <tr>
      <th>143</th>
      <td>Sean's Bar</td>
      <td>900</td>
      <td>CAT4</td>
      <td>IRL</td>
      <td>Cafés, Restaurants &amp; Bars</td>
    </tr>
    <tr>
      <th>139</th>
      <td>Ma Yu Ching's Bucket Chicken House</td>
      <td>1153</td>
      <td>CAT4</td>
      <td>CHN</td>
      <td>Cafés, Restaurants &amp; Bars</td>
    </tr>
  </tbody>
</table>
</div>



## 8. Categories and continents
<p>St. Peter Stifts Kulinarium is old enough that the restaurant is believed to have served Mozart - and it would have been over 900 years old even when he was a patron! Let's finish by looking at the oldest business in each category of commerce for each continent. </p>


```python
# Merge all businesses, countries, and categories together
businesses_categories_countries = businesses_categories.merge(countries, on="country_code")

# Sort businesses_categories_countries from oldest to most recent
businesses_categories_countries = businesses_categories_countries.sort_values("year_founded")

# Create the oldest by continent and category DataFrame
oldest_by_continent_category = businesses_categories_countries.groupby(["continent", "category"]).agg({"year_founded":"min"})
oldest_by_continent_category.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>year_founded</th>
    </tr>
    <tr>
      <th>continent</th>
      <th>category</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">Africa</th>
      <th>Agriculture</th>
      <td>1947</td>
    </tr>
    <tr>
      <th>Aviation &amp; Transport</th>
      <td>1854</td>
    </tr>
    <tr>
      <th>Banking &amp; Finance</th>
      <td>1892</td>
    </tr>
    <tr>
      <th>Distillers, Vintners, &amp; Breweries</th>
      <td>1933</td>
    </tr>
    <tr>
      <th>Energy</th>
      <td>1968</td>
    </tr>
  </tbody>
</table>
</div>


