import kivy 
from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config 


Config.set('graphics', 'resizable', True) 
  
# creating the App class 
class Relative_Layout(App):
      
    def build(self):
  
        # creating Relativelayout 
        grid = RelativeLayout()
        
        for i in range(0,1):
            # Grid row 1-3
            grid.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.9, 'center_y':.1},
                    text = str(i)))
            
            grid.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.3, 'center_y':.7},
                    text ="Grid 1", on_press = self.addPlayerNodes))
            grid.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.5, 'center_y':.7},
                    text ="grid 2", on_press = self.addPlayerNodes))
            grid.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.7, 'center_y':.7},
                    text ="grid 3", on_press = self.addPlayerNodes))
        
            # Grid row 4-6
            grid.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.3, 'center_y':.5},
                    text ="grid 4", on_press = self.addPlayerNodes))
            grid.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.5, 'center_y':.5},
                    text ="grid 5", on_press = self.addPlayerNodes))
            grid.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.7, 'center_y':.5},
                    text ="grid 6", on_press = self.addPlayerNodes))
        
            # Grid row 7-9
            grid.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.3, 'center_y':.3},
                    text ="grid 7", on_press = self.addPlayerNodes))
            grid.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.5, 'center_y':.3},
                    text ="grid 8", on_press = self.addPlayerNodes))
            grid.add_widget(Button(size_hint =(.2, .2),
                    pos_hint ={'center_x':.7, 'center_y':.3},
                    text ="grid 9", on_press = self.addPlayerNodes))
        # returning widget
        print(grid)
        return grid
    
    def addPlayerNodes(self, button):
        layout = GridLayout(cols = 1, padding = 10)
  
        popupLabel = Label(text = "Click for pop-up")
        closeButton = Button(text = "Close the pop-up")
  
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)       
  
        # Instantiate the modal popup and display
        popup = Popup(title ='Demo Popup',
                      content = layout,
                      size_hint =(None, None), size =(200, 200))  
        popup.open()   
  
        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)  
    
# run the App 
if __name__  == "__main__":
    Relative_Layout().run()