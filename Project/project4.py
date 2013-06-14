#George Jing
#3-D Pattern Recognition
"""For this project, you will construct a 3D hexagonal geometry edge finding algorithm that
can combine individual voxels from NIFFTE events fission into connected trajectories.
Once the trajectories have been determined, you will produce a 3D visualization of the
events using Matplotlib's mplot3d, with the different trajectories color-coded. You will
also keep track of how many tracks are found per event, how many voxels go unused or
unconnected to a trajectory and generate histograms of these variables to quantify the
performance of your algorithm"""

import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class Voxel:
    """A class to store the parameters of each voxel and calculate the gradient. Takes in a String parameter and parses it"""
    def __init__(self, data):
        self.volume = float(data.split(' ')[0])
        self.row = float(data.split(' ')[1])
        self.column = float(data.split(' ')[2])
        self.bucket = float(data.split(' ')[3])
        self.ADC = float(data.split(' ')[4])
    def setGradient(self, other):
        self.gradient = (other.ADC-self.ADC)

class Event:
    """A class to manipulate a list of Voxels"""
    def __init__(self, data):
        self.data = sorted(data, key=lambda Voxel: Voxel.ADC)[::-1]
        self.pool = self.data
        self.tracks = []
    def rawGraph(self):
        """graphs all the points in the event"""
        fig = figure()
        ax = fig.gca(projection='3d')
        eventRow = []
        eventCol = []
        eventBuc = []
        for voxel in self.data:
            eventRow.append(voxel.row)
            eventCol.append(voxel.column)
            eventBuc.append(voxel.bucket)
        p = ax.scatter(eventRow,eventCol,eventBuc)
        ax.set_xlabel('Event Row')
        ax.set_ylabel('Event Column')
        ax.set_zlabel('Event Bucket')
    def rawTracks(self, cutoff):
        """sets the tracks and orphans. It adds voxels to an array until it longer meets the gradient cutoff, then it adds that array to the tracks array
            then repeates with what is left until all the voxels are in an array in the tracks array."""
        self.tracks = []
        t = []
        v = self.pool[0]
        for vox in self.pool:
            vox.setGradient(v)
            v = vox
            if vox.gradient<cutoff:
                t.append(vox)
                self.pool.remove(vox)
            else:
                self.tracks.append(t)
                t = []
    def graphEvent(self, cutoff, orphans):
		"""graphs the tracks and orphans, also sets the number of orphans and tracks doesn't work properly"""
        self.orphans = 0
        self.trackNum = 0
        self.rawTracks(cutoff)
        fig = figure()
        ax = fig.gca(projection='3d')
        eventPoolRow = []
        eventPoolCol = []
        eventPoolBuc = []
        for t in self.tracks:
            if len(t)<3:
                for voxel in t:
                    eventPoolRow.append(voxel.row)
                    eventPoolCol.append(voxel.column)
                    eventPoolBuc.append(voxel.bucket)
                    self.orphans+=1
            else:
                self.trackNum +=1
                eventR = []
                eventC = []
                eventB = []
                for vox in t:
                    eventR.append(vox.row)
                    eventC.append(vox.column)
                    eventB.append(vox.bucket)
                ax.scatter(eventR,eventC,eventB, marker='.', s=10, color=numpy.random.rand(3,1))
        if orphans == True:
            ax.scatter(eventPoolRow,eventPoolCol,eventPoolBuc, marker='v', s=10, color=numpy.random.rand(3,1))
        ax.set_xlabel('Row')
        ax.set_ylabel('Column')
        ax.set_zlabel('Bucket')
        plt.show()

def project4(cutoff, orphans):
    """All the events are graphed and stores the number of tracks and orphans per event in the event objects,
        then graphs 2 bar graphs, one for the number of tracks per event and one for the number of orphans per event"""
    niffte = open("niffte_data.txt", 'r')
    line = niffte.readline()
    line = niffte.readline()
    events = []
    for i in range(0,100):
        arr = []
        boolean = True
        while boolean:
            if line == '' or "#### Event " in line:
                events.append(Event(arr))
                boolean = False
            else:
                arr.append(Voxel(line))
            line = niffte.readline()
    niffte.close()
    orphans = []
    tracks = []
    x = list(xrange(100))
    for event in events:
        event.graphEvent(cutoff,orphans)
        orphans.append(event.orphans)
        tracks.append(event.trackNum)
    subplot(3,1,3)
    bar(x,orphans)
    title('Orphans')
    xlabel('Event')
    ylabel('Orphans')
    subplot(2,1,1)
    bar(x,tracks, color='red')
    title('Tracks')
    xlabel('Event')
    ylabel('Tracks')

orphans = input("Show Orphans (True/False): ");
cutoff = input("Enter a cutoff value: ");
project4(cutoff,orphans)

"""
How does your result depend on the cutoff value for the gradient?
The number of tracks and orphans increases as the cutoff value decreases

What additional tricks or tests could you add to your program to improve the efficiency?
Probably some way of getting the number of tracks of each event without having to calculate everything first.
"""

"""
References used: The Python and matplotlib documentation
"""