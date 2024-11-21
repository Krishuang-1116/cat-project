from .cat import Cat


class Healthcheck:
    '''
    Perform checking on each attribute of cat against certain criteria.
    '''

    def __init__(self, pet: Cat):  # Type annotation for Python
        self.pet = pet
        self.age_group = self.get_age_group()

    # make age_group an instance variable, instead of a global variable
    def get_age_group(self):
        '''
        Define the age group for a cat
        '''
        if 0 <= self.pet.age <= 1:
            return "New born"
        if 1 < self.pet.age <= 3:
            return "Child"
        if 3 < self.pet.age <= 7:
            return "Adult"
        return "Aged"

    def check_weight(self):
        '''Check weight according to breed and age.
         Need to expand the weight_ranges list to include all major cat breeds,eg in the mock json data. 
        '''

        weight_ranges = {
            "Maine Coon": {
                "New born": (1, 2),
                "Child": (2, 3),
                "Adult": (4, 10),
                "Aged": (4, 8)},
            "Ragdoll": {
                "New born": (1, 2),
                "Child": (2, 3),
                "Adult": (4, 8),
                "Aged": (4, 7)
            }
        }

        breed_weight_ranges = weight_ranges.get(
            self.pet.breed, {})  # {} to prevent key error
        min_weight, max_weight = breed_weight_ranges.get(
            self.age_group, (4, 6))

        if min_weight <= self.pet.weight <= max_weight:
            return "Healthy weight."
        if self.pet.weight < min_weight:
            return "Cat is underweight."
        return "Cat is overweight."

    def check_temperature(self):
        '''
        Check temperature according to age.
        '''
        temp_ranges = {
            "New born": (39, 41),
            "Child": (38.5, 40),
            "Adult": (38.5, 39.5),
            "Aged": (38.5, 39.5)
        }

        min_temp, max_temp = temp_ranges.get(self.age_group, (38.5, 39.5))

        if min_temp <= self.pet.body_temp <= max_temp:
            return "Your cat's temperature is normal."
        if self.pet.body_temp < min_temp:
            return "Your cat's showing signs of hypothermia."
        return "Your cat's showing signs of hyperthermia."

    def check_vomit(self):
        '''
        Check if cat vomits in two consecutive days.
        '''
        if sum(self.pet.vomit) >= 2:
            for i in range(len(self.pet.vomit)-1):
                if self.pet.vomit[i] and self.pet.vomit[i+1]:
                    return "Your cat develops signs of FIP."
            return "Your cat vomits but not in two consecutive days. Keep close monitoring!"
        return "Your cat does not vomit for the last 5 days. Keep up the good work!"

    def health_status(self):
        '''
        Return the health status of the cat
        '''
        messages = []
        messages.append(self.check_weight())
        messages.append(self.check_temperature())
        messages.append(self.check_vomit())
        return "\n".join(messages)
