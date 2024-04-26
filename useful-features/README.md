# Useful Streamlit Features

## Table of Contents

1. Multiple chat input widgets - `st.chat_input()`

2. Streaming widget for consuming tokens in intervals - `st.write_stream()`
3. Subtitles for `st.video` widget
4. Popover widget, useful for dialog windows - `st.popover()`
5. Hiding border in form!
6. Dialog function decorator (Coming Soon)
7. Partial reruns - `st.fragment()` decorator, useful to rerun parts of your app, like plots.
8. Displaying certain pages to authenticated users - `--client.showSidebarNavigation false` flag and `st.page_link` widget
9. Can browse to new page yourself using `st.switch_page` method (hide the navbar firsts, then add buttons in the UI to navigate to different pages).
10. Catch query parameter from URL as dictionary, useful to initialize settings - `st.query_params`. Can also set query params in the URL using `st.set_query_params` to copy/send to colleagues.
11. Height parameter for `st.container()` to fix the height of the container - `st.container(height=200)`
12. Dataframe and data editor have updated the tool bar for easier searching and data downloading
13. Unit tests for your app, simulates user input workflows - [App Testing](https://docs.streamlit.io/develop/api-reference/app-testing)
14. Connect to various data sources - `st.connection` and [this guide](https://docs.streamlit.io/develop/api-reference/connections/st.connection)
15. New data editor that allows user to edit dataframe which saves to app - `st.data_editor`
16. New toggle method as an alternative to checkbox - `st.toggle`
17. Send a toast to your user, useful for notifications - `st.toast`
18. Send status of a long running process to the user - `st.status`
19. Link button method that draws attention and redirects to external web page - `st.link_button`
20. Line chart, bar chart, scatter chart, etc accepts a "color" keyword argument
21. Scatter chart, useful high level method to quickly build a scatter plot - `st.scatter_chart`
22. Improved map chart, can now customize the columns for latitude and longitude and use improved scatter plotting features - `st.map`
23. Can now add color to markdown text/titles/headers/most widget labels by prefacing it `:color`
24. `st.title` and `st.header` also get a new color divider argument
25. `None` as `default` inputs for most input widgets
26. Captions under each option in `st.radio`
27. `st.multiselect` gets a max selection limits argument
28. Streamlit logs go through their own Streamlit namespace logger, remember to use `config.toml` file for logging verbosity
29. `ttl` argument in `st.cache_data`and `st.cache_resource` accepts string formatted times like 30 days or 1 hour and 30
30. Hash funcs is back! `@st.cache_resource (hash_funcs={Person: str})`. Useful for telling Streamlit how to hash (which input/function variables to use) when caching functions.
31. Toolbar/hamburger menu - new client toolbar mode configuration to show/hide devop options in the toolbar, or entirely hide the toolbar if no menu items are set for the set page config method.
32. Browse note-worthy components (third-party modules) [here](https://streamlit.io/components)
33. Streamlit extras library [here](https://extras.streamlit.app/)
34. `StPaywall` - a component that adds an authentication window that only members with a paid subscription to Stripe or "buy me a coffee" can pass.
35. `Trubrics` - a component that adds a upvote/downvote button near the chat input, allows us to collect user feedback on generated responses with thumbs up/down, which can then be stored Trubrics cloud thru their API for later analysis.
36. Streamlit Creators Program - VIP team of people who made big contributions to the community. Other ways to contribute include becoming a streamlit advocate by regularly producing content, student ambassador, streamlit moderator to help maintain forum/discord server.
37. Streamlit Hackathon - AssemblyAI for auto transcriptions, LangChain/Llama Index for chatbot orchestration, Weaviate for vector database, Clarifai for gen AI in the cloud. Each of these has a specific Streamlit tutorial integration!
38. `st.rerun()` method to rerun the app. Useful for advanced use cases like when you need to rerun an app for each micro-batch of new data for pseudo real-time data processing. Use sparingly, read more about it [here](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun) (when to use vs when not to use)

39. Add anchor argument for quickly navigating through your app by changing the url - `st.title("Example :tada", anchor="title")` for `localhost:8501/#title`

40. Emoji and LaTeX formatting in `st.markdown()` - `:tada:` and `$$` for inline math and `$$$` for block math.

41. Custom CSS in `st.markdown()` using `unsafe_allow_html=True` argument.

42. Captions for footnotes (smaller, greyed out text) - `st.caption`

43. Map support for displaying geo-locations (need to provide dt of longitude/latitude) - `st.map()`

44. Add rows to dataframe and chart elements - `my_table.add_rows(df)`

45. Secret management in Streamlit - [Read here](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)

46. Media elements - `st.image`, `st.video`, `st.audio`

47. Input elements - `st.number_input`, `st.date_inGut`

48. Select box - poor man's multipage app

49. Number input - dedicated widget for numbers (`st.number_input`)

50. Date input - dedicated widget for dates (`st.date_input`)

51. File uploader - [learn more here](https://youtu.be/vIQQR_yq-8I?t=677)

52. Download button for files - [learn more here](https://youtu.be/vIQQR_yq-8I?t=677)

53. **Session State**
    - [Video 1](https://youtu.be/vIQQR_yq-8I?t=677)
    - [Video 2](https://www.youtube.com/watch?v=5l9COMQ3acc&list=PLM8lYG2MzHmRpyrk9_j9FW0HiMwD9jSl5&index=9)

54. `st.empty` - empty placeholder for layout purposes

55. Nicer looking components with `hydralit_components`

56. Set page config using `st.set_page_config`

57. `st.exception(e)` - for exception handling in Streamlit apps

58. `st.info`, `st.success`, `st.warning`, `st.error` for different types of alert messages

59. `st.spinner` to show loader while a function is running (works inside any context manager).

60. Progress bar, useful for showing progress of a long running process, can update any point in app - `st.progress`

61. stop app using `st.stop()` - useful for stopping app if user did not complete a form/condition not met.

62. Rerun app using `st.rerun` - advanced situations to reload data periodically, simulating real-time data.

63. Echo with `st.echo` - prints the code and output to app

64. `st.help` - displays help text for a function

## Features

1. Multiple [`st.chat_input()`](https://docs.streamlit.io/develop/api-reference/chat/st.chat_input) widgets (v1.31)
    - **React to user input.** When you enter text in it, the widget stores the submitted message into a python variable before clearing itself up.

        ```python
        # Send message to LLM using on_submit callback and
        # store both the message and response in session state
        # so the app rerun displays them
        prompt = st.chat_input("What is up?", on_submit=do_something)

        if prompt:
            # Display user message in chat message container
            st.chat_message("user").markdown(prompt)
        ```

    - **Can stack multiple chat inputs in an app.** But Streamlit chat inputs are so heavy that they stick to the bottom of the app. How to fix this?

        ```python
        # Use layout containers like st.container(), st.sidebar(), st.tabs(), st.expander(), or st.empty (empty placeholder)
        # they stick to order and location they were called into
        # coming with v1.31
        st.title("Multiple chat_input")

        with st.container():
            st.chat_input("What is your name?")
            st.chat_input("What is your surname?")
            st.chat_input ("Are you subscribed to my channel?")

            st.header("I'm a sandwich!")
            st.chat_input ("Keep chatting...")

        with st.sidebar:
            st.chat_input("Bread time")
        ```

2. [`st.write_stream()`](https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream) widget (v1.31)
    - **Streaming answers like with ChatGPT.** Tokens appear every few seconds to show the LLM is working hard! The widget takes as input an *OpenAI* stream, or a *LangChain* stream, or a generator function that spits tokens at every call. It's a cousin to `st.write()`, meaning it accepts markdown/Pillow images/Plotly figures/any data input just like `st.write()`.

3. Subtitles for Video Widget (v1.32)
    - **Display subtitles live over video using *srt/vtt* subtitle files (e.g. generated using Whisper).** Pass as argument to [`st.video()`](https://docs.streamlit.io/develop/api-reference/media/st.video) widget. Can even pass a dictionary of languages for subtitles, and Streamlit video player will provide you with language choice.

        ```python
        import streamlit as st

        st.video(
            "sintel-short.mp4",
            subtitles={
                "English": "subtitles-en.vtt",
                "German": "subtitles-de.vtt"
            }
        )
        ```

4. [`st.popover()`](https://docs.streamlit.io/develop/api-reference/layout/st.popover) widget for dialogue windows (v1.32)
    - When you click on it, it pops over a small dialogue window containing Streamlit widgets for input.

    - Opens just like an [`st.expander()`](https://docs.streamlit.io/develop/api-reference/layout/st.expander).

        ```python
        st.title("Small Modal Popover")

        with st.popover("Open popover"):
            st.markdown ("**Hello World**")
            name = st.chat_input("What's your name?")

        if name:
            st.header("Your name is: " + name)
        ```

    - Can will it with widgets using the `with` notation, can also store a popover into a variable, and call widgets on it, in-place of the `st` namespace.

        ```python
        info = st.popover("Open popover")

        # widgets
        info.success("Here is more info")

        data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        info.dataframe(data)

        info.plotly_chart(px.bar(data), use_container_width=True)
        ```

    - But **popover still behaves like a layout container...** You won't nest a pop-over inside a pop-over. But they can go into other layout elements like `st.sidebar`, `st.tabs`, and `st.expander`.

    - Also fits more complex widgets like dataframes, columns, or charts.

    - **While opening and closing a popover won't cause full app rerun, every widget interaction in the popover will trigger a full rerun.** This is really annoying...

    - Can around this using `st.form()`. Anything inside `st.form()` won't trigger a full rerun, **only clicking on the form submit button will trigger a full rerun**.

        ```python
        st.title("Small Modal Popover")

        with st.popover("Open login form"):
            with st.form("login", border=False):
                st.markdown("**Hello World**")
                st.text_input("Name", key="form_login")
                st.text_input ("Password", key="form_pwd", type="password")
                st.form_submit_button("Submit", type="primary")

        if st.session_state["form_login"] and st.session_state["form_pwd"]:
            st.success("Logged in!", icon="ℹ️")

        elif st.session_state["form_login"] or st.session_state["form_pwd"]:
            st.warning("Incomplete login", icon="⚡")
        ```

5. Hiding border in [`st.form()`](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form) (v1.29)
    - Now can hide border from a form using the `border=False` parameter. Looks better now!

        ```python
        with st.form("login", border=False):
            st.markdown("**Hello World**")
        ```

6. New `st.dialog` or `st.experimental_dialog` function decorator (Coming Soon)
    - **How it works**

        ```python
        @st.dialog("Dialog title")
        def show_dialog():
            st.write("This text is inside the dialog.")
            st.text_input("It can also contain widgets and any other elements.")
            if st.button("Close"):
                st.rerun()

        if st.button("Open dialog"):
            show_dialog()
        ```

    - **What it does**

        Closely follows `st.cache` API, just in an inverse way. Creating a function with `st.experimental_dialog` will kind of create an embedded Streamlit app in a dialogue window. This dialogue app will rerun the function at every widget interaction, without ever rerunning the full app, until it's closed.

    - First time Streamlit enables you to rerun part of the code without rerunning the whole app. So if you decorate your function with Streamlit widgets using `@st.experimental_fragment` (or something), this function becomes its own Streamlit container. Any interaction of a widget within this function will only rerun this function and not the full app. Just like for the dialogue window.

    - [See here for preview of st.dialog](https://dialog-preview.streamlit.app/)

    - The dialog function behaves like a [fragment](https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment): if you interact with a widget inside the dialog, only the function will rerun, not the rest of the app. This makes your app much more efficient and avoids long load times.

    - To close a dialog, you need to call st.rerun() inside the dialog function. This will rerun the entire app and therefore close the dialog.

    - A dialog always needs to have a title, which you can set via @st.experimental_dialog("Title").

    - You can show a wider dialog by setting width="large" in the decorator.

7. Partial reruns with [`st.fragment()`](https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment)
    - If you decorate a function with `st.fragment()`, this function becomes its own streamlit container. Any interaction of a widget within this function will **only rerun this function** and not the full app. Just like for the dialogue window. Very useful for plots!

    - Will enable a lot of new use cases, like streaming plots and dynamic forms (e.g. you select a country, it updates the form to select states if you selected USA).

    - Code sample

        ```python
        @st.fragment
        def meetup_chart():
            st.subheader("Developer meetups")
            st.caption("This chart always takes 1 seconds to load")
            time.sleep(1)
            first, last = st.slider("Month filter", 1, 7, (1, 7), label_visibility="collapsed")
            filtered_df = meetup_df[(meetup_df["month"] >= first) & (meetup_df["month"] <= last)]
            st.bar_chart(filtered_df, x="month", y="meetups", color=color)
        ```

8. Displaying certain pages to authenticated users with [`st.page_link`](https://docs.streamlit.io/develop/api-reference/widgets/st.page_link) (v1.33)
    - For [multipage apps](https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app), each Streamlit page must be its own file in the `pages/` directory next to your main streamlit script, you populate with new files, each becoming its own page, order and pages plus icon are being parsed out from file names...no way to control which items are displayed in the nav menu, everyone can access the full navigation.

    - **Can now hide automatically created navigation menu** by setting the `--client.showSidebarNavigation false` parameter when running `streamlit run app.py`. But then how do we navigate to pages?

    - But if you hide it, how do I then browse thru the different Streamlit pages? Use `st.page_link` widget. Can click on it to go to the given page/link. Also have arguments for display label/icon. No more emojis in file names...

        ```python
        with st.expander("Table of contents", expanded="...",):
            st.page_link("pages/secret.py", label="Secret page", icon="🔒")
            st.page_link("pages/hidden.py", label="Hidden page", icon="👀")
        ```

    - Great because now hide multiple pages from un-authenticated users with an if-clause

        ```python
        # for paying customers only
        if st.session_state["authenticated"]:
            st.page_link("pages/vip.py", label="VIP customer", icon="🔒"
            st.page_link("pages/subscribe.py", label="Pay for it", icon="👀")
        ```

    - [Watch video here](https://youtu.be/RW8b-lxCm_8?t=411)

9. Can browse to new page using [`st.switch_page`](https://docs.streamlit.io/develop/api-reference/navigation/st.switch_page) method (v1.30)
    - Completely remove every page navigation from the app and just push the user to different pages yourself, depending on the context of the situation.

    - For example, can have an if `st.button()` widget, when pressed we navigate to a new page using `st.switch_page()` and passing the `pages/secret.py` (e.g.). (for paywalled content).

        ```python
        with st.popover("A secret page")
            if st.button("Go to secret page"):
                st.switch_page("pages/secret.py")
        ```

10. Pass query arguments as dictionary to page, useful to initialize settings (v1.30)
    - **Another multipage behavior change**

    - If you include query params in the URL (e.g. `localhost:8501/?items=10%fruit=apple`), then change pages thru switch page or page link, those query params won't be propagated to the new URL anymore. Why care? Well...

    - In v1.30, query params in the URL can be retrieved as a dictionary using the new experimentalized [`st.query_params`](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.query_params) methods.

    - Can initialize widgets with values stored inside that URL. E.g. initialize slider value (see below)

        ```python
        q_params = st.query_params.to_dict()
        st.json (q_params)

        n = st.slider(
            "Number of cats to display",
            0, 16,
            int(q_params["items"]),
        )
        ```

11. Height parameter for [`st.container()`](https://docs.streamlit.io/develop/api-reference/layout/st.container) (v1.31)

    - Container now takes a height parameter, if put too many widgets in the container such that it becomes longer than the fixed height, it becomes longer than the fixed height, will display a scrollbar. Greatly benefits apps with grid look feeling.

        ```python
        st.title("Grid of cats")

        with st.container(height=200, border=False):
            c = st.columns(3)
            c[0].image("<https://cataas.com/cat?height=300>")
            c[1]. image("https: //cataas.com/cat?height=400") c[2].image("<https://cataas.com/cat?height=100>")

        with st.container (height=200, border=False):
            c = st.columns(3)
            c[0].image("<https://cataas.com/cat?height=350>") c[1].image("<https://cataas.com/cat?height=250>")
            c[2]. image("https: //cataas.com/cat?height=50")

        with st.container (height=200, border=False):
            c = st.columns(3)
            c[0].image("https: //cataas.com/cat?height=170") c[1]. image ("https: //cataas.com/cat?height=270") c[2]. image ("https: / /cataas.com/cat?height=320°)]
        ```

12. Dataframe and data editor have updated the tool bar for easier searching and data downloading (v1.31)

    - **Dataframe toolbar** now has a search bar to search for specific values in the dataframe. Also, can download the dataframe as a CSV file.

    - **Data editor toolbar** now has a search bar to search for specific values in the data editor. Also, can download the data editor as a CSV file.

13. Unit tests for your app (v1.28)
    - E.g. How do you write a unit test for your app example, where users that authenticate from a popover window have access to more navigation menu items.

    - New headless testing framework: [App Testing](https://docs.streamlit.io/develop/api-reference/app-testing), runs user code directly, simulates user input like interacting with popovers/text widgets, then analyzes the outputs. S

    - Streamlit has a [video](https://www.youtube.com/watch?v=99OEoP5sy0U) about it, watch to learn about **unit testing** streamlit apps.

14. Connect to databases using [`st.connection`](https://docs.streamlit.io/develop/api-reference/connections/st.connection) (v1.33)

    - Makes it easy to connect apps to data and APIs.

    - Code here

        ```python
        import streamlit as st

        conn = st.connection('pet_db', type='sql')
        pet_owners = conn.query('select * from pet_owners')
        st.dataframe(pet_owners)
        ```

    - Wrapper that provides a client to various databases or APIs based on the connection type it loads.

    - Can also just...connect to a *PostgreSQL*, call the connection in a cache resource with a time to live, and authenticate the credentials with a secrets file.

        ```python
        @st.cache_resource()
        def get_connection():
            return psycopg2.connect(
                **st.secrets["postgres"]
            )
        
        @st.cache_data(hash_funcs={
            psycopg2.extensions.connection: id
        })
        def get_data(engine, query):
            data = pd.read_sql(query, engine)
            return data
        ```

    - Information/guides about connecting to different data sources can be [found here](https://docs.streamlit.io/develop/tutorials/databases)

    - Note that don't have to use this, [read this](https://docs.streamlit.io/develop/concepts/connections/connecting-to-data
    ) to learn about other ways to connect to data sources.

    - **If using data sources, important to use [secret management](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management) to handle your credentials or secrets**. Secrets management allows you to store secrets securely and access them in your Streamlit app as environment variables.

15. New data editor using [`st.data_editor`](https://docs.streamlit.io/develop/api-reference/data/st.data_editor) (v1.33)
    - Cells/rows made editable to the user, returns changed df to your python code, or any changed cells through session states.

16. New toggle method using [`st.toggle`](https://docs.streamlit.io/develop/api-reference/widgets/st.toggle) (v1.33)
    - Useful if using a checkbox to toggle state in your app.

    - Alternative display of a chatbot...bit more obvious to the user that it's an on/off list.

17. Send a toast to your user with [`st.toast`](https://docs.streamlit.io/develop/api-reference/status/st.toast) method (v1.33)
    - Can display and stack notifications on the bottom right corner of the screen.

    - If fast enough, can even update the label of the toast, instead of stacking a pile of them (e.g. using as a way to indicate "Loading..." and "Ready").

    - **Useful to notify the user of the end of a long running process like a file download**...or toast being being grilled.

18. Another way to display the progress of a multi-step long running process - [`st.status`](https://docs.streamlit.io/develop/api-reference/status/st.status)
    - Like a fusion between an expander and a spinner, the state of the process is written on the expander label.
    - Every step of the process is detailed inside the expander.
    - When process is finished, sets a done checkmark in the label to notify you.
    - Can still send a toast at the end for a double notification.
    - Can even display [balloons](https://docs.streamlit.io/develop/api-reference/status/st.balloons) for **triple notifications!!!!!** But...why???????

19. Link button method that draws attention and redirects to external web page - [`st.link_button`](https://docs.streamlit.io/develop/api-reference/widgets/st.link_button) (v1.33)

20. Line chart, bar chart, scatter chart, etc accepts a "color" keyword argument
    - Code here

        ```python
        st.line_chart(
            chart_data,
            x="coll",
            y=["col2", "col3"],
            color=["#FF0000", (0, 255, 0)]
        )
        ```

21. Scatter chart, useful high level method to quickly build a scatter plot for a long or wide dataframe. The color and size keyword arguments can even accept a column name as input, which will fetch the color/size info directly at row level in the dataframe.

22. [`st.map()`](https://docs.streamlit.io/develop/api-reference/charts/st.map) also benefits from improved scatter plot.
    - You used to have to hard code the latitude/logitude column names in the input df, but with the revamped map, can now customize the columns yourself.

    - Code here

        ```python
        st.map(
            df,
            latitude='lat_col',
            longitude='lon_col',
            size='n citizens',
            color='color_city'
        )
        ```

    - Also gets the color/size treatment, where info can be stored in the df, in each row.

23. Markdown text/titles/headers/most widget labels can display colored text by prefacing it with a color with a specific set of rainbow colors.
    - Code here

        ```python
        st.markdown(
            ":red[Streamlit] :orange [can] :green [write] :blue[text] :violet[in] :gray [pretty] :rainbow[colors]"
        )
        ```

24. Titles and headers also get a new color divider argument, making it easier to differentiate the sections of an app.

25. None as default inputs. Most input widgets like select box and radio buttons now accept `None` as initial input, to represent an empty default state. This way you get select box/radio without any preselected option.

26. Captions under each option in [`st.radio`](https://docs.streamlit.io/develop/api-reference/widgets/st.radio). Acts like mini help descriptions for your items.

27. [Multi-select widget](https://docs.streamlit.io/develop/api-reference/widgets/st.multiselect) gets a max selection limits argument, so you can't select a million args anymore. And a placeholder info can also be displayed when no items are selected.

28. Streamlit logs go through their own Streamlit namespace logger, instead of being mixed with every other message inside the root logger. Cannot configure streamlit logging verbosity outside of the streamlit config file, **Don't use python logging from code** by importing `logging`. Streamlit uses a separate logging mechanism.

    - Example `config.toml` file

        ```python
        [logger]
        level = "info"
        messageFormat = "%(asctime)s % (message)s"
        ```

29. "ttl" argument in [cache data](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data) and [cache resource](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource) accepts string formatted times like 30 days or 1 hour and 30, or anything using the pandas time data constructor.

    - Example

        ```python
        @st.cache_data(ttl="1h30")
        def download_data():
            ...
            return data
        ```

30. Hash funcs is back! `@st. cache_resource (hash_funcs={Person: str})`

    - When you are adding cache data or cache resource to a function, Streamlit's cache mechanism will maintain a key value dict, with the function's arguments as key, and the function's results as value.

    - To build a key, Streamlit hashes every argument and object it finds in its body. So if any argument or variable in the func body changes, the cache will point to a different key and value.

        ```python
        # would hash: "url" and "person"
        @st.cache_data
        def download_data(url):
            r = requests.get(url)
            person = parse_persons(r)
            return person
        ```

    - Sometimes streamlit doesn't know how to hash third party objects like Pydantic models, or takes too mu h time hashing objects with a lot of nested elements like matplotlib figures. Streamlit's `hash_funcs` argument, can provide own dictionary of python type to caching class for **custom/optimized cache-key hashing**.

        ```python
        @st.cache_data(hash_funcs={Person: str})
        def download_data(url):
            r = requests.get(url)
            person = parse_persons(r)
            return person
        ```

    - [Read more about it here](https://docs.streamlit.io/develop/concepts/architecture/caching)

31. Toolbar/hamburger menu - new client toolbar mode configuration to show/hide devop options in the toolbar, or entirely hide the toolbar if no menu items are set for the set page config method.
    - [See toolbar mode here](https://docs.streamlit.io/develop/api-reference/configuration/config.toml)

32. [Browse note-worthy components (third-party modules) here](https://streamlit.io/components)

33. [Streamlit extras library here](https://extras.streamlit.app/)
    - [Grid layout](https://arnaudmiribel.github.io/streamlit-extras/extras/grid/)
    - [Stylable container](https://arnaudmiribel.github.io/streamlit-extras/extras/stylable_container/) that applies custom CSS to a widget
    - [Stlite sandbox](https://arnaudmiribel.github.io/streamlit-extras/extras/sandbox/) to run your untrusted python code in the browser

34. [StPaywall](https://github.com/tylerjrichards/st-paywall) - a component that adds an authentication window that only members with a paid subscription to Stripe or "buy me a coffee" can pass.

35. [Trubrics](https://blog.streamlit.io/trubrics-a-user-feedback-tool-for-your-ai-streamlit-apps/) - a component that adds a upvote/downvote button near the chat input, allows us to collect user feedback on generated responses with thumbs up/down, which can then be stored Trubrics cloud thru their API for later analysis.

36. [Streamlit Creators Program](https://streamlit.io/creators) - VIP team of people who made big contributions to the community. Other ways to contribute include [becoming a streamlit advocate](https://streamlit.io/community/advocates) by regularly producing content, student ambassador, streamlit moderator to help maintain forum/discord server.

37. [Streamlit Hackathon](https://streamlit.io/community/hackathon/llm-hackathon-2023)
    - AssemblyAI for auto transcriptions
    - LangChain/Llama Index for chatbot orchestration
    - Weaviate for vector database
    - Clarifai for gen AI in the cloud
    - Each of these has a specific Streamlit tutorial integration!
    - Even deeper...LangChain agent callbacks being built purely for Streamlit! And LangChain memory and messages primitives will soon integrate with streamlit session state and chat elements.

38. `st.rerun()` method to rerun the app. Useful for advanced use cases like when you need to rerun an app for each micro-batch of new data for pseudo real-time data processing.
    - Code example of use-case

        ```python
        while True:
            data = collect_data()
            df = process_data()
            visualize_data(df)
            st.rerun()
        ```

    - Good article on when to use/when not to use `st.rerun`, be careful of excessive use of it. [Read here](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun)

    - With `st.rerun()`

        ```python
        import streamlit as st

        if "value" not in st.session_state:
            st.session_state.value = "Title"

        ##### Option using st.rerun #####

        st.header(st.session_state.value)

        if st.button("Foo"):
            st.session_state.value = "Foo"
            st.rerun()
        ```

    - Using a callback to update an earlier header

        ```python
        ##### Option using a callback #####

        st.header(st.session_state.value)

        def update_value():
            st.session_state.value = "Bar"

        st.button("Bar", on_click=update_value)
        ```

    - Using containers to update an earlier header

        ```python
        ##### Option using a container #####

        container = st.container()

        if st.button("Baz"):
            st.session_state.value = "Baz"

        container.header(st.session_state.value)
        ```

39. Add anchor argument for quickly navigating through your app by changing the url
    - Example here

        ```python
        # navigate to localhost:8501/#title
        st.title("Example :tada:", anchor="title")
        st.write("...")
        ```

40. `st.markdown()` supports emojis with `:tada:` and LaTeX formatting using `$$` for inline math and `$$$` for block math.

41. `st.markdown` accepts a `unsafe_allow_html=True` HTML argument which you can use to color your text...or use the CSS hack.

42. `st.caption` for putting small text, like footnotes (greyed out, smaller text).

43. `st.map()` - takes in a dataframe of geo-locations to display/map with scatter plot, with each point corresponding to a latitude/longitude pair. Actually displays a world map with city markers.

44. Dataframe and chart (plot) elements accept an `add_rows` method. To programmatically add numpy/pandas data.
    - Code example here

        ```python
        my_table.add_rows(df)
        ```

45. [Secret management in Streamlit](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)

46. Media elements
    - `st.image`
    - `st.video`
    - `st.audio`
    - Can also take raw data from a file, `numpy` data you generated, file names or an URL. All 3 methods above can take in these things.

47. Input elements. They share these in common:
    - Add little tool tip to your widget using `help` argument
    - Disable any widget using `disabled` argument

        ```python
        st.<elem>(
            "Hello world,
            disabled=True
        )
        ```

    - **Key argument** is the widget's **identity**, by default it's the widget's label, which is why if you have multiple widgets named "Click me!", Streamlit cannot differentiate between those two. Make sure to add unique identifiers to your widget(s) using the key argument.

        ```python
        [
            st.button(
                "Click me!",
                key=f"id{i}"
            )

            for i in range(5)
        ]
        ```

    - [Read more here](https://docs.streamlit.io/develop/concepts/architecture/widget-behavior)

48. [Select Box](https://youtu.be/vIQQR_yq-8I?t=554) - poor man's multipage app. This one is pretty useful so check it out.

49. `st.number_input` - dedicated widget for numbers, with min and max values, and step size.

50. `st.date_input` - dedicated widget for dates, with min and max values, can include default tuple value for time period.

51. File uploader - [learn more here](https://youtu.be/vIQQR_yq-8I?t=677)
    - Returned result is of type `UplodadedFile`
    - Can get `getvalue` to get contents as byte array
    - Or can read as file (`pd.read_csv`, or anything that accepts a file as argument).

52. [Download button](https://youtu.be/vIQQR_yq-8I?t=716)

53. **Session State** - [Video 1](https://youtu.be/nnmBdpvN6u8?t=81) and [Video 2](https://www.youtube.com/watch?v=5l9COMQ3acc&list=PLM8lYG2MzHmRpyrk9_j9FW0HiMwD9jSl5&index=9)

54. [st.empty()](https://youtu.be/nnmBdpvN6u8?t=345)

55. Nicer looking components with [hydralit_components](https://github.com/TangleSpace/hydralit_components) - [Watch more here to learn about how to add external components to columns](https://youtu.be/nnmBdpvN6u8?t=381)

56. [Set page config](https://youtu.be/nnmBdpvN6u8?t=432) - put `st.set_page_config` at beginning of `__main__`.

57. st.info, st.success, st.warning, st.error

58. [st.exception(e)](https://youtu.be/nnmBdpvN6u8?t=468)

59. Any code inside context manager is going to show the spinner while it is running, good way to show user app is running, no problem! [st.spinner](https://youtu.be/nnmBdpvN6u8?t=476)

60. [`st.progress`](https://docs.streamlit.io/develop/api-reference/status/st.progress) - show progress bar (can edit at any point in the app)

61. [`st.stop`](https://docs.streamlit.io/develop/api-reference/execution-flow/st.stop)

    - [Video here](https://youtu.be/nnmBdpvN6u8?t=496)
    - Literally stops the app, use to stop the app if user did not complete all of the info or something in an input widget.

62. [`st.rerun`](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun)
    - [Video here](https://youtu.be/nnmBdpvN6u8?t=507)
    - Use for advanced situations, like when you want to rerun streamlit periodically to collect data and then display the new values, real-time system (kinda)

63. [`st.echo`](https://docs.streamlit.io/develop/api-reference/text/st.echo) - echo displays the code/results in the app.

64. [`st.help`](https://docs.streamlit.io/develop/api-reference/utilities/st.help) - show the help of a method that we don't know.

65. For debugging, display session state in sidebar
    - Example code

        ```python
        with st.sidebar:
            st.header("Debug")
            st.write(st.session_state.to_dict())
        ```

    - Hide sidebar by default using `iniial_sidebar_state="collapsed"` in `st.set_page_config()`

        ```python
            st.set_page_config(
                page_title="Wanderlust",
                page_icon=":icon:",
                layout="wide", initial_sidebar_state="collapsed",
            )
        ```
