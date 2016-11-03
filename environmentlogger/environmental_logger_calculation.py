import numpy as np

__all__ = ["AREA", "FLX_SNS", "calculateDownwellingSpectralFlux"]

#Fibre optic collection surface area is pi * (fiber diameter squared) / 4
AREA = np.pi * (3900.0 * 1.0e-6) ** 2 / 4.0  # [m2]

# flx_sns@provenance="EnvironmentalLogger calibration information from file S05673_08062015.IrradCal provided by TinoDornbusch and discussed here: https://github.com/terraref/reference-data/issues/30#issuecomment-217518434";
#_FLX_SNS comment: [uJ cnt-1] 10 sensitivities per line, 1024 total
FLX_SNS = \
    [2.14905162e-3, 2.14905162e-3, 2.13191329e-3, 2.09958721e-3, 2.07255014e-3, 2.04042869e-3, 2.01065201e-3, 1.98247712e-3, 1.95695595e-3, 1.93084270e-3,
     1.90570597e-3, 1.87482001e-3, 1.85556117e-3, 1.83111292e-3, 1.80493827e-3, 1.78204243e-3, 1.76011709e-3, 1.74298970e-3, 1.72493868e-3, 1.70343113e-3,
     1.68553722e-3, 1.66631622e-3, 1.65443041e-3, 1.63642311e-3, 1.61846215e-3, 1.60545573e-3, 1.59131286e-3, 1.57713520e-3, 1.56105571e-3, 1.54524417e-3,
     1.53346351e-3, 1.51857527e-3, 1.50523348e-3, 1.49241475e-3, 1.47961893e-3, 1.46809459e-3, 1.45371019e-3, 1.44115770e-3, 1.42656173e-3, 1.41449893e-3,
     1.40218325e-3, 1.38727829e-3, 1.37516400e-3, 1.36250816e-3, 1.34930545e-3, 1.33658553e-3, 1.32360948e-3, 1.31037104e-3, 1.29485640e-3, 1.28218362e-3,
     1.26643446e-3, 1.25134745e-3, 1.23774104e-3, 1.22154062e-3, 1.20610594e-3, 1.19103569e-3, 1.17634593e-3, 1.16196432e-3, 1.14706609e-3, 1.13382928e-3,
     1.11918389e-3, 1.10556178e-3, 1.09188557e-3, 1.07918790e-3, 1.06742601e-3, 1.05718118e-3, 1.04694473e-3, 1.03659582e-3, 1.02873900e-3, 1.02288609e-3,
     1.01628109e-3, 1.01158157e-3, 1.00762812e-3, 1.00491506e-3, 9.99889414e-4, 9.95638736e-4, 9.91223764e-4, 9.86536043e-4, 9.82378851e-4, 9.75992983e-4,
     9.68055921e-4, 9.60360601e-4, 9.52229616e-4, 9.44288731e-4, 9.35551583e-4, 9.27778978e-4, 9.19234295e-4, 9.10434775e-4, 9.02072493e-4, 8.94082691e-4,
     8.86054070e-4, 8.80176269e-4, 8.73884929e-4, 8.67741565e-4, 8.61294713e-4, 8.55225782e-4, 8.50034434e-4, 8.44592095e-4, 8.39026291e-4, 8.32991645e-4,
     8.27232672e-4, 8.20422797e-4, 8.12627476e-4, 8.03944155e-4, 7.93686106e-4, 7.82697718e-4, 7.71489658e-4, 7.58484857e-4, 7.47988099e-4, 7.37636214e-4,
     7.28366631e-4, 7.19162810e-4, 7.11125553e-4, 7.03209565e-4, 6.94909585e-4, 6.86758690e-4, 6.78942712e-4, 6.70144668e-4, 6.62797996e-4, 6.54343779e-4,
     6.46170305e-4, 6.38872127e-4, 6.30959379e-4, 6.25264821e-4, 6.19260059e-4, 6.14223740e-4, 6.09600378e-4, 6.04109797e-4, 5.99684341e-4, 5.94762462e-4,
     5.89358438e-4, 5.84542583e-4, 5.79374467e-4, 5.76250247e-4, 5.72012513e-4, 5.68631187e-4, 5.65821491e-4, 5.62718648e-4, 5.59116033e-4, 5.55411029e-4,
     5.51801247e-4, 5.47598043e-4, 5.43247327e-4, 5.37762461e-4, 5.33460619e-4, 5.28878572e-4, 5.23689536e-4, 5.19266009e-4, 5.14458405e-4, 5.10751276e-4,
     5.07003427e-4, 5.03165882e-4, 4.98966826e-4, 4.96001001e-4, 4.93715941e-4, 4.90249980e-4, 4.86771807e-4, 4.83624709e-4, 4.80476687e-4, 4.76929878e-4,
     4.74001018e-4, 4.70608674e-4, 4.66770209e-4, 4.64581056e-4, 4.61759438e-4, 4.59189259e-4, 4.57332260e-4, 4.55348303e-4, 4.53789335e-4, 4.51997104e-4,
     4.51229308e-4, 4.49813718e-4, 4.49043888e-4, 4.48243809e-4, 4.47227105e-4, 4.45901662e-4, 4.44320515e-4, 4.42138136e-4, 4.40911947e-4, 4.38857020e-4,
     4.36114912e-4, 4.32791420e-4, 4.29184734e-4, 4.26039764e-4, 4.23760025e-4, 4.20638491e-4, 4.17739943e-4, 4.15334137e-4, 4.13241033e-4, 4.10672248e-4,
     4.08480950e-4, 4.07521131e-4, 4.06620556e-4, 4.05633162e-4, 4.04394743e-4, 4.02768826e-4, 4.01579752e-4, 4.00290096e-4, 3.98392706e-4, 3.96699174e-4,
     3.94234388e-4, 3.91851912e-4, 3.89154416e-4, 3.86231981e-4, 3.83777232e-4, 3.81168698e-4, 3.78433645e-4, 3.76298344e-4, 3.74215227e-4, 3.72197441e-4,
     3.70207284e-4, 3.68657365e-4, 3.67545261e-4, 3.66319403e-4, 3.65206679e-4, 3.63557693e-4, 3.62294538e-4, 3.61179418e-4, 3.58947889e-4, 3.56599608e-4,
     3.53923148e-4, 3.51224187e-4, 3.48070600e-4, 3.44364936e-4, 3.40781769e-4, 3.37471420e-4, 3.33912295e-4, 3.30235172e-4, 3.26561393e-4, 3.23282422e-4,
     3.20050433e-4, 3.17180477e-4, 3.14219227e-4, 3.11600742e-4, 3.09493381e-4, 3.07471257e-4, 3.05484183e-4, 3.03684277e-4, 3.01998980e-4, 3.00340107e-4,
     2.98343918e-4, 2.96867620e-4, 2.94945050e-4, 2.93219375e-4, 2.91688135e-4, 2.89922856e-4, 2.87800025e-4, 2.85461354e-4, 2.83757039e-4, 2.81377961e-4,
     2.79552629e-4, 2.77642310e-4, 2.75503391e-4, 2.73875335e-4, 2.72347155e-4, 2.70900748e-4, 2.69293738e-4, 2.67858074e-4, 2.66460300e-4, 2.65251110e-4,
     2.64275292e-4, 2.63248240e-4, 2.62327379e-4, 2.61579696e-4, 2.60818456e-4, 2.60002965e-4, 2.58705340e-4, 2.57752670e-4, 2.56913992e-4, 2.56361785e-4,
     2.55265269e-4, 2.54289030e-4, 2.53369783e-4, 2.52709129e-4, 2.51737103e-4, 2.50397300e-4, 2.48911620e-4, 2.47940106e-4, 2.46958831e-4, 2.46000402e-4,
     2.44657610e-4, 2.42959871e-4, 2.41646677e-4, 2.40071179e-4, 2.38572274e-4, 2.37125904e-4, 2.35921992e-4, 2.34980504e-4, 2.34028683e-4, 2.32572352e-4,
     2.31160035e-4, 2.29885626e-4, 2.28995291e-4, 2.28016467e-4, 2.26725040e-4, 2.25484801e-4, 2.23893466e-4, 2.22942513e-4, 2.21397987e-4, 2.19729430e-4,
     2.18184785e-4, 2.16237560e-4, 2.14867776e-4, 2.13119570e-4, 2.11095792e-4, 2.09431424e-4, 2.07369328e-4, 2.05197478e-4, 2.02992714e-4, 2.00995783e-4,
     1.99040628e-4, 1.97330365e-4, 1.95128937e-4, 1.92897050e-4, 1.90828812e-4, 1.88848992e-4, 1.86812770e-4, 1.85107403e-4, 1.83851878e-4, 1.81970227e-4,
     1.80471463e-4, 1.78981517e-4, 1.77286120e-4, 1.76392581e-4, 1.75098596e-4, 1.74137351e-4, 1.73190515e-4, 1.72166132e-4, 1.71231374e-4, 1.70366007e-4,
     1.69568760e-4, 1.68589267e-4, 1.67791363e-4, 1.66897578e-4, 1.65888439e-4, 1.65083935e-4, 1.64157795e-4, 1.63088458e-4, 1.62054638e-4, 1.60921204e-4,
     1.59597998e-4, 1.58591166e-4, 1.57448762e-4, 1.55975979e-4, 1.54945634e-4, 1.53768607e-4, 1.52490862e-4, 1.51237859e-4, 1.50099128e-4, 1.49111429e-4,
     1.47998498e-4, 1.47145525e-4, 1.46192385e-4, 1.45307609e-4, 1.44594903e-4, 1.43689016e-4, 1.42978840e-4, 1.42385947e-4, 1.41618642e-4, 1.41296459e-4,
     1.40736609e-4, 1.40128598e-4, 1.39496377e-4, 1.38800776e-4, 1.38248154e-4, 1.37619848e-4, 1.37121202e-4, 1.36531523e-4, 1.35719098e-4, 1.35125606e-4,
     1.34189288e-4, 1.33450058e-4, 1.32766920e-4, 1.31885017e-4, 1.31122573e-4, 1.30328488e-4, 1.29426836e-4, 1.28660144e-4, 1.27935543e-4, 1.27252022e-4,
     1.26480762e-4, 1.25668248e-4, 1.24922118e-4, 1.24410907e-4, 1.23808009e-4, 1.23163911e-4, 1.22517652e-4, 1.21996101e-4, 1.21426745e-4, 1.20795188e-4,
     1.20351946e-4, 1.19824156e-4, 1.19435754e-4, 1.19034938e-4, 1.18434743e-4, 1.18058836e-4, 1.17753346e-4, 1.17341202e-4, 1.17001634e-4, 1.16538566e-4,
     1.16315189e-4, 1.16025052e-4, 1.15877025e-4, 1.15561180e-4, 1.15133517e-4, 1.14836326e-4, 1.14582204e-4, 1.14243860e-4, 1.14197033e-4, 1.13911263e-4,
     1.13780203e-4, 1.13241434e-4, 1.12847757e-4, 1.12518590e-4, 1.12240191e-4, 1.12090644e-4, 1.11898539e-4, 1.11697770e-4, 1.11478439e-4, 1.11055915e-4,
     1.11038903e-4, 1.10892821e-4, 1.10844792e-4, 1.10832493e-4, 1.10685454e-4, 1.10585787e-4, 1.10523459e-4, 1.10538204e-4, 1.10352101e-4, 1.10342922e-4,
     1.10281513e-4, 1.10136790e-4, 1.10034253e-4, 1.10161106e-4, 1.10100572e-4, 1.10110098e-4, 1.10080592e-4, 1.09984173e-4, 1.09845052e-4, 1.09851854e-4,
     1.09905915e-4, 1.10028217e-4, 1.10035987e-4, 1.09960749e-4, 1.09766410e-4, 1.09785602e-4, 1.09799006e-4, 1.09935387e-4, 1.09996957e-4, 1.10015594e-4,
     1.09970966e-4, 1.09805155e-4, 1.09719944e-4, 1.09678392e-4, 1.09725399e-4, 1.09808313e-4, 1.09636200e-4, 1.09535133e-4, 1.09295215e-4, 1.09169349e-4,
     1.09191375e-4, 1.09233527e-4, 1.09205113e-4, 1.09120552e-4, 1.09119671e-4, 1.08973612e-4, 1.08924114e-4, 1.08891026e-4, 1.08907229e-4, 1.08986240e-4,
     1.08900531e-4, 1.08753082e-4, 1.08703896e-4, 1.08787039e-4, 1.08795093e-4, 1.08699656e-4, 1.08837754e-4, 1.08804051e-4, 1.08825203e-4, 1.08836245e-4,
     1.08750606e-4, 1.08911309e-4, 1.08993157e-4, 1.09019453e-4, 1.08906882e-4, 1.08830389e-4, 1.08786024e-4, 1.08648784e-4, 1.08543831e-4, 1.08526696e-4,
     1.08346842e-4, 1.08177325e-4, 1.07894351e-4, 1.07585013e-4, 1.07355722e-4, 1.07161797e-4, 1.07018269e-4, 1.06701081e-4, 1.06490135e-4, 1.06148921e-4,
     1.05780669e-4, 1.05519970e-4, 1.05237804e-4, 1.05018149e-4, 1.04960672e-4, 1.04759539e-4, 1.04540409e-4, 1.04335532e-4, 1.04248329e-4, 1.04080729e-4,
     1.04091425e-4, 1.04055083e-4, 1.04023531e-4, 1.03982955e-4, 1.03897792e-4, 1.03664565e-4, 1.03597003e-4, 1.03534202e-4, 1.03538706e-4, 1.03610086e-4,
     1.03562393e-4, 1.03382849e-4, 1.03208570e-4, 1.03080933e-4, 1.03024256e-4, 1.03051061e-4, 1.03046453e-4, 1.02968720e-4, 1.02813488e-4, 1.02603014e-4,
     1.02234419e-4, 1.02028022e-4, 1.01905582e-4, 1.01804529e-4, 1.01678913e-4, 1.01525915e-4, 1.01235735e-4, 1.01002510e-4, 1.00753430e-4, 1.00514078e-4,
     1.00437680e-4, 1.00426425e-4, 1.00342652e-4, 1.00324563e-4, 1.00193735e-4, 9.99614188e-5, 9.97959450e-5, 9.96635685e-5, 9.95680633e-5, 9.95295601e-5,
     9.95419478e-5, 9.93610409e-5, 9.92005015e-5, 9.89874238e-5, 9.87621992e-5, 9.86741797e-5, 9.86446806e-5, 9.87023188e-5, 9.86904988e-5, 9.87196887e-5,
     9.86048564e-5, 9.84391907e-5, 9.83676057e-5, 9.83207848e-5, 9.84386405e-5, 9.84955583e-5, 9.85247638e-5, 9.85229229e-5, 9.84406010e-5, 9.83803668e-5,
     9.83439478e-5, 9.83296520e-5, 9.84439321e-5, 9.85235870e-5, 9.85655663e-5, 9.84966496e-5, 9.84488197e-5, 9.84056559e-5, 9.83206327e-5, 9.81939782e-5,
     9.83002829e-5, 9.82246562e-5, 9.82700124e-5, 9.83010388e-5, 9.82759501e-5, 9.81680327e-5, 9.80868465e-5, 9.80081521e-5, 9.80084773e-5, 9.80201149e-5,
     9.81387400e-5, 9.80116911e-5, 9.80144351e-5, 9.79589533e-5, 9.78046061e-5, 9.76346492e-5, 9.76720556e-5, 9.76000615e-5, 9.76940237e-5, 9.76700649e-5,
     9.76436554e-5, 9.76217315e-5, 9.75644547e-5, 9.74582521e-5, 9.73723677e-5, 9.75158846e-5, 9.76063227e-5, 9.76576561e-5, 9.78378613e-5, 9.78764318e-5,
     9.78355668e-5, 9.79053556e-5, 9.78971200e-5, 9.79906854e-5, 9.80966670e-5, 9.83212609e-5, 9.83661316e-5, 9.85426549e-5, 9.86024674e-5, 9.86590075e-5,
     9.86276988e-5, 9.87354712e-5, 9.87754605e-5, 9.89135932e-5, 9.91850242e-5, 9.94027993e-5, 9.94630471e-5, 9.95331627e-5, 9.95927355e-5, 9.96449255e-5,
     9.96738155e-5, 9.97903713e-5, 9.99867011e-5, 1.00180641e-4, 1.00305263e-4, 1.00350675e-4, 1.00337790e-4, 1.00368296e-4, 1.00386643e-4, 1.00381686e-4,
     1.00519126e-4, 1.00708351e-4, 1.00900376e-4, 1.00985285e-4, 1.01155946e-4, 1.01232434e-4, 1.01246029e-4, 1.01294137e-4, 1.01423141e-4, 1.01638838e-4,
     1.01812099e-4, 1.01937894e-4, 1.02167422e-4, 1.02253729e-4, 1.02424793e-4, 1.02521930e-4, 1.02690121e-4, 1.02839311e-4, 1.03089113e-4, 1.03250475e-4,
     1.03431580e-4, 1.03716033e-4, 1.03938607e-4, 1.04117939e-4, 1.04384106e-4, 1.04529677e-4, 1.04654582e-4, 1.04814310e-4, 1.05092692e-4, 1.05413737e-4,
     1.05740355e-4, 1.06083661e-4, 1.06308365e-4, 1.06565438e-4, 1.06629335e-4, 1.06744210e-4, 1.06882442e-4, 1.07187881e-4, 1.07381175e-4, 1.07571985e-4,
     1.07752337e-4, 1.07958784e-4, 1.08010861e-4, 1.08075778e-4, 1.08124883e-4, 1.08257449e-4, 1.08419171e-4, 1.08593318e-4, 1.08694174e-4, 1.08884465e-4,
     1.09042040e-4, 1.09206302e-4, 1.09350437e-4, 1.09438760e-4, 1.09607358e-4, 1.09782787e-4, 1.09955758e-4, 1.10091358e-4, 1.10285940e-4, 1.10491229e-4,
     1.10742419e-4, 1.10907433e-4, 1.10989206e-4, 1.10994674e-4, 1.11224947e-4, 1.11275260e-4, 1.11379372e-4, 1.11598462e-4, 1.11899867e-4, 1.12232203e-4,
     1.12446731e-4, 1.12641100e-4, 1.12842223e-4, 1.13075513e-4, 1.13342586e-4, 1.13508149e-4, 1.13820379e-4, 1.14203203e-4, 1.14490663e-4, 1.14760307e-4,
     1.15092754e-4, 1.15469416e-4, 1.15670149e-4, 1.16009156e-4, 1.16271820e-4, 1.16580050e-4, 1.16902429e-4, 1.17308313e-4, 1.17666409e-4, 1.18021025e-4,
     1.18417002e-4, 1.18680029e-4, 1.18865319e-4, 1.19262047e-4, 1.19437496e-4, 1.19686615e-4, 1.19978762e-4, 1.20252739e-4, 1.20473473e-4, 1.20770056e-4,
     1.21090033e-4, 1.21331608e-4, 1.21505469e-4, 1.21699316e-4, 1.21782412e-4, 1.21974020e-4, 1.22103237e-4, 1.22231939e-4, 1.22420471e-4, 1.22581870e-4,
     1.22711136e-4, 1.22866496e-4, 1.22913279e-4, 1.23115711e-4, 1.23199889e-4, 1.23323819e-4, 1.23461205e-4, 1.23642315e-4, 1.23796507e-4, 1.24020468e-4,
     1.24238753e-4, 1.24422114e-4, 1.24625589e-4, 1.24860150e-4, 1.24989076e-4, 1.25232771e-4, 1.25461347e-4, 1.25751417e-4, 1.26039690e-4, 1.26363122e-4,
     1.26586473e-4, 1.26874300e-4, 1.27211480e-4, 1.27449080e-4, 1.27810195e-4, 1.28112243e-4, 1.28496922e-4, 1.28769318e-4, 1.28988874e-4, 1.29308334e-4,
     1.29681533e-4, 1.30081273e-4, 1.30484797e-4, 1.30834377e-4, 1.31195470e-4, 1.31542514e-4, 1.31971306e-4, 1.32327207e-4, 1.32671516e-4, 1.33163904e-4,
     1.33602896e-4, 1.34007504e-4, 1.34403545e-4, 1.34785880e-4, 1.35232311e-4, 1.35920055e-4, 1.36371634e-4, 1.36941354e-4, 1.37497873e-4, 1.38329979e-4,
     1.38981090e-4, 1.39719676e-4, 1.40596483e-4, 1.41573836e-4, 1.42701064e-4, 1.43912407e-4, 1.45127755e-4, 1.46710702e-4, 1.48201619e-4, 1.49963009e-4,
     1.51809861e-4, 1.53750193e-4, 1.55815317e-4, 1.57693897e-4, 1.59629003e-4, 1.61541153e-4, 1.63306339e-4, 1.64888939e-4, 1.66286077e-4, 1.67668695e-4,
     1.68815611e-4, 1.69629768e-4, 1.70307707e-4, 1.70592642e-4, 1.70837390e-4, 1.70905017e-4, 1.70730284e-4, 1.70560321e-4, 1.70279811e-4, 1.69980969e-4,
     1.69683568e-4, 1.69203059e-4, 1.68858534e-4, 1.68509619e-4, 1.68194840e-4, 1.67681333e-4, 1.67199028e-4, 1.66717819e-4, 1.66199767e-4, 1.65735840e-4,
     1.65420369e-4, 1.65032314e-4, 1.64890865e-4, 1.64715724e-4, 1.64497541e-4, 1.64412240e-4, 1.64324793e-4, 1.64276994e-4, 1.64155537e-4, 1.64020542e-4,
     1.64016963e-4, 1.63898890e-4, 1.64032362e-4, 1.64045267e-4, 1.64195414e-4, 1.64285742e-4, 1.64460407e-4, 1.64661763e-4, 1.64738587e-4, 1.64862909e-4,
     1.65076816e-4, 1.65024997e-4, 1.65162453e-4, 1.65237474e-4, 1.65562552e-4, 1.65709225e-4, 1.66142295e-4, 1.66413982e-4, 1.66803643e-4, 1.67161297e-4,
     1.67479188e-4, 1.67667097e-4, 1.67864791e-4, 1.68139958e-4, 1.68233347e-4, 1.68368232e-4, 1.68734109e-4, 1.68895921e-4, 1.69306212e-4, 1.69651966e-4,
     1.69946857e-4, 1.70444809e-4, 1.70732732e-4, 1.71135157e-4, 1.71231516e-4, 1.71550211e-4, 1.71696417e-4, 1.71827084e-4, 1.72142950e-4, 1.72525391e-4,
     1.72856514e-4, 1.73390715e-4, 1.73767822e-4, 1.74328441e-4, 1.74893554e-4, 1.75395641e-4, 1.75742115e-4, 1.76164298e-4, 1.76419331e-4, 1.76746627e-4,
     1.76913681e-4, 1.77372254e-4, 1.77897899e-4, 1.78453513e-4, 1.79169646e-4, 1.79727818e-4, 1.80409802e-4, 1.81135436e-4, 1.81693575e-4, 1.82304987e-4,
     1.82840211e-4, 1.83218701e-4, 1.83686875e-4, 1.84158245e-4, 1.84720710e-4, 1.85261670e-4, 1.86044882e-4, 1.86910627e-4, 1.87744111e-4, 1.88640197e-4,
     1.89536957e-4, 1.90373887e-4, 1.91044376e-4, 1.91770554e-4, 1.92334227e-4, 1.93008156e-4, 1.93752580e-4, 1.94471581e-4, 1.95272205e-4, 1.96159946e-4,
     1.97179878e-4, 1.98147132e-4, 1.99205315e-4, 2.00512171e-4, 2.01401775e-4, 2.02350741e-4, 2.03121965e-4, 2.03880283e-4, 2.04553652e-4, 2.05224749e-4,
     2.05896678e-4, 2.06741041e-4, 2.07620395e-4, 2.08540576e-4, 2.09373829e-4, 2.10385794e-4, 2.11266605e-4, 2.12109107e-4, 2.12682109e-4, 2.13305338e-4,
     2.13902214e-4, 2.14484164e-4, 2.14843762e-4, 2.15242449e-4, 2.15718844e-4, 2.16421684e-4, 2.17195290e-4, 2.18005590e-4, 2.18962077e-4, 2.19991471e-4,
     2.20919919e-4, 2.21546974e-4, 2.22053928e-4, 2.22555080e-4, 2.23237798e-4, 2.23532485e-4, 2.23996613e-4, 2.24501430e-4, 2.25173147e-4, 2.25737767e-4,
     2.26423767e-4, 2.27365037e-4, 2.28449699e-4, 2.29400621e-4, 2.30377333e-4, 2.31057918e-4, 2.31964152e-4, 2.32623742e-4, 2.33166196e-4, 2.33650080e-4,
     2.34105936e-4, 2.34878659e-4, 2.35394209e-4, 2.36099367e-4, 2.37123530e-4, 2.38223666e-4, 2.39309613e-4, 2.40405595e-4, 2.41495657e-4, 2.42458496e-4,
     2.43313474e-4, 2.44175726e-4, 2.44734401e-4, 2.45486851e-4, 2.45993980e-4, 2.46800743e-4, 2.47463201e-4, 2.48445219e-4, 2.49488279e-4, 2.50569021e-4,
     2.51747840e-4, 2.52951109e-4, 2.54188859e-4, 2.55386833e-4, 2.56298369e-4, 2.57479006e-4, 2.58213101e-4, 2.59065147e-4, 2.60018887e-4, 2.61076885e-4,
     2.62283407e-4, 2.63904910e-4, 2.65792030e-4, 2.67956880e-4, 2.70494493e-4, 2.73225853e-4, 2.76170072e-4, 2.79055057e-4, 2.81984548e-4, 2.88500954e-4,
     2.89109910e-4, 2.93129400e-4, 2.92536512e-4, 2.92536512e-4]  # [uJ cnt-1] 10 sensitivities per line, 1024 total

