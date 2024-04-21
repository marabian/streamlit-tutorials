# Streamlit Dashboard Tutorial

A [Streamlit](https://docs.streamlit.io/) dashboard tutorial using [Plotly](https://plotly.com/python/) for creating data visualizations. Includes code samples for creating useful charts, as well as [Pandas](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) dataframe transformations like `pandas.melt` (unpivot) for turning wide data into long data (useful for plotting). For SQL version of the methods below, [see here](https://github.com/andfanilo/social-media-tutorials/blob/master/20230816-stdashboard/streamlit_app.py). Also useful to learn about financial data analysis and the differences between **actuals**, **budgets**, and **forecasts**.

## Data

### Test Financial Data

Using a [test dataset](./data/financial_data_clean.xlsx) which data contains both actual monthly sales figures and forecasted sales predictions grouped under the same column but differentiated by labels (e.g. 'Actuals', 'Budget' and 'Forecast') in the 'Scenario' field for different business units/account  (e.g. Software).

### "Business Unit" Column

* ***Definition***: Specific division within a company focusing on particular products or services.

* ***Example***: "Software" could be the division dealing with software (including all of their accounts like R&D expenses, sales, marketing, payroll, consulting, etc).

### "Account" Column

* ***Definition***: Category for organizing financial transactions, either as revenues or expenses.

* ***Example***: "Sales" tracks revenue from business activities; "Cost of Goods Sold" tracks the expenses related to production.

### "Scenario" Column

* **Actuals**:
    * ***Definition***: Actuals represent the **concrete/actual** financial outcomes for both revenue and expenses for a specific time period, such as a month or year.

    * ***Use***: These figures are crucial for evaluating the real financial performance of the business. Positive values indicate income or revenue, while negative values represent costs or expenditures. Reflects the real revenue earned during the period. These figures are recorded after transactions occur and show what the company actually made.

    * ***Example***: For the "Sales" account of the "Software" business unit, actuals would show the actual sales revenue generated each month. This should usually be positive (unless returns/charge backs are counted as expense for sales account). For the R&D account, actuals would show the actual expenses incurred each month (should be negative number, pretty much always).

* **Budget**
    * ***Definition***: The budget outlines the planned financial outcomes for a specific period, such as a fiscal year. It includes both expected revenue (positive values) and anticipated expenses (negative values).

    * ***Use***:  Budget figures are instrumental for setting financial goals and resource planning. Positive values in the budget indicate targeted income, while negative values denote planned spending.

    * ***Example***:
        1. For the "Sales" account of the "Software" business unit, the budget details expected monthly sales revenue (based on historic data).
        2. For the "R&D" account, the budget specifies planned monthly expenses.

    * **Budget vs Actuals**: Comparing actuals to the budget is crucial for assessing how the company performs against its financial plans. Actuals represent the real financial outcomes—both earnings and expenditures—that have occurred, allowing the company to see where it is exceeding or not meeting its planned figures. This comparison helps identify effective strategies and areas needing adjustment.

* **Forecast:**
    * ***Definition***: A forecast in financial terms is an estimate of future financial outcomes for a company, both for revenue (positive values) and expenses (negative values), based on current data, trends, and projections. It’s usually updated regularly to reflect the most recent information.

    * ***Use***: Forecasts are crucial for ongoing financial management and strategic planning. They allow companies to adjust their strategies in response to changing market conditions, operational performance, and other external factors. Positive values in a forecast suggest expected income, while negative values indicate anticipated expenses.

    ***Example***:
    * For the "Sales" account of the "Software" business unit, the forecast might project expected sales revenue based on current market trends and past performance data.

    * For the "R&D" account, the forecast would estimate future spending needed to support ongoing and upcoming projects.

    * **Budget vs Forecast**: A **budget** is primarily a financial plan set for a specific period, typically a fiscal year, and is based on historical data, expected company performance, and strategic goals. It serves as a baseline against which actual financial performance is measured, focusing on managing expenses and generating revenue according to predefined targets. Unlike forecasts, which are updated regularly to reflect current market conditions and company performance, budgets are generally fixed once set and reflect the organization's financial aspirations and constraints at the beginning of the period. While budgets are more about setting financial limits and targets, forecasts are dynamic, adapting to real-time economic environments, market trends, and unexpected changes, providing an ongoing prediction of financial outcomes based on the most current data.

## Plots

### 1. Plotting Monthly Budget vs Forecast for 2023 Sales in Software Business Unit

* **Function Name**: [plot_bottom_left()](./app.py#L169)

* **Purpose**: The function plots a line chart to compare budgeted sales figures and forecasted sales data for the year 2023 in the Software business unit.

* **Code Description**
    1. **Data Filtering**: It selects rows from your dataset where the 'Year' is 2023, 'Account' is "Sales", and 'business_unit' is "Software". This focuses the analysis on the specific financial data relevant to the budget and forecast for software sales.
    2. **Data Transformation**: Using the *Pandas* [`melt()`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) (unpivot) function, it transforms the dataset from wide to long format, to make it suitable for plotting  Each row corresponds to a specific month and scenario. This setup is ideal for time-series comparison. The rows are ordered by month. Now we have 3 columns: "Scenario", "month", and "sales". With two different scenarios: "Budget" and "Forecast".
    3. **Plotting**: It then uses [Streamlit Plotly Widget](https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart) to plot these data points on a line chart, with months on the x-axis and sales figures on the y-axis, and different lines representing different scenarios (budget and forecast).

* **Use**: This visualization helps in directly comparing what was forecasted against what was budgeted for sales in the Software business unit for each month of 2023. It can help identify discrepancies between the two figures, which can be crucial for financial planning and decision-making.

* **Other use case(s)**: In projects analyzing daily scraped data (e.g., Google search results for specific keywords), a modified version of this function can visualize changes in search rankings, sentiment analysis, or other metrics over time. This can reveal trends or the impact of SEO strategies.
    * Identify upward or downward trends in search rankings and correlate these with SEO activities or external events (like Google algorithm updates).

    * Quickly pinpoint which SEO strategies are yielding positive results and which are not, allowing for agile adjustments to SEO tactics.

    * Detect seasonality and cyclic trends in keyword performance, which can guide content strategy.

## Pivot vs Melt

* **Pivot**
    * Used to **transform long-form data to wide-form**. It reshapes the data by pivoting the values of one column into multiple columns.

    * Useful when you have long-form data, such as data in a tidy format with rows for each observation.

    * In *Pandas*, The [pivot()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html) function's `index` parameter value should be the same as the `id_vars` value. The "columns" value should be passed as the name of the "variable" column.

* **Melt**
    * Used to transform wide-form data to long-form.

    * **Making data more accessible and easier to work with**:
        When data is in a wide format, it can be difficult to see all of the relationships between the different variables. Melting the data can make it easier to identify patterns and trends.

    * **Simplifying complex datasets:**
        Melting data can help to simplify complex datasets by making them more intuitive and analysis-ready.

    * **Preparing data for visualization:**
        Many data visualization tools require data to be in a long format. Melting data can make it easier to create charts and graphs.

    * In *Pandas*, the [melt()](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) function is used to **transform data from wide to long format**, which simplifies analysis and visualization. The function’s parameters include `id_vars`, which specifies the columns to retain (unchanged), while the `var_name` and `value_name` parameters define the names of the new variable and value columns created from the columns that are "melted" down.

## Libraries for Running SQL Over Pandas DataFrames

* The Ibis Project
* JupySQL
* SparkSQL
* DuckDB - in memory vectorized database that can run SQL queries over Pandas DataFrames
