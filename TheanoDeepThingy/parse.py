
class experiment():
    def __init__(self,frames):
        self.frames = frames
        carsIn = {}
        carsOrder = []
        self.gaps = []

        for frame in frames:
            pos = [9.930516, 22.94445, -0.04681887]
            for car in frame.getCars():
                if car.getId() not in carsIn:
                    carPos = car.getPos()
                    dist = (pos[0]-carPos[0]) *(pos[0]-carPos[0]) + (pos[1]-carPos[1])*(pos[1]-carPos[1])
                    if(dist<1):
                        carsIn[car.getId()]= frame.getTime()
                        carsOrder.append(car.getId())


        for a in range(1,len(carsOrder)):
            self.gaps.append(carsIn[carsOrder[a]]-carsIn[carsOrder[a-1]])

    def getFrames(self):
        return self.frames

    def getGaps(self):
        return self.gaps


class frame():
    def __init__(self, time):
        self.time = time
        self.cars = []

    def getTime(self):
        return self.time

    def defPed(self,ped):
        self.ped = ped

    def getPed(self):
        return self.ped

    def addCar(self,car):
        self.cars.append(car)

    def getCars(self):
        return self.cars


class pedData():
    def __init__(self,data ):
        self.data = data
        dataSplit = data.split(',')
        self.pos = [float(dataSplit[1]),float(dataSplit[2]),float(dataSplit[3])]
        self.facing = [float(dataSplit[4]),float(dataSplit[5]),float(dataSplit[6])]
        if len(dataSplit)>= 8:
            self.angle = dataSplit[7]
            self.mazeSolved = dataSplit[8]
        else:
            self.angle = None
            self.mazeSolved = None

    def getPos(self):
        return self.pos

    def getForward(self):
        return self.facing

    def getAnglePhone(self):
        return self.angle

    def getNbMazeSolved(self):
        return self.mazeSolved

class carData():
    def __init__(self,data):
        self.data = list(data)
        dataSplit = data[0].split(',')
        self.id = int(dataSplit[0])
        self.pos = [float(dataSplit[1]),float(dataSplit[2]),float(dataSplit[3])]
        self.facing = [float(dataSplit[4]),float(dataSplit[5]),float(dataSplit[6])]
        self.speed = float(dataSplit[7])

        self.points = []

        for i in range(4):
            dataSplit = data[i+1].split(',')
            self.points.append([float(dataSplit[0]),float(dataSplit[1]),float(dataSplit[2])])

    def getId(self):
        return self.id

    def getPos(self):
        return self.pos

    def getForward(self):
        return self.facing

    #km/h
    def getSpeed(self):
        return self.speed

    def getPoints(self):
        return self.points



def parse(path):
    f= open(path, 'r')
    text = f.read()
    frameSplit = text.split("\n")
    started = False
    frames = []
    carDataAccumulator = []
    lineAccumulated = 0
    for line in frameSplit:
        if len(line) < 2:
            started = False
        elif started is False:
            currentFrame = frame(float(line))
            started = True
            frames.append(currentFrame)
        else:
            if(line[0]=='u'):
                currentFrame.defPed(pedData(line))
            else:
                carDataAccumulator.append(line)
                lineAccumulated+=1
                if lineAccumulated==5:
                    lineAccumulated = 0
                    currentFrame.addCar(carData(carDataAccumulator))
                    del carDataAccumulator[:]

    return experiment(frames)

parse("./20170301170223PLS0.txt")