WAVELENGTHS =\
     [3.377048E+02, 3.381601E+02, 3.386155E+02, 3.390709E+02, 3.395263E+02, 3.399818E+02, 3.404373E+02, 3.408929E+02, 3.413485E+02, 3.418041E+02, 
      3.422598E+02, 3.427155E+02, 3.431713E+02, 3.436271E+02, 3.440829E+02, 3.445388E+02, 3.449947E+02, 3.454507E+02, 3.459067E+02, 3.463628E+02, 
      3.468189E+02, 3.472750E+02, 3.477312E+02, 3.481874E+02, 3.486437E+02, 3.491000E+02, 3.495563E+02, 3.500127E+02, 3.504691E+02, 3.509256E+02, 
      3.513821E+02, 3.518387E+02, 3.522953E+02, 3.527519E+02, 3.532086E+02, 3.536653E+02, 3.541221E+02, 3.545789E+02, 3.550357E+02, 3.554926E+02, 
      3.559495E+02, 3.564065E+02, 3.568635E+02, 3.573205E+02, 3.577776E+02, 3.582347E+02, 3.586919E+02, 3.591491E+02, 3.596064E+02, 3.600637E+02, 
      3.605210E+02, 3.609784E+02, 3.614358E+02, 3.618933E+02, 3.623508E+02, 3.628083E+02, 3.632659E+02, 3.637235E+02, 3.641812E+02, 3.646389E+02, 
      3.650966E+02, 3.655544E+02, 3.660123E+02, 3.664701E+02, 3.669281E+02, 3.673860E+02, 3.678440E+02, 3.683020E+02, 3.687601E+02, 3.692182E+02, 
      3.696764E+02, 3.701346E+02, 3.705928E+02, 3.710511E+02, 3.715094E+02, 3.719678E+02, 3.724262E+02, 3.728847E+02, 3.733432E+02, 3.738017E+02, 
      3.742603E+02, 3.747189E+02, 3.751775E+02, 3.756362E+02, 3.760949E+02, 3.765537E+02, 3.770125E+02, 3.774714E+02, 3.779303E+02, 3.783892E+02, 
      3.788482E+02, 3.793072E+02, 3.797663E+02, 3.802254E+02, 3.806845E+02, 3.811437E+02, 3.816030E+02, 3.820622E+02, 3.825215E+02, 3.829809E+02, 
      3.834403E+02, 3.838997E+02, 3.843592E+02, 3.848187E+02, 3.852782E+02, 3.857378E+02, 3.861975E+02, 3.866571E+02, 3.871169E+02, 3.875766E+02, 
      3.880364E+02, 3.884963E+02, 3.889561E+02, 3.894161E+02, 3.898760E+02, 3.903360E+02, 3.907961E+02, 3.912561E+02, 3.917163E+02, 3.921764E+02, 
      3.926366E+02, 3.930969E+02, 3.935572E+02, 3.940175E+02, 3.944779E+02, 3.949383E+02, 3.953987E+02, 3.958592E+02, 3.963198E+02, 3.967803E+02, 
      3.972409E+02, 3.977016E+02, 3.981623E+02, 3.986230E+02, 3.990838E+02, 3.995446E+02, 4.000055E+02, 4.004664E+02, 4.009273E+02, 4.013883E+02, 
      4.018493E+02, 4.023104E+02, 4.027715E+02, 4.032326E+02, 4.036938E+02, 4.041550E+02, 4.046163E+02, 4.050776E+02, 4.055389E+02, 4.060003E+02, 
      4.064617E+02, 4.069232E+02, 4.073847E+02, 4.078463E+02, 4.083079E+02, 4.087695E+02, 4.092311E+02, 4.096929E+02, 4.101546E+02, 4.106164E+02, 
      4.110782E+02, 4.115401E+02, 4.120020E+02, 4.124640E+02, 4.129260E+02, 4.133880E+02, 4.138501E+02, 4.143122E+02, 4.147743E+02, 4.152365E+02, 
      4.156988E+02, 4.161610E+02, 4.166233E+02, 4.170857E+02, 4.175481E+02, 4.180105E+02, 4.184730E+02, 4.189355E+02, 4.193981E+02, 4.198607E+02, 
      4.203233E+02, 4.207860E+02, 4.212487E+02, 4.217115E+02, 4.221743E+02, 4.226371E+02, 4.231000E+02, 4.235629E+02, 4.240259E+02, 4.244889E+02, 
      4.249519E+02, 4.254150E+02, 4.258781E+02, 4.263413E+02, 4.268045E+02, 4.272677E+02, 4.277310E+02, 4.281943E+02, 4.286577E+02, 4.291211E+02, 
      4.295846E+02, 4.300480E+02, 4.305116E+02, 4.309751E+02, 4.314387E+02, 4.319024E+02, 4.323661E+02, 4.328298E+02, 4.332936E+02, 4.337574E+02, 
      4.342212E+02, 4.346851E+02, 4.351490E+02, 4.356130E+02, 4.360770E+02, 4.365410E+02, 4.370051E+02, 4.374693E+02, 4.379334E+02, 4.383976E+02, 
      4.388619E+02, 4.393262E+02, 4.397905E+02, 4.402548E+02, 4.407193E+02, 4.411837E+02, 4.416482E+02, 4.421127E+02, 4.425773E+02, 4.430419E+02, 
      4.435065E+02, 4.439712E+02, 4.444359E+02, 4.449007E+02, 4.453655E+02, 4.458304E+02, 4.462953E+02, 4.467602E+02, 4.472251E+02, 4.476902E+02, 
      4.481552E+02, 4.486203E+02, 4.490854E+02, 4.495506E+02, 4.500158E+02, 4.504810E+02, 4.509463E+02, 4.514116E+02, 4.518770E+02, 4.523424E+02, 
      4.528079E+02, 4.532733E+02, 4.537389E+02, 4.542044E+02, 4.546700E+02, 4.551357E+02, 4.556014E+02, 4.560671E+02, 4.565329E+02, 4.569987E+02, 
      4.574645E+02, 4.579304E+02, 4.583963E+02, 4.588623E+02, 4.593283E+02, 4.597943E+02, 4.602604E+02, 4.607265E+02, 4.611927E+02, 4.616589E+02, 
      4.621251E+02, 4.625914E+02, 4.630577E+02, 4.635241E+02, 4.639905E+02, 4.644569E+02, 4.649234E+02, 4.653899E+02, 4.658565E+02, 4.663231E+02, 
      4.667897E+02, 4.672564E+02, 4.677231E+02, 4.681899E+02, 4.686567E+02, 4.691235E+02, 4.695904E+02, 4.700573E+02, 4.705242E+02, 4.709912E+02, 
      4.714583E+02, 4.719253E+02, 4.723924E+02, 4.728596E+02, 4.733268E+02, 4.737940E+02, 4.742613E+02, 4.747286E+02, 4.751960E+02, 4.756633E+02, 
      4.761308E+02, 4.765982E+02, 4.770657E+02, 4.775333E+02, 4.780009E+02, 4.784685E+02, 4.789362E+02, 4.794039E+02, 4.798716E+02, 4.803394E+02, 
      4.808072E+02, 4.812751E+02, 4.817430E+02, 4.822109E+02, 4.826789E+02, 4.831469E+02, 4.836150E+02, 4.840831E+02, 4.845512E+02, 4.850194E+02, 
      4.854876E+02, 4.859559E+02, 4.864242E+02, 4.868925E+02, 4.873609E+02, 4.878293E+02, 4.882978E+02, 4.887663E+02, 4.892348E+02, 4.897034E+02, 
      4.901720E+02, 4.906406E+02, 4.911093E+02, 4.915780E+02, 4.920468E+02, 4.925156E+02, 4.929845E+02, 4.934533E+02, 4.939223E+02, 4.943912E+02, 
      4.948602E+02, 4.953293E+02, 4.957984E+02, 4.962675E+02, 4.967366E+02, 4.972058E+02, 4.976751E+02, 4.981444E+02, 4.986137E+02, 4.990830E+02, 
      4.995524E+02, 5.000219E+02, 5.004913E+02, 5.009609E+02, 5.014304E+02, 5.019000E+02, 5.023696E+02, 5.028393E+02, 5.033090E+02, 5.037788E+02, 
      5.042485E+02, 5.047184E+02, 5.051882E+02, 5.056581E+02, 5.061281E+02, 5.065981E+02, 5.070681E+02, 5.075381E+02, 5.080082E+02, 5.084784E+02, 
      5.089486E+02, 5.094188E+02, 5.098890E+02, 5.103593E+02, 5.108297E+02, 5.113000E+02, 5.117704E+02, 5.122409E+02, 5.127114E+02, 5.131819E+02, 
      5.136525E+02, 5.141231E+02, 5.145937E+02, 5.150644E+02, 5.155351E+02, 5.160059E+02, 5.164767E+02, 5.169475E+02, 5.174184E+02, 5.178893E+02, 
      5.183603E+02, 5.188313E+02, 5.193023E+02, 5.197734E+02, 5.202445E+02, 5.207156E+02, 5.211868E+02, 5.216581E+02, 5.221293E+02, 5.226006E+02, 
      5.230720E+02, 5.235434E+02, 5.240148E+02, 5.244862E+02, 5.249577E+02, 5.254293E+02, 5.259009E+02, 5.263725E+02, 5.268441E+02, 5.273158E+02, 
      5.277876E+02, 5.282593E+02, 5.287311E+02, 5.292030E+02, 5.296749E+02, 5.301468E+02, 5.306188E+02, 5.310908E+02, 5.315628E+02, 5.320349E+02, 
      5.325070E+02, 5.329792E+02, 5.334514E+02, 5.339236E+02, 5.343959E+02, 5.348682E+02, 5.353405E+02, 5.358129E+02, 5.362854E+02, 5.367578E+02, 
      5.372303E+02, 5.377029E+02, 5.381755E+02, 5.386481E+02, 5.391207E+02, 5.395934E+02, 5.400662E+02, 5.405390E+02, 5.410118E+02, 5.414846E+02, 
      5.419575E+02, 5.424304E+02, 5.429034E+02, 5.433764E+02, 5.438495E+02, 5.443226E+02, 5.447957E+02, 5.452688E+02, 5.457420E+02, 5.462153E+02, 
      5.466885E+02, 5.471619E+02, 5.476352E+02, 5.481086E+02, 5.485820E+02, 5.490555E+02, 5.495290E+02, 5.500026E+02, 5.504761E+02, 5.509498E+02, 
      5.514234E+02, 5.518971E+02, 5.523709E+02, 5.528446E+02, 5.533185E+02, 5.537923E+02, 5.542662E+02, 5.547401E+02, 5.552141E+02, 5.556881E+02, 
      5.561621E+02, 5.566362E+02, 5.571104E+02, 5.575845E+02, 5.580587E+02, 5.585329E+02, 5.590072E+02, 5.594815E+02, 5.599559E+02, 5.604303E+02, 
      5.609047E+02, 5.613792E+02, 5.618537E+02, 5.623282E+02, 5.628028E+02, 5.632774E+02, 5.637521E+02, 5.642268E+02, 5.647015E+02, 5.651763E+02, 
      5.656511E+02, 5.661259E+02, 5.666008E+02, 5.670757E+02, 5.675507E+02, 5.680257E+02, 5.685007E+02, 5.689758E+02, 5.694509E+02, 5.699261E+02, 
      5.704013E+02, 5.708765E+02, 5.713518E+02, 5.718271E+02, 5.723024E+02, 5.727778E+02, 5.732532E+02, 5.737287E+02, 5.742042E+02, 5.746797E+02, 
      5.751553E+02, 5.756309E+02, 5.761065E+02, 5.765822E+02, 5.770579E+02, 5.775337E+02, 5.780095E+02, 5.784853E+02, 5.789612E+02, 5.794371E+02, 
      5.799131E+02, 5.803891E+02, 5.808651E+02, 5.813412E+02, 5.818173E+02, 5.822934E+02, 5.827696E+02, 5.832458E+02, 5.837221E+02, 5.841984E+02, 
      5.846747E+02, 5.851511E+02, 5.856275E+02, 5.861039E+02, 5.865804E+02, 5.870569E+02, 5.875335E+02, 5.880101E+02, 5.884867E+02, 5.889634E+02, 
      5.894401E+02, 5.899168E+02, 5.903936E+02, 5.908705E+02, 5.913473E+02, 5.918242E+02, 5.923012E+02, 5.927781E+02, 5.932551E+02, 5.937322E+02, 
      5.942093E+02, 5.946864E+02, 5.951636E+02, 5.956408E+02, 5.961180E+02, 5.965953E+02, 5.970726E+02, 5.975500E+02, 5.980273E+02, 5.985048E+02, 
      5.989822E+02, 5.994597E+02, 5.999373E+02, 6.004149E+02, 6.008925E+02, 6.013701E+02, 6.018478E+02, 6.023256E+02, 6.028033E+02, 6.032811E+02, 
      6.037590E+02, 6.042369E+02, 6.047148E+02, 6.051927E+02, 6.056707E+02, 6.061487E+02, 6.066268E+02, 6.071049E+02, 6.075831E+02, 6.080612E+02, 
      6.085395E+02, 6.090177E+02, 6.094960E+02, 6.099743E+02, 6.104527E+02, 6.109311E+02, 6.114096E+02, 6.118880E+02, 6.123666E+02, 6.128451E+02, 
      6.133237E+02, 6.138023E+02, 6.142810E+02, 6.147597E+02, 6.152385E+02, 6.157172E+02, 6.161961E+02, 6.166749E+02, 6.171538E+02, 6.176327E+02, 
      6.181117E+02, 6.185907E+02, 6.190698E+02, 6.195488E+02, 6.200280E+02, 6.205071E+02, 6.209863E+02, 6.214655E+02, 6.219448E+02, 6.224241E+02, 
      6.229035E+02, 6.233828E+02, 6.238623E+02, 6.243417E+02, 6.248212E+02, 6.253007E+02, 6.257803E+02, 6.262599E+02, 6.267395E+02, 6.272192E+02, 
      6.276989E+02, 6.281787E+02, 6.286585E+02, 6.291383E+02, 6.296182E+02, 6.300981E+02, 6.305780E+02, 6.310580E+02, 6.315380E+02, 6.320180E+02, 
      6.324981E+02, 6.329783E+02, 6.334584E+02, 6.339386E+02, 6.344189E+02, 6.348991E+02, 6.353794E+02, 6.358598E+02, 6.363402E+02, 6.368206E+02, 
      6.373011E+02, 6.377816E+02, 6.382621E+02, 6.387427E+02, 6.392233E+02, 6.397039E+02, 6.401846E+02, 6.406653E+02, 6.411461E+02, 6.416269E+02, 
      6.421077E+02, 6.425886E+02, 6.430695E+02, 6.435504E+02, 6.440314E+02, 6.445124E+02, 6.449935E+02, 6.454746E+02, 6.459557E+02, 6.464369E+02, 
      6.469181E+02, 6.473993E+02, 6.478806E+02, 6.483619E+02, 6.488432E+02, 6.493246E+02, 6.498060E+02, 6.502875E+02, 6.507690E+02, 6.512505E+02, 
      6.517321E+02, 6.522137E+02, 6.526954E+02, 6.531770E+02, 6.536588E+02, 6.541405E+02, 6.546223E+02, 6.551041E+02, 6.555860E+02, 6.560679E+02, 
      6.565498E+02, 6.570318E+02, 6.575138E+02, 6.579959E+02, 6.584780E+02, 6.589601E+02, 6.594423E+02, 6.599245E+02, 6.604067E+02, 6.608890E+02, 
      6.613713E+02, 6.618536E+02, 6.623360E+02, 6.628184E+02, 6.633009E+02, 6.637834E+02, 6.642659E+02, 6.647485E+02, 6.652311E+02, 6.657137E+02, 
      6.661964E+02, 6.666791E+02, 6.671619E+02, 6.676446E+02, 6.681275E+02, 6.686103E+02, 6.690932E+02, 6.695762E+02, 6.700591E+02, 6.705421E+02, 
      6.710252E+02, 6.715083E+02, 6.719914E+02, 6.724745E+02, 6.729577E+02, 6.734409E+02, 6.739242E+02, 6.744075E+02, 6.748908E+02, 6.753742E+02, 
      6.758576E+02, 6.763411E+02, 6.768246E+02, 6.773081E+02, 6.777916E+02, 6.782752E+02, 6.787589E+02, 6.792425E+02, 6.797262E+02, 6.802100E+02, 
      6.806937E+02, 6.811775E+02, 6.816614E+02, 6.821453E+02, 6.826292E+02, 6.831132E+02, 6.835972E+02, 6.840812E+02, 6.845653E+02, 6.850494E+02, 
      6.855335E+02, 6.860177E+02, 6.865019E+02, 6.869861E+02, 6.874704E+02, 6.879547E+02, 6.884391E+02, 6.889235E+02, 6.894079E+02, 6.898924E+02, 
      6.903769E+02, 6.908614E+02, 6.913460E+02, 6.918306E+02, 6.923153E+02, 6.928000E+02, 6.932847E+02, 6.937695E+02, 6.942543E+02, 6.947391E+02, 
      6.952240E+02, 6.957089E+02, 6.961938E+02, 6.966788E+02, 6.971638E+02, 6.976488E+02, 6.981339E+02, 6.986190E+02, 6.991042E+02, 6.995894E+02, 
      7.000746E+02, 7.005599E+02, 7.010452E+02, 7.015305E+02, 7.020159E+02, 7.025013E+02, 7.029868E+02, 7.034723E+02, 7.039578E+02, 7.044433E+02, 
      7.049289E+02, 7.054146E+02, 7.059002E+02, 7.063859E+02, 7.068717E+02, 7.073574E+02, 7.078432E+02, 7.083291E+02, 7.088150E+02, 7.093009E+02, 
      7.097868E+02, 7.102728E+02, 7.107589E+02, 7.112449E+02, 7.117310E+02, 7.122172E+02, 7.127033E+02, 7.131895E+02, 7.136758E+02, 7.141621E+02, 
      7.146484E+02, 7.151347E+02, 7.156211E+02, 7.161075E+02, 7.165940E+02, 7.170805E+02, 7.175670E+02, 7.180536E+02, 7.185402E+02, 7.190268E+02, 
      7.195135E+02, 7.200002E+02, 7.204870E+02, 7.209738E+02, 7.214606E+02, 7.219474E+02, 7.224343E+02, 7.229212E+02, 7.234082E+02, 7.238952E+02, 
      7.243822E+02, 7.248693E+02, 7.253564E+02, 7.258436E+02, 7.263307E+02, 7.268180E+02, 7.273052E+02, 7.277925E+02, 7.282798E+02, 7.287672E+02, 
      7.292546E+02, 7.297420E+02, 7.302295E+02, 7.307170E+02, 7.312045E+02, 7.316921E+02, 7.321797E+02, 7.326673E+02, 7.331550E+02, 7.336427E+02, 
      7.341305E+02, 7.346183E+02, 7.351061E+02, 7.355939E+02, 7.360818E+02, 7.365698E+02, 7.370577E+02, 7.375457E+02, 7.380338E+02, 7.385218E+02, 
      7.390100E+02, 7.394981E+02, 7.399863E+02, 7.404745E+02, 7.409627E+02, 7.414510E+02, 7.419394E+02, 7.424277E+02, 7.429161E+02, 7.434045E+02, 
      7.438930E+02, 7.443815E+02, 7.448700E+02, 7.453586E+02, 7.458472E+02, 7.463359E+02, 7.468245E+02, 7.473133E+02, 7.478020E+02, 7.482908E+02, 
      7.487796E+02, 7.492685E+02, 7.497574E+02, 7.502463E+02, 7.507353E+02, 7.512243E+02, 7.517133E+02, 7.522024E+02, 7.526915E+02, 7.531806E+02, 
      7.536698E+02, 7.541590E+02, 7.546482E+02, 7.551375E+02, 7.556268E+02, 7.510000E+02, 7.899669E+02, 7.904587E+02, 7.909505E+02, 7.914424E+02,
      7.919343E+02, 7.924263E+02, 7.929183E+02, 7.934103E+02, 7.939024E+02, 7.943945E+02, 7.948866E+02, 7.953788E+02, 7.958710E+02, 7.963632E+02,
      7.968555E+02, 7.973478E+02, 7.978401E+02, 7.983325E+02, 7.988249E+02, 7.993174E+02, 7.998099E+02, 8.003024E+02, 8.007949E+02, 8.012875E+02,
      8.017801E+02, 8.022728E+02, 8.027655E+02, 8.032582E+02, 8.037510E+02, 8.042438E+02, 8.047366E+02, 8.052295E+02, 8.057224E+02, 8.062153E+02,
      8.067083E+02, 8.072013E+02, 8.076943E+02, 8.081874E+02, 8.086805E+02, 8.091736E+02, 8.096668E+02, 8.101600E+02, 8.106533E+02, 8.111466E+02,
      8.116399E+02, 8.121332E+02, 8.126266E+02, 8.131200E+02, 8.136135E+02, 8.141070E+02, 8.146005E+02, 8.150940E+02, 8.155876E+02, 8.160813E+02,
      8.165749E+02, 8.170686E+02, 8.175624E+02, 8.180561E+02, 8.185499E+02, 8.190438E+02, 8.195376E+02, 8.200315E+02, 8.205255E+02, 8.210195E+02,
      8.215135E+02, 8.220075E+02, 8.225016E+02, 8.229957E+02, 8.234894E+02]

