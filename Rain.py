import pickle
import streamlit as st
import streamlit.components.v1 as components

import webbrowser

# loading the trained model
pickle_in = open('rf1.pkl', 'rb')
classifier = pickle.load(pickle_in)
#url = '/html/after_rainy.html'
#url1='/html/after_sunny.html'
link = '/html/after_rainy.html'



@st.cache()
# defining the function which will make the prediction using the data which the user inputs
def prediction(location , minTemp , maxTemp , rainfall , evaporation , sunshine ,
					 windGustDir , windGustSpeed , winddDir9am , winddDir3pm , windSpeed9am , windSpeed3pm ,
					 humidity9am , humidity3pm , pressure9am , pressure3pm , cloud9am , cloud3pm , temp9am , temp3pm ,
					 rainToday , month , day):
    # Making predictions
    prediction = classifier.predict(
        [[location , minTemp , maxTemp , rainfall , evaporation , sunshine ,
					 windGustDir , windGustSpeed , winddDir9am , winddDir3pm , windSpeed9am , windSpeed3pm ,
					 humidity9am , humidity3pm , pressure9am , pressure3pm , cloud9am , cloud3pm , temp9am , temp3pm ,
					 rainToday , month , day]])

    if prediction == 0:

        pred = 'after_sunny'

    else:
        #st.markdown(link, unsafe_allow_html=True)
        pred = 'after_rainy'
    return pred


