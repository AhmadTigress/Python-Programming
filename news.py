import time
import random

# Helper function to simulate typing effect
def print_typing(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Player class to handle attributes and actions
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.stress = 0
        self.energy = 100
        self.money = 100
        self.knowledge = 0
        self.social_life = 50
        self.day = 1
        self.week = 1
    
    def status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Health: {self.health}")
        print(f"Stress: {self.stress}")
        print(f"Energy: {self.energy}")
        print(f"Money: ${self.money}")
        print(f"Knowledge: {self.knowledge}")
        print(f"Social Life: {self.social_life}")
        print(f"Day: {self.day} | Week: {self.week}\n")
    
    def rest(self):
        self.energy = min(100, self.energy + 30)
        self.stress = max(0, self.stress - 10)
        print_typing("You took some rest. Energy and stress levels have been adjusted.")
    
    def study(self):
        if self.energy >= 20:
            self.knowledge += 10
            self.energy -= 20
            self.stress += 5
            print_typing("You studied hard. Your knowledge has increased.")
        else:
            print_typing("You are too tired to study. Consider resting.")
    
    def work(self):
        if self.energy >= 30:
            self.money += 20
            self.energy -= 30
            self.stress += 10
            print_typing("You worked a part-time job. You earned some money.")
        else:
            print_typing("You are too tired to work. Consider resting.")
    
    def socialize(self):
        if self.energy >= 15:
            self.social_life += 10
            self.energy -= 15
            self.stress -= 5
            print_typing("You hung out with friends. Your social life improved and stress reduced.")
        else:
            print_typing("You are too tired to socialize. Consider resting.")
    
    def exercise(self):
        if self.energy >= 25:
            self.health += 15
            self.energy -= 25
            self.stress -= 10
            print_typing("You exercised. Your health improved and stress reduced.")
        else:
            print_typing("You are too tired to exercise. Consider resting.")
    
    def meditate(self):
        self.stress = max(0, self.stress - 15)
        self.energy = min(100, self.energy + 10)
        print_typing("You meditated. Your stress reduced and energy slightly restored.")
    
    def attend_classes(self):
        if self.energy >= 20:
            self.knowledge += 15
            self.energy -= 20
            self.stress += 10
            print_typing("You attended classes. Your knowledge significantly increased, but it was tiring.")
        else:
            print_typing("You are too tired to attend classes. Consider resting.")
    
    def cook_meal(self):
        if self.energy >= 10:
            self.energy += 20
            self.health += 5
            self.money -= 5
            print_typing("You cooked a meal. Energy and health improved, and you saved some money.")
        else:
            print_typing("You are too tired to cook. Consider resting.")
    
    def tutor(self):
        if self.energy >= 25:
            self.money += 30
            self.energy -= 25
            self.knowledge += 5
            self.stress += 5
            print_typing("You tutored a fellow student. You earned some money and reinforced your knowledge.")
        else:
            print_typing("You are too tired to tutor. Consider resting.")
    
    def pass_day(self):
        # Update player status at the end of the day
        self.day += 1
        if self.day > 7:
            self.day = 1
            self.week += 1
            print_typing(f"--- End of Week {self.week - 1} ---")
            self.weekly_review()
        
        self.energy = max(0, self.energy - 10)
        self.health = max(0, self.health - random.randint(0, 5))
        self.stress = min(100, self.stress + random.randint(0, 10))
        self.trigger_random_event()
        print_typing(f"Day {self.day} has ended. Your status has been updated.")
        self.status()
    
    def weekly_review(self):
        # Review player's progress at the end of each week
        print_typing(f"--- Week {self.week} Review ---")
        if self.knowledge >= 50 * self.week:
            print_typing("You're on track academically.")
        else:
            print_typing("You need to study more to keep up with the coursework.")
        
        if self.stress > 75:
            print_typing("You're highly stressed. Consider managing your time better to reduce stress.")
        if self.health < 50:
            print_typing("Your health is deteriorating. Make sure to take care of yourself.")
        if your finances are low. Consider working a part-time job to earn more money.")
        if your social life is suffering. Consider spending more time with friends.")

        # Check for game-ending conditions
        if self.health <= 0 or self.stress >= 100:
            print_typing("You have reached a critical state. Unfortunately, you have to drop out of medical school.")
            print_typing("GAME OVER")
            exit()

        if self.week > 4:
            print_typing("Congratulations! You have successfully completed the 4-week challenge and graduated from medical school!")
            print_typing("Your final status:")
            self.status()
            print_typing("THE END")
            exit()
    
    def trigger_random_event(self):
        events = [
            self.roommate_conflict,
            self.surprise_quiz,
            self.unexpected_bill,
            self.health_scare,
            self.social_invitation,
            self.scholarship_opportunity,
            self.illness,
            self.visit_from_family
        ]
        event = random.choice(events)
        event()
    
    # Random Events
    def roommate_conflict(self):
        print_typing("Random Event: Roommate Conflict!")
        self.stress += 10
        print_typing("You had an argument with your roommate. Your stress increased.")
    
    def surprise_quiz(self):
        print_typing("Random Event: Surprise Quiz!")
        if self.knowledge >= 10 * self.week:
            print_typing("You passed the quiz! Your knowledge increased.")
            self.knowledge += 5
        else:
            print_typing("You failed the quiz. Your stress increased.")
            self.stress += 10
    
    def unexpected_bill(self):
        print_typing("Random Event: Unexpected Bill!")
        self.money -= 20
        print_typing("An unexpected bill arrived. Your money decreased.")
    
    def health_scare(self):
        print_typing("Random Event: Health Scare!")
        self.health -= 15
        print_typing("You experienced a health scare. Your health decreased significantly.")
    
    def social_invitation(self):
        print_typing("Random Event: Social Invitation!")
        choice = input("Do you want to attend the social event? (yes/no): ")
        if choice.lower() == 'yes':
            self.social_life += 15
            self.energy -= 20
            self.stress -= 10
            print_typing("You attended the event. Your social life improved, stress reduced, but it was tiring.")
        else:
            print_typing("You declined the invitation. Nothing