DARK_MEASUREMENTS = \
    [1501, 1500, 1500, 1499, 1499, 1499, 1499, 1502, 1499, 1502, 1501, 1500, 1500, 1499, 1498, 1501, 1500, 1500, 1502, 1502, 1500, 1500, 1501, 1499, 
     1501, 1500, 1500, 1500, 1498, 1499, 1499, 1499, 1500, 1499, 1499, 1500, 1500, 1502, 1501, 1499, 1499, 1498, 1500, 1500, 1499, 1500, 1500, 1499, 
     1500, 1499, 1501, 1500, 1500, 1499, 1499, 1498, 1499, 1498, 1499, 1502, 1500, 1499, 1499, 1500, 1501, 1499, 1501, 1500, 1500, 1498, 1499, 1499, 
     1500, 1499, 1499, 1502, 1500, 1498, 1499, 1499, 1498, 1501, 1500, 1500, 1499, 1499, 1500, 1500, 1500, 1499, 1499, 1499, 1499, 1500, 1498, 1499, 
     1500, 1499, 1500, 1500, 1501, 1500, 1500, 1498, 1499, 1500, 1500, 1500, 1499, 1500, 1499, 1500, 1499, 1500, 1501, 1499, 1500, 1500, 1502, 1499, 
     1500, 1500, 1499, 1500, 1499, 1501, 1500, 1499, 1501, 1499, 1501, 1501, 1500, 1500, 1498, 1500, 1499, 1499, 1499, 1500, 1499, 1500, 1500, 1501, 
     1501, 1502, 1499, 1500, 1499, 1500, 1499, 1499, 1499, 1499, 1501, 1499, 1501, 1501, 1501, 1500, 1499, 1500, 1501, 1499, 1499, 1500, 1501, 1499, 
     1501, 1500, 1499, 1500, 1499, 1500, 1500, 1500, 1500, 1501, 1501, 1498, 1497, 1500, 1500, 1498, 1500, 1499, 1499, 1501, 1498, 1498, 1500, 1500, 
     1499, 1499, 1501, 1501, 1502, 1500, 1500, 1499, 1499, 1500, 1501, 1499, 1497, 1501, 1498, 1500, 1499, 1499, 1499, 1501, 1499, 1500, 1500, 1501, 
     1500, 1501, 1500, 1500, 1500, 1499, 1499, 1499, 1501, 1499, 1500, 1499, 1500, 1498, 1501, 1500, 1501, 1500, 1502, 1500, 1500, 1499, 1500, 1499, 
     1500, 1499, 1500, 1499, 1499, 1500, 1499, 1499, 1500, 1500, 1499, 1499, 1501, 1500, 1500, 1499, 1499, 1498, 1498, 1499, 1499, 1500, 1500, 1500, 
     1499, 1501, 1498, 1499, 1500, 1500, 1501, 1502, 1501, 1499, 1498, 1501, 1501, 1500, 1500, 1500, 1499, 1500, 1499, 1499, 1500, 1501, 1498, 1499, 
     1500, 1501, 1500, 1498, 1499, 1499, 1499, 1497, 1500, 1499, 1500, 1498, 1498, 1501, 1500, 1501, 1499, 1500, 1500, 1501, 1501, 1499, 1500, 1501, 
     1501, 1499, 1499, 1503, 1498, 1500, 1500, 1500, 1499, 1499, 1499, 1500, 1500, 1500, 1499, 1501, 1500, 1500, 1499, 1500, 1499, 1497, 1498, 1501, 
     1498, 1499, 1498, 1499, 1500, 1499, 1497, 1501, 1501, 1498, 1498, 1501, 1501, 1500, 1499, 1500, 1500, 1500, 1499, 1499, 1499, 1501, 1498, 1499, 
     1499, 1499, 1500, 1500, 1501, 1499, 1500, 1500, 1499, 1500, 1500, 1497, 1499, 1500, 1498, 1498, 1501, 1500, 1499, 1498, 1500, 1501, 1499, 1499, 
     1500, 1500, 1498, 1499, 1500, 1499, 1499, 1497, 1497, 1499, 1500, 1501, 1499, 1500, 1498, 1499, 1499, 1501, 1499, 1498, 1500, 1499, 1500, 1501, 
     1499, 1497, 1502, 1500, 1500, 1500, 1501, 1500, 1502, 1499, 1501, 1501, 1499, 1499, 1498, 1498, 1499, 1499, 1498, 1501, 1500, 1500, 1499, 1499, 
     1500, 1499, 1499, 1499, 1500, 1498, 1501, 1498, 1501, 1498, 1498, 1498, 1500, 1499, 1501, 1499, 1499, 1498, 1499, 1498, 1498, 1500, 1498, 1500, 
     1499, 1498, 1499, 1501, 1497, 1498, 1499, 1499, 1499, 1499, 1500, 1499, 1500, 1499, 1500, 1500, 1499, 1498, 1498, 1499, 1500, 1500, 1500, 1500, 
     1499, 1499, 1499, 1499, 1498, 1500, 1500, 1501, 1497, 1498, 1500, 1500, 1499, 1497, 1499, 1501, 1500, 1499, 1498, 1499, 1500, 1499, 1500, 1498, 
     1501, 1500, 1499, 1500, 1499, 1499, 1500, 1500, 1501, 1499, 1499, 1499, 1502, 1500, 1500, 1500, 1499, 1501, 1499, 1498, 1500, 1500, 1500, 1499, 
     1500, 1501, 1499, 1499, 1499, 1499, 1501, 1500, 1500, 1499, 1499, 1500, 1499, 1499, 1500, 1501, 1499, 1500, 1499, 1499, 1498, 1499, 1500, 1500, 
     1500, 1500, 1499, 1501, 1499, 1499, 1499, 1500, 1498, 1501, 1500, 1500, 1499, 1499, 1499, 1499, 1501, 1500, 1500, 1500, 1497, 1500, 1499, 1500, 
     1500, 1499, 1499, 1499, 1499, 1499, 1500, 1501, 1497, 1499, 1498, 1499, 1499, 1499, 1498, 1499, 1499, 1502, 1498, 1501, 1500, 1498, 1500, 1500, 
     1499, 1499, 1499, 1501, 1500, 1498, 1501, 1501, 1500, 1498, 1502, 1499, 1499, 1499, 1499, 1501, 1500, 1498, 1499, 1500, 1499, 1498, 1499, 1499, 
     1499, 1499, 1498, 1499, 1501, 1500, 1498, 1499, 1500, 1501, 1501, 1500, 1497, 1500, 1500, 1499, 1500, 1499, 1498, 1499, 1499, 1500, 1500, 1499, 
     1499, 1500, 1499, 1499, 1499, 1498, 1499, 1500, 1501, 1500, 1498, 1500, 1499, 1500, 1500, 1500, 1500, 1497, 1500, 1498, 1500, 1499, 1498, 1500, 
     1498, 1499, 1500, 1499, 1500, 1499, 1499, 1501, 1499, 1499, 1499, 1501, 1500, 1498, 1499, 1500, 1500, 1499, 1499, 1499, 1500, 1500, 1501, 1499, 
     1499, 1500, 1499, 1500, 1500, 1499, 1498, 1499, 1496, 1500, 1501, 1500, 1499, 1497, 1499, 1500, 1500, 1499, 1499, 1499, 1500, 1500, 1498, 1499, 
     1500, 1500, 1500, 1500, 1500, 1500, 1501, 1499, 1499, 1501, 1500, 1499, 1499, 1499, 1500, 1500, 1498, 1500, 1500, 1498, 1500, 1499, 1498, 1499, 
     1499, 1500, 1500, 1500, 1499, 1500, 1500, 1500, 1499, 1498, 1498, 1500, 1500, 1501, 1499, 1499, 1499, 1501, 1500, 1500, 1500, 1501, 1500, 1499, 
     1499, 1499, 1500, 1500, 1500, 1500, 1501, 1499, 1499, 1500, 1501, 1500, 1498, 1500, 1500, 1501, 1499, 1500, 1499, 1499, 1501, 1499, 1498, 1499, 
     1501, 1499, 1498, 1501, 1500, 1499, 1500, 1499, 1501, 1499, 1498, 1500, 1500, 1501, 1498, 1499, 1503, 1502, 1500, 1500, 1501, 1500, 1498, 1500, 
     1498, 1499, 1501, 1500, 1501, 1498, 1501, 1500, 1502, 1498, 1500, 1500, 1500, 1498, 1498, 1500, 1500, 1499, 1500, 1501, 1500, 1499, 1498, 1500, 
     1499, 1501, 1499, 1499, 1502, 1499, 1501, 1502, 1501, 1501, 1500, 1499, 1500, 1499, 1499, 1499, 1501, 1500, 1501, 1499, 1499, 1499, 1499, 1498, 
     1501, 1501, 1501, 1498, 1500, 1500, 1499, 1498, 1499, 1500, 1501, 1501, 1499, 1499, 1500, 1499, 1500, 1500, 1499, 1500, 1501, 1499, 1502, 1499, 
     1500, 1500, 1500, 1499, 1501, 1500, 1501, 1499, 1499, 1500, 1500, 1499, 1498, 1502, 1499, 1499, 1499, 1498, 1501, 1497, 1499, 1500, 1499, 1499, 
     1497, 1501, 1501, 1499, 1501, 1501, 1500, 1500, 1499, 1501, 1500, 1502, 1499, 1500, 1499, 1500, 1499, 1500, 1500, 1500, 1499, 1500, 1499, 1500, 
     1502, 1500, 1499, 1500, 1498, 1500, 1499, 1499, 1499, 1503, 1500, 1500, 1499, 1500, 1500, 1500, 1500, 1498, 1499, 1501, 1498, 1500, 1500, 1501, 
     1500, 1500, 1500, 1501, 1500, 1499, 1499, 1501, 1502, 1499, 1502, 1500, 1501, 1500, 1500, 1500, 1500, 1500, 1499, 1501, 1501, 1499, 1499, 1500, 
     1500, 1501, 1499, 1500, 1501, 1500, 1500, 1500, 1499, 1502, 1500, 1499, 1502, 1502, 1500, 1498, 1500, 1501, 1500, 1499, 1500, 1500, 1502, 1499, 
     1499, 1500, 1502, 1499, 1497, 1501, 1501, 1501, 1497, 1499, 1502, 1501, 1497, 1499, 1500, 1500]

