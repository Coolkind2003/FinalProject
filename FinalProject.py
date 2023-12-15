









st.title('Final Project ')






# Function to read data from a CSV file
# function called at least twice
def read_data():

    return pd.read_csv("/Users/rominbakhtiyor/PycharmProjects/Final Project/Parking_Meters.csv")

df=read_data()

# Number 1 )

top_5_max_prices = df.nlargest(5, 'BASE_RATE')
print(top_5_max_prices[['STREET', 'BASE_RATE']])

st.subheader('5 Most Expensive Parking Spots in Boston Based on Base Rate ')
#bar graph
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(top_5_max_prices['STREET'], top_5_max_prices['BASE_RATE'], color='skyblue')
ax.set_xlabel('Street')
ax.set_ylabel('Base Rate')
ax.set_title('Top 5 Highest Base Rates')
st.pyplot(fig)


#MAP OF IT
#
#do hovering
def longitude_and_latitude():
    st.header("Map of Parking Spots Near Boston")
    df = read_data()
    columns = ["STREET", "BASE_RATE", "LATITUDE", "LONGITUDE"]
    dfLatAndLong = df.loc[:, columns]
    dfLatAndLong = dfLatAndLong.dropna(subset=columns)

    view_parking = pdk.ViewState(
        latitude=dfLatAndLong["LATITUDE"].mean(),
        longitude=dfLatAndLong["LONGITUDE"].mean(),
        zoom=11,
        pitch=0
    )

    layer1 = pdk.Layer(
        'ScatterplotLayer',
        data=dfLatAndLong,
        get_position='[LONGITUDE, LATITUDE]',
        get_radius=75,
        get_color=[255, 0, 0],
        pickable=True
    )

    tool_tip = {
        "html": "STREET<br/> <b>{STREET}</b><br/>"
                "BASE_RATE<br/> <b>{BASE_RATE}</b><br/>",
        "style": {"backgroundColor": "steelblue", "color": "white"}
    }

    map = pdk.Deck(
        map_style='mapbox://styles/mapbox/outdoors-v11',
        initial_view_state=view_parking,

        layers=[layer1],
          # Replace with your Mapbox access token
    )
    st.pydeck_chart(map)
longitude_and_latitude()


# a question



# Displaying images
image_path = '/Users/rominbakhtiyor/PycharmProjects/Final Project/Broadway.png'
image = Image.open(image_path)
size = (200, 200)

# Resize the image
new_image = image.resize(size)

# Display the image in Streamlit
st.image(new_image, caption='The Most Expensive Place to Park in Boston.')

st.write("114 Borad St C-M with a Base Rate of 2.00")

#42.3551° N, 71.0657° W Boston Common
# bar graph
# picute of Broad st C_m and why it's so expesensive



# AVERAGE RATE OF IT


st.subheader('Average Base Rate in All of Boston  ')
mean=df['BASE_RATE'].mean()
st.write(f"Average Base Rate: {mean:.2f}")

#42.3551 #-71.0657 #BOSTON COMMON
# 2) NEAREST PARKING SPOTS IN BOSTON COMMON


# A Question here
genre = st.radio(
        "Do you like Boston Common",
        ('Yes', 'No')
    )
if genre == 'Yes':
        st.write('Everyone Loves Boston Common.')
else:
        st.write("Please leave Boston.")



# 3) PArking Spot near Bentley
#42.3855 #-71.2218 #
#sort and filter
def place2():
    st.subheader("Nearest Parking Spots in Boston to Bentley")

    # 42.3855° N, 71.2218° W
    latlist = df['LATITUDE'].tolist()
    longlist = df['LONGITUDE'].tolist()
    cool = []
    for i in range(len(latlist)):
        # Calculate Euclidean distance
        cal = math.sqrt((42.3855 - latlist[i]) ** 2 + (-71.2218 - longlist[i]) ** 2)
        cool.append(cal)
    df['BCD'] = cool
    st.dataframe(df)
    # Sort the DataFrame by the calculated distance
    sorted_df = df.sort_values('BCD')

    # Select the top 5 unique nearest spots
    nearest_spots = sorted_df.drop_duplicates(subset=['STREET', 'VENDOR']).head(5)

    fig, ax = plt.subplots(figsize=(10, 6))


    ax.scatter(nearest_spots['LONGITUDE'], nearest_spots['LATITUDE'], color='green')


    for i, row in nearest_spots.iterrows():
        ax.text(row['LONGITUDE'], row['LATITUDE'], row['STREET'], fontsize=9)

    # Set labels and title
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Nearest Parking Spots in Boston to Bentley')

    # Display the scatter plot in Streamlit
    st.pyplot(fig)

    # Display the top 5 nearest spots in a table
    st.table(nearest_spots[['STREET', 'VENDOR', 'BASE_RATE']])

