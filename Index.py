from PIL import Image
import streamlit as st




st.set_page_config(page_title="Newton's Law of Cooling: Explained!", page_icon="📊", layout="wide")
#newtonFormula = st.file_uploader("Images/Screenshot 2025-02-26 182724.png", type=["png"])


newtonFormulaImg = Image.open("CalcProjectWebsite/Images/Fromula.png")
slopeFeilds = Image.open("CalcProjectWebsite/Images/Fromula.png")
posEq = Image.open("CalcProjectWebsite/Images/Fromula.png")

# First centered title

col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.write("Unit 7 lesson 8 - Newton's Law")


with col2:
    st.title(":gray[Newton's Law of Cooling: Explained!]")

st.write("---")
st.write("")
st.write('')
# Second centered subheader (separate column instance)
col4, col5, col6 = st.columns([1,.1,1.4])
with col4:
    st.subheader(":blue[What is Newton's Law of Cooling?]")
    st.markdown("<p style='font-size:18px;'>Newton’s law of cooling describes the rate at which an exposed body changes temperature through radiation, "
             "which is approximately proportional to the difference between the object’s temperature and its surroundings, "
             "provided the difference is small.</p>", unsafe_allow_html=True)
    

    st.write("")
    st.write('Formula:')

    st.image(newtonFormulaImg, width=400)
#    st.image('C:\\Users\Anjan\Website\Images\Fromula.png', width=300)  # Adjust width as needed
#    if newtonFormula:
#        st.image(newtonFormula, caption="Newton's Cooling Formula", use_column_width=True)

    st.write(' Where T_a is the ambient temperature. By generating a slope field for this differential equation, we can see that a solution to the differential equation is a vertical shift of the exponential decay equation:')
    st.image(posEq, width=500)
    st.markdown("<p style='font-size:18px;'>  Here the proportionality constant k will be specific to each problem, depending on the object which is cooling. The coefficient A will be the initial difference in temperatures. </p>", unsafe_allow_html=True)
    
    st.subheader('[Desmos Slope Feilds Link!](https://www.desmos.com/calculator/5volnpwfua)')


with col6:
    st.components.v1.iframe("https://www.desmos.com/calculator/5volnpwfua", width=1000, height = 800)
#    st.image(slopeFeilds, width=800)



#end of intro for slope feilds

st.write("---")

a, b = st.columns([1,1])




with a:
    st.components.v1.iframe("https://www.desmos.com/calculator", width=800, height = 850)

with b:
    st.markdown("**<p style='font-size:55px; color:gold; text-align:center;'>Practice</p>**", unsafe_allow_html=True)
    st.markdown("<p style='font-size:25px;'>A cup of coffee is made with boiling water at a temperature of 100C in a room with ambient temperature 20C. After 4 minutes the coffee has cooled to 90C. </p>", unsafe_allow_html=True)

    st.write("")
    st.write('')

    st.markdown("<p style='font-size:25px;'> a. What is the equation T(t) for the temperature of the coffee? </p>", unsafe_allow_html=True)

    st.write("")
    st.write('')
    st.write("")
    st.write('')
    st.write("")
    st.write('')
    st.write("")
    st.write('')

    st.markdown("<p style='font-size:25px;'> b. What is the temperature of the coffee after 8 minutes? </p>", unsafe_allow_html=True)

    st.write("")
    st.write('')
    st.write("")
    st.write('')
    st.write("")
    st.write('')
    st.write("")
    st.write('')

    st.markdown("<p style='font-size:25px;'> c. Does the coffee cool more in the first 4 minutes or the second 4 minutes? Why does this make sense in terms of the differential equation? </p>", unsafe_allow_html=True)

st.write('---')

cola, colb, colc = st.columns([1,1,1])

with colb:
    st.subheader("Additional Resources + Homework")

with cola:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.subheader("[Youtube link to Newton's Law of Cooling](https://www.youtube.com/watch?v=xq-JiYMQydc)")

with colb:

    st.subheader("[Khan Academy Video](https://www.youtube.com/watch?v=IICR-w1jYcA)")

with colc:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.subheader("[Homework](https://docs.google.com/document/d/1ZjJSgRNnetPD_x8umJxtNLiHgVkFOsajygmgFX9d1XU/edit?usp=sharing)")
