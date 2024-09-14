from Model.cow_model import CowModel
from View.white_cow_view import WhiteCowView
from View.brown_cow_view import BrownCowView
from View.pink_cow_view import PinkCowView

class CowController:
    def __init__(self, main_window):
        self.model = CowModel()
        self.main_window = main_window

    def handle_color_submission(self, color):
        if color in self.model.valid_colors:
            self.main_window.hide()
            if color == 'white':
                self.view = WhiteCowView(self)
            elif color == 'brown':
                self.view = BrownCowView(self)
            elif color == 'pink':
                self.view = PinkCowView(self)
            self.view.show()
        else:
            self.main_window.show_error_message("Invalid color")

    def submit_white_cow(self, cow_id, farm_id, years, months):
        if not self.model.validate_cow_id(cow_id):
            self.view.show_error_message("Invalid Cow ID")
        elif not self.model.validate_farm_id(farm_id):
            self.view.show_error_message("Invalid Farm ID")
        elif not self.model.validate_age(years, months):
            self.view.show_error_message("Invalid Age")
        elif not self.model.can_farm_accept_cow(farm_id, 'white'):
            self.view.show_error_message(f"Farm {farm_id} already has cows of another color.")
        else:
            self.model.register_cow(farm_id, 'white')
            self.show_farm_summary()

    def submit_brown_cow(self, cow_id, farm_id, mother_id):
        if not self.model.validate_cow_id(cow_id):
            self.view.show_error_message("Invalid Cow ID")
        elif not self.model.validate_farm_id(farm_id):
            self.view.show_error_message("Invalid Farm ID")
        elif not self.model.validate_mother_id(mother_id):
            self.view.show_error_message("Invalid Mother ID")
        elif not self.model.can_farm_accept_cow(farm_id, 'brown'):
            self.view.show_error_message(f"Farm {farm_id} already has cows of another color.")
        else:
            self.model.register_cow(farm_id, 'brown')
            self.show_farm_summary()

    def submit_pink_cow(self, cow_id, farm_id, first_name, last_name):
        if not self.model.validate_cow_id(cow_id):
            self.view.show_error_message("Invalid Cow ID")
        elif not self.model.validate_farm_id(farm_id):
            self.view.show_error_message("Invalid Farm ID")
        elif not self.model.validate_owner_name(first_name) or not self.model.validate_owner_name(last_name):
            self.view.show_error_message("Invalid Owner Name")
        elif not self.model.can_farm_accept_cow(farm_id, 'pink'):
            self.view.show_error_message(f"Farm {farm_id} already has cows of another color.")
        else:
            self.model.register_cow(farm_id, 'pink')
            self.show_farm_summary()

    def show_farm_summary(self):
        summary = self.model.get_farm_summary()
        self.main_window.show_summary(summary)
        self.view.close()
        self.main_window.show()
