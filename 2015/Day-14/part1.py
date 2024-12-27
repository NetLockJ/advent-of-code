class Reindeer:
    
    def __init__(self, name, speed, flight_duration, rest):
        self.name = name
        self.speed = speed
        self.rest = rest
        self.flight_duration = flight_duration
        self.distance = 0
        self.count = -flight_duration
    
    def simulate(self):
        if self.count > self.rest - 1:
            self.count = -self.flight_duration
        if self.count < 0:
            self.distance += self.speed
        
        self.count += 1

        return self.distance

    def get_distance(self):
        return self.distance


deer = []

src = open("./input.txt").read().split("\n")[:-1]
for line in src:
    line = line.split(" ")
    print(line[0], int(line[3]), int(line[6]), int(line[13]))
    deer.append(Reindeer(line[0], int(line[3]), int(line[6]), int(line[13])))

for i in range(0, 2503):
    for d in deer:
        d.simulate()

distance = 0

for d in deer:
    distance = max(distance, d.get_distance())

print(distance)