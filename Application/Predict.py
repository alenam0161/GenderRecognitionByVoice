import subprocess
import pandas as pd
import xgboost as xgb
from spafe.features.spfeats import extract_feats
import librosa
import numpy as np
from scipy import stats

#subprocess.call ("/usr/bin/Rscript --vanilla /home/prathamsolanki/github/gender-recognition-by-voice/Application/ExtractFeatures.R", shell=True)

features_to_use = ["meanfreq","sd","median","Q25","Q75","IQR","skew","kurt","sp.ent","sfm","mode","centroid","meanfun","minfun","maxfun","meandom","mindom","maxdom","dfrange","modindx"]

list_of_data = []

sample, sample_rate = librosa.load('Data/brian.wav')
sample_rate = 22000
smp = extract_feats(sample,sample_rate)
names = list(smp.keys())
list_of_data.append(list(smp.values())) 

def transform():
    for indx in range(len(list_of_data)):
        lst = []
        for each in list_of_data[indx]:
            if type(each) == list or type(each) ==np.ndarray:
                if(len(each) == 0):
                    continue
                else:
                    lst.append(np.max(each))
                    lst.append(np.min(each))
                    lst.append(np.mean(each))
                    lst.append(np.argmax(each))
                    lst.append(np.argmin(each))
                    lst.append(int(stats.mode(each).mode))
                    continue
            if type(each) == tuple:
                rl,bl = each
                each = rl
                
            if type(each) == np.complex128:
                each = each.real
                
            lst.append(each)
        list_of_data[indx] = lst
transform()
transform()

test_X = pd.DataFrame(data = list_of_data)
xgtest = xgb.DMatrix(test_X)

model = xgb.Booster({'nthread':4})
model.load_model("Application/voice-gender.model")

pred_test_y = model.predict(xgtest)

pred_test_y
if pred_test_y >= 0.5:
    print("Male")

else:
    print("Female")