def calculateDownwellingSpectralFlux(wvl_lgr, spectrum, delta):
    '''
    This function will calculate the downwelling spectral flux.
    A desired type for wvl_lgr would be a single 1D list, and spectrum
    should be a nested 2D list. The area for spectrometer and integration
    time are default.

    This function is based on the following algorithm, provided by Solmaz in 
    https://github.com/terraref/reference-data/issues/30#issuecomment-253000597

    Ip = (Sp - Dp) * Cp / (T * A * dLp) 
    dL = [L(p + 1) - L(p - 1)] / 2

    Here:
    **Denominator**
    AREA                          -> the area of the sensor (A above)
    Spectrometer_Integration_Time -> integartion time (5000us, T above)
    delta                         -> The wavelength spread (dL above)

    **Numerator**
    spectrum                      -> the spectrum, a 2D array(Sp above)
    DARK_REF                      -> the dark reference (Dp above)
    FLX_SNS                       -> the calibration (Cp above)  
    '''


    Spectrometer_Integration_Time_In_Microseconds = 5000.0 # [us]
    Spectrometer_Integration_Time                 = Spectrometer_Integration_Time_In_Microseconds * 1.0e-6 # [s]

    # wvl_ntf  = [np.average([wvl_lgr[i], wvl_lgr[i+1]]) for i in range(len(wvl_lgr)-1)]
    # delta    = [wvl_ntf[i+1] - wvl_ntf[i] for i in range(len(wvl_ntf) - 1)]
    # delta.insert(0,  2*(wvl_ntf[0]  - wvl_lgr[0]))
    # delta.insert(-1, 2*(wvl_lgr[-1] - wvl_ntf[-1]))

    # Using dark reference to calibrate the original sperctrum value

    # General formula used in calculating downwelling spectral flux:
    # Downwelling Spectral Flux = (spectrum [cnt] - dark [cnt]) * flx_sns [J cnt-1]  / bandwidth [m] / area [m2] / time [s]
    downwellingSpectralFlux = np.array(FLX_SNS) * 1.0e-6 * (np.array(spectrum) - np.array(DARK_MEASUREMENTS)) / np.array(delta) / AREA / Spectrometer_Integration_Time # [J m-2 m-1 s-1] = [W m-2 m-1]

    # downwellingFlux is the summation (integration) of downwelling flux
    downwellingFlux = np.sum(downwellingSpectralFlux)

    return downwellingSpectralFlux, downwellingFlux  