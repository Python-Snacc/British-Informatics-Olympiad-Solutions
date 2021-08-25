alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


class Room():
    def __init__(self, roomLetter):
        self.Letter = roomLetter
        self.connectedRooms = []
        self.visited = 0
        self.connectionUsed = []


class Spy():
    def __init__(self, plan, r):
        self.plan = plan
        self.unexploredRooms = alphabet[:r]
        self.nonPlanRooms = []
        for room in self.unexploredRooms:
            self.nonPlanRooms.append(room)
        self.ans = self.rooms = []

    def construct_map(self):
        rooms = []
        chosen = []
        while True:
            i = 0
            usedRooms = [room.Letter for room in rooms]
            if len(self.plan)== 0:
                for room in chosen:
                    self.unexploredRooms.remove(room)
                if self.unexploredRooms[0] in usedRooms:
                    rooms[usedRooms.index(self.unexploredRooms[0])].connectedRooms.append(self.unexploredRooms[1])
                else:
                    rooms.append(Room(self.unexploredRooms[0]))
                    rooms[-1].connectedRooms.append(self.unexploredRooms[1])
                if self.unexploredRooms[1] in usedRooms:
                    rooms[usedRooms.index(self.unexploredRooms[1])].connectedRooms.append(self.unexploredRooms[0])
                else:
                    rooms.append(Room(self.unexploredRooms[1]))
                    rooms[-1].connectedRooms.append(self.unexploredRooms[0])
                break
            while True:
                if self.nonPlanRooms[i] not in self.plan:
                    break
                else: i += 1
            if self.nonPlanRooms[i] not in usedRooms:
                first_room = Room(self.nonPlanRooms[i])
                chosen.append(self.nonPlanRooms[i])
                first_room.connectedRooms.append(self.plan[0])
                rooms.append(first_room)
            else:
                chosen.append(self.nonPlanRooms[i])
                rooms[usedRooms.index(self.nonPlanRooms[i])].connectedRooms.append(self.plan[0])

            if self.plan[0] in usedRooms:
                rooms[usedRooms.index(self.plan[0])].connectedRooms.append(self.nonPlanRooms[i])
            else:
                second_room = Room(self.plan[0])
                second_room.connectedRooms.append(self.nonPlanRooms[i])
                rooms.append(second_room)
            del self.plan[0]
            del self.nonPlanRooms[i]
        cR = [room.connectedRooms for room in rooms]
        rL = [room.Letter for room in rooms]
        #####################################################
        self.ans = [''.join(s) for s in [sorted(connections) for connections, roomLetters in sorted(zip(cR, rL), key=lambda pair: pair[1])]]
        for line in self.ans:
            print(line)
            
        for room in rooms:
            room.connectedRooms = sorted(room.connectedRooms)

        self.rooms = [room for room, roomLetter in sorted(zip(rooms, [room.Letter for room in rooms]), key=lambda pair: pair[1])]

    def move(self, n):
        for room in self.rooms:
            room.visited = 0
            room.connectionUsed = []
            for i in range(len(room.connectedRooms)):
                room.connectionUsed.append(0)
        currentLetter = "A"
        nextLetter = ""
        for moves in range(n):
            currentRoom = self.rooms[alphabet.index(currentLetter)]
            currentRoom.visited += 1
            if currentRoom.visited % 2 == 1:
                nextLetter = currentRoom.connectedRooms[0]
                currentRoom.connectionUsed[0] += 1
            else:
                for i in range(len(currentRoom.connectionUsed)):
                    if currentRoom.connectionUsed[i] % 2 == 1:
                        if i == len(currentRoom.connectionUsed) -1:
                            nextLetter = currentRoom.connectedRooms[i]
                            currentRoom.connectionUsed[i] += 1
                        else:
                            nextLetter = currentRoom.connectedRooms[i+1]
                            currentRoom.connectionUsed[i+1] += 1
                        break                    
                            
            currentLetter = nextLetter
        return str(currentLetter)
                
if __name__ == '__main__':
    NAME = ""
    SCHOOL = ""
    print(f"Name: {NAME}\nSchool: {SCHOOL}")
    while True:
        print("\n")
        plan, p, q = input().split()
        spy = Spy(list(plan), len(plan) + 2)
        spy.construct_map()
        print(spy.move(int(p)) + spy.move(int(q)))
        
        
        
        
