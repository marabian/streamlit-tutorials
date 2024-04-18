import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Sales Streamlit Dashboard")
st.markdown("Streamlit Dashboard Tutorial")


# store and use result of method whenever ran with same input
@st.cache_data
def load_data(file):
    data = pd.read_excel(file)
    # do light cleaning here
    return data


with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is None:
    st.stop()

df = load_data(uploaded_file)

# fmt: off
with st.expander("Data Preview"):
    st.dataframe(
        df,
        column_config={
            "Year": st.column_config.NumberColumn(format="%d")
        },
    )
# fmt: on

all_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


# Select Software sales for 2023
def plot_bottom_left():
    # Use the melt (wide to long) function from pandas to transform the DataFrame from wide to long format.
    sales_data = pd.melt(
        # Filter the original DataFrame for rows where the Year is 2023 and the business_unit is "Software".
        df[(df["Year"] == 2023) & (df["business_unit"] == "Software")],
        # Specify "Scenario" as the identifier variable to keep it as a separate column in the melted DataFrame.
        id_vars=["Scenario"],
        # Specify the list of columns that contain the data to be unpivoted (melted), in this case, the monthly sales data.
        value_vars=all_months,
        # Name of the new column in the melted DataFrame that will contain the variable names (here, the names of the months).
        var_name="month",
        # Name of the new column in the melted DataFrame that will contain the values from the melted columns (sales data).
        value_name="sales",
    )

    # Tells pandas to group the data by unique combinations of Scenario and month
    # After grouping, this aggregation instruction tells pandas to apply a summation operation to the sales column within each group.
    # It specifies the operation
    sales_data = sales_data.groupby(["Scenario", "month"]).agg({"sales": "sum"}).reset_index()

    st.dataframe(sales_data)
    st.line_chart(sales_data, x="month", y="sales")


plot_bottom_left()
