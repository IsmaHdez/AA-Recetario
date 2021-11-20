from kivy.app import App
from inventory import InventoryWindow

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from kivy.lang.builder import Builder

class InventoryScreen(Screen):
    def __init__(self, **kwargs):
        super(InventoryScreen, self).__init__(**kwargs)
        Builder.load_file('inventory.kv')
        self.add_widget(InventoryWindow())
    pass

class RecipeScreen(Screen):
    def __init__(self, **kwargs):
        super(RecipeScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='recipe'))
    pass

class MealScreen(Screen):
    def __init__(self, **kwargs):
        super(MealScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='meal'))
    pass

class ShopScreen(Screen):
    def __init__(self, **kwargs):
        super(ShopScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='shop'))
    pass

class ModuleContainer(ScreenManager):
    def __init__(self, **kwargs):
        super(ModuleContainer, self).__init__(**kwargs)
        self.add_widget(InventoryScreen(name = 'inventory'))
        self.add_widget(ShopScreen(name = 'shopping'))
        self.add_widget(MealScreen(name = 'mealplan'))
        self.add_widget(RecipeScreen(name = 'recipes'))
    pass

class NavBar(GridLayout):
    pass

class AppContainer(GridLayout):
    def __init__(self, **kwargs):
        super(AppContainer, self).__init__(**kwargs)
        print(self.children)
    pass

class Vittler(App):
    def build(self):
        return AppContainer()


if __name__=="__main__":

    vit = Vittler()
    Builder.load_file('main.kv')
    vit.run()