def place3():
    st.subheader("Nearest Parking Spots in Boston to Boston Common")

    # 42.3855° N, 71.2218° W
    latlist = df['LATITUDE'].tolist()
    longlist = df['LONGITUDE'].tolist()
    cool = []
    for i in range(len(latlist)):
        # Calculate Euclidean distance
        cal = math.sqrt((42.3551 - latlist[i]) ** 2 + (-71.0657 - longlist[i]) ** 2)
        cool.append(cal)
    df['BCD'] = cool
    st.dataframe(df)
    # Sort the DataFrame by the calculated distance
    sorted_df = df.sort_values('BCD')

    # Select the top 5 unique nearest spots
    nearest_spots = sorted_df.drop_duplicates(subset=['STREET', 'VENDOR']).head(5)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Scatter plot of parking spots
    ax.scatter(nearest_spots['LONGITUDE'], nearest_spots['LATITUDE'], color='green')

    # Label each point with the street name
    for i, row in nearest_spots.iterrows():
        ax.text(row['LONGITUDE'], row['LATITUDE'], row['STREET'], fontsize=9)

    # Set labels and title
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Nearest Parking Spots in Boston to Boston Common')

    # Display the scatter plot in Streamlit
    st.pyplot(fig)

    # Display the top 5 nearest spots in a table
    st.table(nearest_spots[['STREET', 'VENDOR', 'BASE_RATE']])


def place4():
    st.subheader("Nearest Parking Spots in Boston to Harvard Square")

    # 42.3855° N, 71.2218° W
    latlist = df['LATITUDE'].tolist()
    longlist = df['LONGITUDE'].tolist()
    cool = []
    #list comprehention
    cool =  [math.sqrt((42.3735 - latlist[i]) ** 2 + (-71.1189 - longlist[i]) ** 2) for i in range(len(latlist))]
    df['BCD'] = cool
    st.dataframe(df)
    # Sort the DataFrame by the calculated distance
    sorted_df = df.sort_values('BCD')

    # Select the top 5 unique nearest spots
    nearest_spots = sorted_df.drop_duplicates(subset=['STREET', 'VENDOR']).head(5)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Scatter plot of parking spots
    ax.scatter(nearest_spots['LONGITUDE'], nearest_spots['LATITUDE'], color='green')

    # Label each point with the street name
    for i, row in nearest_spots.iterrows():
        ax.text(row['LONGITUDE'], row['LATITUDE'], row['STREET'], fontsize=9)


    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Nearest Parking Spots in Boston to Harvard Square')


    st.pyplot(fig)


    st.table(nearest_spots[['STREET', 'VENDOR', 'BASE_RATE']])


location = st.selectbox(
    "Choose a location:",
    ("Bentley","Boston Common", "Harvard Square", )
)

if location == "Bentley":
    place2()
elif location == "Boston Common":
    place3()
elif location == "Harvard Square":
    place4()

#42.3524 #-71.0718

#Pie chart #fix
def create_pie_chart_for_streets():

      top_5_streets = df['STREET'].value_counts().nlargest(5)


      labels = top_5_streets.index
      sizes = top_5_streets.values

      # Create pie chart
      fig, ax = plt.subplots()
      ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
      ax.axis('equal')
      plt.title('Top 5 Streets with Most Parking Meters')

      # Display the pie chart in Streamlit
      st.pyplot(fig)


create_pie_chart_for_streets()

st.markdown("**This doesn't show all the streets but just the top five and the most amount among the top 5.**")

genre = st.button("Thank you")


