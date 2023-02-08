import pandas as pd


######################################
def perp_dist(x1, x2, x3, y1, y2, y3):
  '''
  This function returns the perpendicular distance from a point to a line segment.
    
  (x1,y1) and (x2,y2) define the start and end points of your line.
  (x3, y3) defines a point.
  '''
  if x2==x1:
    return abs(x3-x1)
  m = (y2-y1)/(x2-x1)
  c = y1-m*x1
  d = abs(m*x3 - y3 + c)/(m**2 + 1)**0.5
  return d

def max_point(start,last):
  for i in range(last - start):
    d = perp_dist(data("lon",start),data("lon",i),data("lon",last),data("lat",start),data("lat",i),data("lat",last))
    final_d = 0
    mid = 0
    if final_d < d:
      final_d = d
      mid  = i
      max_point1 = [final_d, mid]
  return max_point1


def Douglas_Peucker(start,last,tol):
    d = max_point(start,last)[0]
    mid = max_point(start,last)[1]
    final_line = []
    if (d < tol):
        line = data[data[0,start],data[1,start]],data[data[0,last],data[1,last]]
        final_line.append(line)
    if (d > tol):
        Douglas_Peucker(start,mid,tol)
        Douglas_Peucker(mid,last,tol)
    return line

if __name__=="__main__":
  '''Main block'''
  # relative path to filename from OOSA-code-public folder
  filename='/home/s2440667/oosa/squirrel_ordered.txt'

  # read data in to RAM
  data=pd.read_csv(filename, sep = "\000")

  # sort by the time column
  #sortedData=data.sort_values('time').reset_index(drop=True)
  print(max_point(1,5))
  #print(Douglas_Peucker(0,10,5))
  