class CowModel:
    def __init__(self):
        self.valid_colors = ['white', 'brown', 'pink']
        self.farm_data = {}
    
    def validate_cow_id(self, cow_id):
        return cow_id.isdigit() and len(cow_id) == 8 and cow_id[0] != '0'

    def validate_farm_id(self, farm_id):
        return farm_id.isdigit() and len(farm_id) == 1 and farm_id != '0'

    def validate_age(self, years, months):
        return (years.isdigit() and 0 <= int(years) <= 10) and (months.isdigit() and 0 <= int(months) <= 11)

    def validate_mother_id(self, mother_id):
        return mother_id.isdigit() and len(mother_id) == 8 and mother_id[0] != '0'

    def validate_owner_name(self, name):
        return name.isalpha() and name.islower() and len(name) <= 8

    def can_farm_accept_cow(self, farm_id, cow_color):
        if farm_id not in self.farm_data:
            self.farm_data[farm_id] = {'color': cow_color, 'count': 0}
            return True
        else:
            return self.farm_data[farm_id]['color'] == cow_color

    def register_cow(self, farm_id, cow_color):
        if farm_id in self.farm_data:
            self.farm_data[farm_id]['count'] += 1
        else:
            self.farm_data[farm_id] = {'color': cow_color, 'count': 1}

    def get_farm_summary(self):
        summary = []
        for farm_id, data in self.farm_data.items():
            summary.append(f"Farm {farm_id}: {data['count']} cow(s) of color {data['color']}")
        return "\n".join(summary)