from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout



class Grid_LayoutApp(App):
 
    # to build the application we have to
    # return a widget on the build() function.
    def build(self):
 
        # adding GridLayouts in App
        # Defining number of column
        # You can use row as well depends on need
        layout = GridLayout(cols = 3, padding = [150, 150, 150, 150])
        layout.add_widget(Button(text ='Grid 1'))
        layout.add_widget(Button(text ='Grid 2'))
        layout.add_widget(Button(text ='Grid 3'))
        layout.add_widget(Button(text ='Grid 4'))
        layout.add_widget(Button(text ='Grid 5'))
        layout.add_widget(Button(text ='Grid 6'))
        layout.add_widget(Button(text ='Grid 7'))
        layout.add_widget(Button(text ='Grid 8'))
        layout.add_widget(Button(text ='Grid 8'))
                          
 
        # returning the layout
        return layout
 
# creating object of the App class
root = Grid_LayoutApp()
# run the App
root.run()