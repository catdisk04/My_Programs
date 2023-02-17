import random

#TODO unable to reach a constant population. its always decreasing
#TODO date and timestep available in environment
def sim_days(num_days, time_steps, environment):
    sim_report = {}
    for day in range(num_days):
        environment.day = day
        day_report = sim_day(time_steps, environment)
        sim_report[day] = day_report
    return sim_report


def sim_day(time_steps, environment):
    for time_step in range(time_steps):
        environment.time_step = time_step
        for i in environment.organisms:
            i.move()

    environment.new_day()
    print(environment.report())
    return environment.report()
    
    return 

class Organism():
    def __init__(self, x, y, environment_var, gene1 = 0.2):
        self.gene1 = gene1 # expresses the preferred number of foods before returning to edge
        
        self.go_home=False
        
        self.environment = environment_var
        
        #number of food units collected during the day
        self.food = 0 
        
        
        self.x = x
        self.y = y
        
        self.is_alive=True
        
        self.pos_log=[[self.x, self.y]]
        self.birth_date = [self.environment.day, self.environment.time_step]
        self.death_date = False
        print
        
    def feed(self):
        self.food += 1
        
    def feed_sate(self):
        return self.food
    
    def reproduce(self):
        if self.is_alive:
            self.environment.organisms.append(Organism(self.x, self.y, self.environment,  self.gene1+((random.random()-0.5)/20)))
            
    
    def new_day(self):
        if self.is_alive:
            if not self.environment.get_block(self.x, self.y).is_edge():
                self.is_alive = False
                self.death_date = [self.environment.day, self.environment.time_step]
                return
            
            if self.food == 0:
                self.is_alive = False
                self.death_date = [self.environment.day, self.environment.time_step]
            elif self.food == 2:
                self.reproduce()
            self.food = 0
        

    
    def move(self):
        
        if self.is_alive:
            state = ((self.food)/2)-self.gene1
            
            if random.random() < state:
                self.go_home=True
            else:
                self.random_move()  
                return
            if self.go_home:
                self.move_to_edge()
            
            self.pos_log.append([self.x, self.y])
        return 
    
    def random_move(self):
        i = random.random()
        if i <0.25:
            self.x +=1
        elif i < 0.5:
            self.y+=1
        elif i < 0.75:
            self.x-=1
        else:
            self.y -=1
        
        self.handle_move()

    def handle_move(self):
        if self.x == self.environment.length:
            self.x = self.environment.length-1
        if self.y == self.environment.width:
            self.y = self.environment.width-1
        if self.x <0:
            self.x = 0
        if self.y <0:
            self.y= 0
            
        block = self.environment.get_block(self.x, self.y)
        if block.food:
            self.food += 1
            block.food = False
    
    #TODO something to make the organism reluctant to change direction
    
    def move_to_edge(self):
        dist_to_right = self.environment.length-self.x
        dist_to_left = self.x
        dist_to_top = self.environment.width-self.y
        dist_to_bottom = self.y
        
        min_dist = min(dist_to_bottom, dist_to_left, dist_to_right, dist_to_top)
        
        if min_dist==dist_to_right:
            self.x +=1
        elif min_dist == dist_to_left:
            self.x -=1
        elif min_dist == dist_to_top:
            self.y += 1
        elif min_dist == dist_to_bottom:
            self.y -= 1
        
        self.handle_move()
            
        
class Environment():
    def __init__(self, x, y, food_blocks, starting_organisms):
        self.env_blocks = []
        for i in range(x):
            for j in range(y):
                self.env_blocks.append(Env_block(i, j, self))
        self.length = x
        self.width = y
        self.no_of_food_blocks = food_blocks
        self.no_of_starting_organisms = starting_organisms
        self.organisms = []
        self.day = 0.
        self.time_step = 0
        for i in range(self.no_of_starting_organisms):
            x, y = self.generate_pos()
            self.organisms.append(Organism(x, y, self))
        self.set_food()


    def generate_pos(self):
        x = random.randrange(0, self.length)
        y = random.randrange(0, self.width)
        return x, y
    
    def get_block(self, x, y):
        # blocks = self.env_blocks
        # for block in blocks:
        #     if block.x == x and block.y==y:
        #         return block
        # return 0
        index = x*self.length+y
        return self.env_blocks[index]
    
    def set_food(self):
        for i in self.env_blocks:
            i.food=False
        for i in range(self.no_of_food_blocks):
            while True:
                x, y = self.generate_pos()
                block = self.get_block(x, y)
                if not block.food:
                    block.set_food()
                    break
    
    def report(self):
        food_blocks, organisms, alive = 0, 0, 0
        for i in range(self.length):
            for j in range(self.width):
                if self.get_block(i, j).food:
                    food_blocks += 1
        for organism in self.organisms:
            organisms += 1
            if organism.is_alive:
                alive +=1
        D={}
        D["food blocks"] = food_blocks
        D["organisms"] = organisms
        D["alive"] = alive
        return D
    
    def new_day(self):
        for i in range(len(self.organisms)):
            self.organisms[i].new_day()
        self.set_food()

        

class Env_block():
    def __init__(self, x, y, environment_var):
        self.environment = environment_var
        self.x = x
        self.y = y
        self.food = False
        
    
    def is_edge(self):
        state=False
        if self.x == 0 or self.x == self.environment.length-1:
            state = True
        if self.y == 0 or self.y == self.environment.width-1:
            state = True
        return state
    
    def set_food(self):
        self.food = True

env=Environment(100, 100, 5000, 100)
print(sim_days(100, 1000, env))