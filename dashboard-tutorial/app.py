import random
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


#######################################
# PAGE SETUP
#######################################

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Sales Streamlit Dashboard")
st.markdown("Streamlit Dashboard Tutorial")


with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is None:
    st.info(" Upload a file through config", icon="ℹ️")
    st.stop()

#######################################
# DATA LOADING
#######################################


@st.cache_data
def load_data(file):
    print("Loading data...")
    data = pd.read_excel(file)
    return data


df = load_data(uploaded_file)
all_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# fmt: off
with st.expander("Data Preview"):
    st.dataframe(
        df,
        column_config={
            "Year": st.column_config.NumberColumn(format="%d")
        },
    )
# fmt: on


#######################################
# VISUALIZATION METHODS
#######################################


@st.cache_data
def plot_metric(label, value, prefix="", suffix="", show_graph=False, color_graph=""):
    fig = go.Figure()

    fig.add_trace(
        go.Indicator(
            value=value,
            gauge={"axis": {"visible": False}},
            number={
                "prefix": prefix,
                "suffix": suffix,
                "font.size": 28,
            },
            title={
                "text": label,
                "font": {"size": 24},
            },
        )
    )

    if show_graph:
        fig.add_trace(
            go.Scatter(
                y=random.sample(range(0, 101), 30),
                hoverinfo="skip",
                fill="tozeroy",
                fillcolor=color_graph,
                line={
                    "color": color_graph,
                },
            )
        )

    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)
    fig.update_layout(
        # paper_bgcolor="lightgrey",
        margin=dict(t=30, b=0),
        showlegend=False,
        plot_bgcolor="white",
        height=100,
    )

    st.plotly_chart(fig, use_container_width=True)


@st.cache_data
def plot_gauge(indicator_number, indicator_color, indicator_suffix, indicator_title, max_bound):
    fig = go.Figure(
        go.Indicator(
            value=indicator_number,
            mode="gauge+number",
            domain={"x": [0, 1], "y": [0, 1]},
            number={
                "suffix": indicator_suffix,
                "font.size": 26,
            },
            gauge={
                "axis": {"range": [0, max_bound], "tickwidth": 1},
                "bar": {"color": indicator_color},
            },
            title={
                "text": indicator_title,
                "font": {"size": 28},
            },
        )
    )
    fig.update_layout(
        # paper_bgcolor="lightgrey",
        height=200,
        margin=dict(l=10, r=10, t=50, b=10, pad=8),
    )
    st.plotly_chart(fig, use_container_width=True)


@st.cache_data
def plot_top_right():
    # Filter the DataFrame and unpivot it
    # fmt: off
    sales_data = df.loc[
        (df["Year"] == 2023) & (df["Account"] == "Sales"),
        ["Scenario", "business_unit"] + all_months
    ].melt(
        id_vars=["Scenario", "business_unit"],
        var_name="month",
        value_name="sales"
    )
    # fmt: on

    # Aggregate the sales data
    sales_data = sales_data.groupby(["Scenario", "business_unit"], as_index=False).sum()

    fig = px.bar(
        sales_data,
        x="business_unit",
        y="sales",
        color="Scenario",
        barmode="group",
        text_auto=".2s",
        title="Sales for Year 2023",
        height=400,
    )
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig, use_container_width=True)


# Plot a line chart of monthly budget vs forecast for 2023 sales in the software business unit
@st.cache_data
def plot_bottom_left():
    sales_data = df.loc[
        (df["Year"] == 2023) & (df["Account"] == "Sales") & (df["business_unit"] == "Software"),
        ["Scenario"] + all_months,
    ].melt(
        id_vars=["Scenario"],
        var_name="month",
        value_name="sales",
    )

    # display the dataframe - useful to see what we're plotting
    st.dataframe(sales_data)

    fig = px.line(
        sales_data,
        x="month",
        y="sales",
        color="Scenario",
        markers=True,
        text="sales",
        title="Monthly Budget vs Forecast 2023",
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)


@st.cache_data
def plot_bottom_right():
    # Preparing the columns with the absolute value transformation
    abs_columns = {month: abs(df[month]) for month in all_months}

    # Filter the DataFrame, apply the absolute values and unpivot it
    # fmt: off
    sales_data = df.loc[
        (df["Scenario"] == "Actuals") & (df["Account"] != "Sales"),
        ["Account", "Year"] + all_months
    ].assign(**abs_columns).melt(
        id_vars=["Account", "Year"],
        var_name="month",  # This appears to be a mistake in naming in your original code; it should be "month" ideally
        value_name="sales"
    )
    # fmt: on

    # Aggregate the sales data
    sales_data = sales_data.groupby(["Account", "Year"], as_index=False).sum()

    fig = px.bar(
        sales_data,
        x="Year",
        y="sales",
        color="Account",
        title="Actual Yearly Sales Per Account",
    )
    st.plotly_chart(fig, use_container_width=True)


#######################################
# STREAMLIT LAYOUT
#######################################

# first row div
top_left_column, top_right_column = st.columns((2, 1))
# second row div
bottom_left_column, bottom_right_column = st.columns(2)

# Streamlit allows one level of nesting for the columns
with top_left_column:
    column_1, column_2, column_3, column_4 = st.columns(4)

    with column_1:
        plot_metric(
            "Total Accounts Receivable",
            6621280,
            prefix="$",
            suffix="",
            show_graph=True,
            color_graph="rgba(0, 104, 201, 0.2)",
        )
        plot_gauge(1.86, "#0068C9", "%", "Current Ratio", 3)

    with column_2:
        plot_metric(
            "Total Accounts Payable",
            1630270,
            prefix="$",
            suffix="",
            show_graph=True,
            color_graph="rgba(255, 43, 43, 0.2)",
        )
        plot_gauge(10, "#FF8700", " days", "In Stock", 31)

    with column_3:
        plot_metric("Equity Ratio", 75.38, prefix="", suffix=" %", show_graph=False)
        plot_gauge(7, "#FF2B2B", " days", "Out Stock", 31)

    with column_4:
        plot_metric("Debt Equity", 1.10, prefix="", suffix=" %", show_graph=False)
        plot_gauge(28, "#29B09D", " days", "Delay", 31)

with top_right_column:
    plot_top_right()

with bottom_left_column:
    plot_bottom_left()

with bottom_right_column:
    plot_bottom_right()

# fmt: on
