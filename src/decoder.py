from distutils.command.config import config
import string
from NSFopen.read import read as afmreader
import matplotlib.pyplot as plt
import numpy as np
import sys

class Config:
  dirpath = "/home/private/repos/afm-reader/"
  resultPath = "/home/private/repos/afm-reader/results/"
  dataConfig = {
      "bias": [('Spec', 'Backward', 'Sample_Bias'), ('Spec', 'Forward', 'Sample_Bias')],
      "amplitude": [('Spec', 'Backward', '2nd Lock-In Amplitude'), ('Spec', 'Forward', '2nd Lock-In Amplitude')],
      "phase": [('Spec', 'Backward', '2nd Lock-In Phase'), ('Spec', 'Forward', '2nd Lock-In Phase')]
  }
  files = ["bias", "amplitude", "phase"]
  plots = [("bias", "-", "amplitude", "pN"), ("bias", "-", "phase", "deg")]
config = Config()
#def checkConfig if dirpath and resultpath exist

def decodeAFM(path):
    return afmreader(path, verbose=False).data

def getDataFromDecoded(decoded, dataConfig: dict) -> dict:
  data = {}

  for key, value in dataConfig.items():
    arr = None
    i = 0
    for keys in value:
      try: 
        d = decoded[keys[0]][keys[1]][keys[2]]
        if i == 0:
          arr = d
        else:
          arr = np.concatenate((arr, d), axis=1)
      except: 
        raise NameError('!!! Config error !!!')
      i += 1
    data[key] = arr  
  return data

def saveFile(name: string, data: dict, dataName: dict):
  savePath = config.resultPath+name.split('.')[0]+'-'+dataName+'.csv'
  np.savetxt(savePath, data, fmt='%s', delimiter=",")

def plot(name, x, y, nameX, unitX, nameY, unitY, xlim = None, ylim = None):
  for i in range(len(y)):
      plt.plot(x[i], y[i])

  if xlim != None:
      plt.xlim(xlim)
  if ylim != None:
      plt.ylim(ylim)

  plt.xlabel(nameX + ' ['+ unitX +']')
  plt.ylabel(nameY + ' ['+ unitY +']')

  savePath = config.resultPath+name.split('.')[0]+'-plot-'+nameX+'-'+ nameY+'.png'

  fig = plt.gcf()
  fig.savefig(savePath, dpi=300)
  plt.show()

if __name__ == "__main__":
    file = sys.argv[1]
    fileName = file.split('/')[-1].split('.')[0]
    
    decoded = decodeAFM(file)
    data = getDataFromDecoded(decoded, config.dataConfig)

    for f in config.files:
      try:
        saveFile(fileName, data[f], f)
      except:
        raise NameError('!!! Config error !!!')

    for p in config.plots:
      try:
        plot(fileName,data[p[0]], data[p[2]], p[0], p[1], p[2], p[3])
      except:
        raise NameError('!!! Config error !!!')