# this is the main function in which we define our webpage
def main():


    st.sidebar.header("WELCOME TO RAIN PREDICTION")
    st.sidebar.markdown("This app is going to predict what will be the weather condition depending the")
    st.sidebar.markdown("values you are going to enter. It will predict wheather there will be any chance")
    st.sidebar.markdown("of ** Rain ** or not")
    foot = """ 
        <div style =padding:13px"> 
        <p>Developed with ❤ by <a style='display: block margin-top: 492px;' href="#" target="_blank">Nijithkamal</a></p> 
        </div> 
        """
    # display the front end aspect
    st.sidebar.markdown(foot, unsafe_allow_html=True)

    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:#1589FF;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Streamlit Rain Forecasting ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    with st.form(key='my_form'):

        col1,col2=st.beta_columns([3,3])

        with col1:

            location=st.selectbox("Location",["","Adelaide","Portland","Walpole","Cairns","Dartmoor","NorfolkIsland","MountGambier","Albany","Witchcliffe","CoffsHarbour","MountGinini","NorahHead",
                                              "Darwin","Sydney","SydneyAirport","Ballarat","GoldCoast","Watsonia","Newcastle","Hobart","Wollongong","Williamtown","Launceston",
                                              "Brisbane","MelbourneAirport","Sale","Albury","Perth","Melbourne","Nuriootpa","Penrith","BadgerysCreek","PerthAirport","Tuggeranong","Richmond","Bendigo",
                                              "Canberra","WaggaWagga","Townsville","Katherine","PearceRAAF","SalmonGums","Nhil","Moree","Cobar","Mildura","AliceSprings","Uluru","Woomera"])
            maxTemp = float(st.number_input("Maxium Temp"))
            evaporation=float(st.number_input("Evaporation"))
            windGustDir = st.selectbox("Select Wind Gust Direction",
                                       ["", "N", "W", "S", "E", "NE", "NW", "SW", "SE", "NNW", "NNE", "SSW", "SSE",
                                        "WNW", "WSW", "ENE", "ESE"])
            winddDir9am = st.selectbox("select wind Dir at 9 AM",
                                       ["", "N", "W", "S", "E", "NE", "NW", "SW", "SE", "NNW", "NNE", "SSW", "SSE",
                                        "WNW", "WSW", "ENE", "ESE"])
            windSpeed9am = float(st.number_input("WindSpeed9am"))
            humidity9am = float(st.number_input("humidity9am"))
            pressure9am=float(st.number_input("pressure9am"))
            cloud9am = float(st.number_input("cloud9am"))
            temp9am = float(st.number_input("temp9am"))
            rainToday = st.selectbox("Did it rain Today", ["", "Yes", "No"])
            day = st.number_input("Day")


        with col2:

            minTemp = float(st.number_input("Minimum Temp"))
            rainfall = float(st.number_input("Amount of Rainfall"))
            sunshine = float(st.number_input("Sunshine"))
            windGustSpeed = float(st.number_input("WindGustSpeed"))
            winddDir3pm = st.selectbox("Select Wind Dir at 3 PM",
                                       ["", "N", "W", "S", "E", "NE", "NW", "SW", "SE", "NNW", "NNE", "SSW", "SSE",
                                        "WNW", "WSW", "ENE", "ESE"])
            windSpeed3pm = float(st.number_input("windSpeed3pm"))
            humidity3pm=float(st.number_input("humidity3pm"))
            pressure3pm = float(st.number_input("pressure3pm"))
            cloud3pm = float(st.number_input("cloud3pm"))
            temp3pm = float(st.number_input("temp3pm"))
            month = st.number_input("Month")


        submit_button=st.form_submit_button(label='Predict')

    if submit_button:

        loc = {'Portland':1, 'Cairns':2, 'Walpole':3, 'Dartmoor':4, 'MountGambier':5,
       'NorfolkIsland':6, 'Albany':7, 'Witchcliffe':8, 'CoffsHarbour':9, 'Sydney':10,
       'Darwin':11, 'MountGinini':12, 'NorahHead':13, 'Ballarat':14, 'GoldCoast':15,
       'SydneyAirport':16, 'Hobart':17, 'Watsonia':18, 'Newcastle':19, 'Wollongong':20,
       'Brisbane':21, 'Williamtown':22, 'Launceston':23, 'Adelaide':24, 'MelbourneAirport':25,
       'Perth':26, 'Sale':27, 'Melbourne':28, 'Canberra':29, 'Albury':30, 'Penrith':31,
       'Nuriootpa':32, 'BadgerysCreek':33, 'Tuggeranong':34, 'PerthAirport':35, 'Bendigo':36,
       'Richmond':37, 'WaggaWagga':38, 'Townsville':39, 'PearceRAAF':40, 'SalmonGums':41,
       'Moree':42, 'Cobar':43, 'Mildura':44, 'Katherine':45, 'AliceSprings':46, 'Nhil':47,
       'Woomera':48, 'Uluru':49}
        if location:
            location = loc[location]
            print(location)

        windgustdir = {'NNW': 0, 'NW': 1, 'WNW': 2, 'N': 3, 'W': 4, 'WSW': 5, 'NNE': 6, 'S': 7, 'SSW': 8, 'SW': 9,
                       'SSE': 10,'NE': 11, 'SE': 12, 'ESE': 13, 'ENE': 14, 'E': 15}
        if windGustDir:
            windGustDir = windgustdir[windGustDir]
            print(windGustDir)

        winddir9am = {'NNW': 0, 'N': 1, 'NW': 2, 'NNE': 3, 'WNW': 4, 'W': 5, 'WSW': 6, 'SW': 7, 'SSW': 8, 'NE': 9,
                      'S': 10,'SSE': 11, 'ENE': 12, 'SE': 13, 'ESE': 14, 'E': 15}
        if winddDir9am:
            winddDir9am = winddir9am[winddDir9am]
            print(winddDir9am)

        winddir3pm = {'NW': 0, 'NNW': 1, 'N': 2, 'WNW': 3, 'W': 4, 'NNE': 5, 'WSW': 6, 'SSW': 7, 'S': 8, 'SW': 9,
                      'SE': 10,'NE': 11, 'SSE': 12, 'ENE': 13, 'E': 14, 'ESE': 15}
        if winddDir3pm:
            winddDir3pm = winddir3pm[winddDir3pm]
            print(winddDir3pm)

        rn = {'Yes': 1, 'No': 0}
        if rainToday:
            rainToday = rn[rainToday]
            print(rainToday)

        result = prediction(location , minTemp , maxTemp , rainfall , evaporation , sunshine ,
					 windGustDir , windGustSpeed , winddDir9am , winddDir3pm , windSpeed9am , windSpeed3pm ,
					 humidity9am , humidity3pm , pressure9am , pressure3pm , cloud9am , cloud3pm , temp9am , temp3pm ,
					 rainToday , month , day)

        #st.success('Weather Status : {}'.format(result))

        if result ==1:
            task=st.markdown("Tomorrow is going to be *** RAINY DAY ***")
            st.markdown("So enjoy yourselves with a hot cup of tea")
            HtmlFile = open("html/rainy.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read()
            print(source_code)
            components.html(source_code,height=600)
        else:
            task = st.markdown("Tomorrow is going to be *** SUNNY DAY ***")
            st.markdown(" So enjoy yourselves with something cool")

            HtmlFile = open("html/sunny.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read()
            print(source_code)
            components.html(source_code, height=600)

if __name__ == '__main__':
    main()