# Useful Tips for Styling Streamlit Widgets

1. **Markdown Trick**
    - Code example

        **Applying CSS**

        ```python
        st.markdown(
        """
        <style>
        .stApp {
            background-color: green;
        }
        </style>
        """,
        unsafe_allow_html=True
        )
        ```

        **Applying HTML**

        ```python
        st.markdown(
            """
            <h1>Hello World</h1>
            """
            unsafe_allow_html=True
        )
        ```

    - [Video here](https://youtu.be/AtRf_eRQZwQ?t=8)

2. **iFrame Sandbox Breaking**
    - Code example

        ```python
        st.title("Escape the Sandbox")
        st.button("Red")
        st.button ("Blue")
        st.button("Green")

        components.html("""
        <script>
        const elements = window.parent.document.querySelectorAll('.stButton > button')
        elements[0].style.backgroundColor = 'lightcoral'
        elements[1].style.backgroundColor = 'lightblue'
        elements[2].style.backgroundColor = 'lightgreen'
        </script>
        """,
            height=0, 
            width=0
        )
        ```

    - [Video here](https://youtu.be/AtRf_eRQZwQ?t=11)

3. **Simpler Way to Style Widgets** - `st.stylable_container`

    - [See this](https://discuss.streamlit.io/t/button-css-for-streamlit/45888/9) for how to accomplish this without using the `st.stylable_container` context manager which comes with **streamlit-extras**.

    - Basically: **The secret is in the new *CSS* `:has pseudo-class`, one can inject the Markdown span element with a key class in a `st.container()` and a CSS selector which only selects containers that contains a span with a certain key class.**

    - `st.stylable_container` from [streamlit extras](https://extras.streamlit.app/) is a context manager that uses this trick in order to allow you to apply CSS styles to all its nested widgets.

    - Example here

        ```python
        from streamlit_extras.stylable_container import stylable_container

        with stylable_container(
            key="cat_image",
            css_styles="""
            div[data-testid="stImage"] > img {
                border-radius: 100px;
            }
            """,
        ):
            st.image("./cat.jpg")
        
        ```

    - Streamlit is a React web app which compiles to HTML/CSS/JS for your browser.

    - Any element element style is specified with its CSS.
    - So if you want to restyle a widget in your app, you want to pick into your Streamlit app's CSS through a mirror as you edit it.

    - Inspector Keyboard Shortcut: `CMD OPT i`. Press `Elements` tab...

    - Or Open Web Browser -> `More Tools` -> `Developer Tools` -> `Elements`

    - Long html... no time to browse full HTML tree for specific widget...

    - Fortunately, can search the HTML tree (e.g. for searching for a `st.image("./cat.jpg")`), **click on the little arrow button on top left**, called the `Inspector`.

    - **Can now hover any part of the app, corresponding HTML element will be highlighted now**

    - Can also right click on a widget/element, and inspect it, the `img` tag of the image should now be outlined.

    - Can see the CSS skin here, in the `Styles` tab.

    - Now we want the cat to have round corner, notice it is enclosed in a div:

        ```html
        <div data-testid="stImage" class="css-1v0mbdj e115fcil1">
            <img src="https://localhost:8501/media/5rgdfg....jpg" alt="0>
        </div>
        ```

    - Some other random class classes that we won't be using here (e.g. `class="css-1v0mbdj e115fcil1`), because it will probably change between two Streamlit versions.

    - Head back to `Styles` tab for the outlined image, play around/edit some of them with the inspect element tool to see how it changes

    - At the top there is an `element.style{}` part, which you can edit to add and overwrite css properties. E.g. double click and add a `border-radius: 100px`, this will override any other border-radius property and now your cat has curvy lines!!!

    - Good way of training your CSS styling skills.

    - These changes will be lost when we close the browser...

    - Ideally we could do something like this: `st.image (" ./cat.jpg", css-"border-radius: 100px")`

    - Or if you're a Streamlit **power user**, can create a `st.container` with a set of CSS properties that applies to every widget nested inside:

        ```python
        with container(css="img { border-radius: 100px; }"):
            st.image("./cat.jpg")
        ```

    - **NEW CSS PSEUDO CLASS** recently added to browsers (except Firefox, where it is hid behind a flag: `layout.css.has-selector.enabled`)  

    - Can simulate a stylable container context manager.

    - **IMPORTANT**: The secret is in the new CSS `:has pseudo-class`, one can inject a markdown span element with a key class in a `st.container` and a CSS Selector which only selects containers that contain a span with a certain key class.

    - What does that mean? Basically there is a way to create a `st.container` which applies CSS styles to all its nested widgets.

    - [See here for link to stylable container](https://arnaudmiribel.github.io/streamlit-extras/extras/stylable_container/)

    - Example here

        ```python
        from streamlit_extras.stylable_container import stylable_container

        with stylable_container(
            key="cat_image",
            css_styles="""
            div[data-testid="stImage"] > img {
                border-radius: 100px;
            }
            """,
        ):
            st.image("./cat.jpg")
        
        ```

    - Moved the cat image to the new stylable container context manager, just like you'd add elements into an expander.

    - Give the container a unique key (e.g. `cat_image`), then write down the CSS properties to a apply a border radius (e.g.) to any image tag directly under any div with the `stImage` *data-testid* attribute.

        ```html
        <div data-testid="stImage" class="dsgjdfgdf fds">
            <img src="https://localhost:8501/media/5rgdfg....jpg" alt="0">
        </div>
        ```

    - Any images in `stImage` div, which are only generated through `st.image`, now have curves!

    - [Useful video here](https://www.youtube.com/watch?v=AtRf_eRQZwQ)

    - Markdown element doesn't seem to care about parent container's padding, **unfortunately has a fixed width defined by the Streamlit server**...so also need extra right padding to the markdown element. Fortunately can pass a list of CSS styles to `stylable_container`, so make this a list, add an extra style for any markdown element in the container, and insert that extra right padding.

    - So can just eat adding a bunch of `st.stylable_container` elements to your app, injects HTML/CSS blocks, so performance overhead is low, but still a hack...let's see why it's not great below

    - **Problems with this approach**:
        1. Abuses `:has` CSS psuedo class, which some browsers (e.g. *Firefox*) have disabled

        2. Widgets with response width, fixed by Streamlit like `st.markdown` or plots or dataframes, will overlap their parent's containers like `columns`, will need some work on the target children to properly style them.

        3. Some widgets with appearing/disappearing elements like the select box, may not be fully contained in the parent container, so they won't be targeted by the CSS.

    - But useful for applying quick color and size retouches to buttons and checkboxes (e.g.), this is the best way to do it!

4. Useful Links for Styling Purposes
    - [How to dynamically place stuff on screen, separate layout from logic/rendering](https://discuss.streamlit.io/t/ugly-screen-shifting-when-rendering-how-to-avoid-this/7790)

    - [How to build any button](https://discuss.streamlit.io/t/how-to-build-an-unique-button-in-streamlit-web-program/12012/22?page=2)

    - [How to apply custom styling to any container](https://discuss.streamlit.io/t/applying-custom-css-to-manually-created-containers/33428/7)

    - [How to change font size in st.write()](https://discuss.streamlit.io/t/change-font-size-in-st-write/7606)
