from streamlit_elements import mui,html,elements,dashboard,event,media,editor

# SRC: https://share.streamlit.io/okld/streamlit-gallery/main?p=elements
# material.ui inside streamlit is amazing.


def probando_dashboard():
    with elements("dashboard"):
        layout = [
            # Parameters: element_identifier, 
            #             x_pos, y_pos, 
            #             width, height, [item properties...]

            dashboard.Item("first_item", 0, 0, 2, 2),
            dashboard.Item("second_item", 2, 0, 2, 2,
                           isDraggable=False, moved=False),
            dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
        ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find in the GitHub links below.

        with dashboard.Grid(layout):
            mui.Paper("First item", key="first_item")
            mui.Paper("Second item (cannot drag)", key="second_item")
            mui.Paper("Third item (cannot resize)", key="third_item")


def probando_elements():
    with elements("dashboard"):
        layout = [dashboard.Item(f"item{i}", i/2, i, 2, 1) for i in range(4)]

        with dashboard.Grid(layout):
            for i in range(len(layout)):
                mui.Paper(f"Item {i}", key=f"item{i}")
    
                
    





def probando_elementsBackup():

    with elements("nested_children"):

        # You can nest children using multiple 'with' statements.
        #
        # <Paper>
        #   <Typography>
        #     <p>Hello world</p>
        #     <p>Goodbye world</p>
        #   </Typography>
        # </Paper>

        with mui.Paper:
            with mui.Typography:
                html.p("Hello world")
                html.p("Goodbye world")



    with elements("properties"):

        # You can add properties to elements with named parameters.
        #
        # To find all available parameters for a given element, you can
        # refer to its related documentation on mui.com for MUI widgets,
        # on https://microsoft.github.io/monaco-editor/ for Monaco editor,
        # and so on.
        #
        # <Paper elevation={3} variant="outlined" square>
        #   <TextField label="My text input" defaultValue="Type here" variant="outlined" />
        # </Paper>

        with mui.Paper(elevation=3, variant="outlined", square=True):
            mui.TextField(
                label="My text input",
                defaultValue="Type here",
                variant="outlined",
            )

    # If you must pass a parameter which is also a Python keyword, you can append an
    # underscore to avoid a syntax error.
    #
    # <Collapse in />

        mui.Collapse(in_=True)
        mui.Box('.')

        mui.Box(
            "Some text in a styled box",
            sx={
                "bgcolor": "background.paper",
                "boxShadow": 1,
                "borderRadius": 2,
                "p": 2,
                "minWidth": 300,
            }
        )
     
        # genial esto


        html.div(
            "This has a green background",
            css={
                "backgroundColor": "green",
                "&:hover": {
                    "color": "yellow"
                }
            }
        )









    with elements("multiple_children"):

        # You have access to Material UI icons using: mui.icon.IconNameHere
        #
        # Multiple children can be added in a single element.
        #
        # <Button>
        #   <EmojiPeople />
        #   <DoubleArrow />
        #   Hello world
        # </Button>

        mui.Button(
            mui.icon.EmojiPeople,
            mui.icon.DoubleArrow,
            "Button with multiple children"
        )

        # You can also add children to an element using a 'with' statement.
        #
        # <Button>
        #   <EmojiPeople />
        #   <DoubleArrow />
        #   <Typography>
        #     Hello world
        #   </Typography>
        # </Button>

        with mui.Button:
            mui.icon.EmojiPeople()
            mui.icon.DoubleArrow()
            mui.Typography("Button with multiple children")



    with elements("dashboard"):

        # You can create a draggable and resizable dashboard using
        # any element available in Streamlit Elements.

    

        # First, build a default layout for every element you want to include in your dashboard

        layout = [
            # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
            dashboard.Item("first_item", 0, 0, 2, 2),
            dashboard.Item("second_item", 2, 0, 2, 2,
                        isDraggable=False, moved=False),
            dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
        ]

        # Next, create a dashboard layout using the 'with' syntax. It takes the layout
        # as first parameter, plus additional properties you can find in the GitHub links below.

        with dashboard.Grid(layout):
            mui.Paper("First item", key="first_item")
            mui.Paper("Second item (cannot drag)", key="second_item")
            mui.Paper("Third item (cannot resize)", key="third_item")



    with elements('callbacks'):
        def hotkey_pressed():
            print("Hotkey pressed")

        event.Hotkey("g", hotkey_pressed)

        # If you want your hotkey to work even in text fields, set bind_inputs to True.
        event.Hotkey("h", hotkey_pressed, bindInputs=True)
        mui.TextField(label="Try pressing 'h' while typing some text here.")

        # If you want to override default hotkeys (ie. ctrl+f to search in page),
        # set overrideDefault to True.
        event.Hotkey("ctrl+f", hotkey_pressed, overrideDefault=True)



    with elements("media_player"):
        pass
        # Play video from many third-party sources: YouTube, Facebook, Twitch,
        # SoundCloud, Streamable, Vimeo, Wistia, Mixcloud, DailyMotion and Kaltura.
        #
        # This element is powered by ReactPlayer (GitHub link below).


        #media.Player(
        #    url="https://www.youtube.com/watch?v=FPjkKVovDgs&ab_channel=GilbertoTob%C3%B3nSan%C3%ADn", 
        #    controls=True)

    with elements("monaco_editors"):

        # Streamlit Elements embeds Monaco code and diff editor that powers Visual Studio Code.
        # You can configure editor's behavior and features with the 'options' parameter.
        #
        # Streamlit Elements uses an unofficial React implementation (GitHub links below for
        # documentation).


       
        mui.Typography("Content: ", 'jola')

        

        editor.Monaco(
            height=300,
            defaultValue='hello',
            #onChange=lazy(update_content)
        )

        mui.Button("Update content")#, onClick=sync())

        editor.MonacoDiff(
            original="Happy Streamlit-ing!",
            modified="Happy Streamlit-in' with Elements!",
            height=300,
        )
