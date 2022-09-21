import matplotlib.pyplot as plt
import numpy as np


def saveFile(outputPrefix, data, dataName):
  savePath = outputPrefix+'-'+dataName+'.csv'
  np.savetxt(savePath, data, fmt='%s', delimiter=",")

def plot(outputPrefix, x, y, nameX, unitX, nameY, unitY,  outputPath, xlim = None, ylim = None):
  for i in range(len(y)):
      plt.plot(x[i], y[i])

  if xlim != None:
      plt.xlim(xlim)
  if ylim != None:
      plt.ylim(ylim)

  plt.xlabel(nameX + ' ['+ unitX +']')
  plt.ylabel(nameY + ' ['+ unitY +']')

  savePath = outputPrefix+'-plot-'+nameX+'-'+ nameY+'.png'

  fig = plt.gcf()
  fig.savefig(savePath, dpi=300)
  plt.show()

