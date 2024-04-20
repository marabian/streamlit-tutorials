# Streamlit Dashboard Tutorial

Basic *Streamlit* tutorial for building dashboards using *Pandas* and *Plotly* for data visualization.

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
