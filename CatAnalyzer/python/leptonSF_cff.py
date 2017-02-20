import FWCore.ParameterSet.Config as cms

dummySF = cms.PSet(
    pt_bins = cms.vdouble(0,1e9),
    abseta_bins = cms.vdouble(0,1e9),
    eta_bins = cms.vdouble(-1e9,1e9),
    values = cms.vdouble(1.0),
    errors = cms.vdouble(0.0),
)

## Muon SF reference https://twiki.cern.ch/twiki/bin/view/CMS/MuonWorkInProgressAndPagResults
## SF for Run2016BCDE, before HIP issue
muonSFTight = cms.PSet(
    # Values of "MC_NUM_TightID_DEN_genTracks_PAR_pt_eta + TightISO_TightID_pt_eta"
    pt_bins = cms.vdouble(20, 25, 30, 40, 50, 60, 120),
    abseta_bins = cms.vdouble(0, 0.9, 1.2, 2.1, 2.4),
    values = cms.vdouble(
        0.968738, 0.973607, 0.975917, 0.978181, 0.976527, 0.991363, 
        0.95508, 0.960286, 0.964482, 0.965257, 0.969011, 0.966896, 
        0.972479, 0.976585, 0.981631, 0.985377, 0.983263, 0.987963, 
        0.946304, 0.956094, 0.961093, 0.967634, 0.965302, 0.964568, 
    ),
    errors = cms.vdouble(
        0.015418, 0.0150867, 0.0150098, 0.0150043, 0.0150314, 0.0151446, 
        0.0157991, 0.0152807, 0.0151646, 0.0150083, 0.0150749, 0.0152792, 
        0.0151862, 0.0150565, 0.0150083, 0.0150033, 0.0150312, 0.0151421, 
        0.0155888, 0.0152089, 0.0150463, 0.0154599, 0.0152765, 0.0161151, 
    ),
)

## SF for Run2016G-H, after HIP issue
muonSFTightGH = cms.PSet(
    # Values of "MC_NUM_TightID_DEN_genTracks_PAR_pt_eta + TightISO_TightID_pt_eta"
    pt_bins = cms.vdouble(20, 25, 30, 40, 50, 60, 120),
    abseta_bins = cms.vdouble(0, 0.9, 1.2, 2.1, 2.4),
    values = cms.vdouble(
        0.974446, 0.979875, 0.98113, 0.985025, 0.981515, 0.990442, 
        0.983291, 0.984416, 0.983519, 0.981617, 0.979491, 0.982805, 
        0.984607, 0.988896, 0.991054, 0.992458, 0.984471, 0.988043, 
        0.975841, 0.978226, 0.971587, 0.974991, 0.967654, 0.964672, 
    ),
    errors = cms.vdouble(
        0.0154011, 0.0486999, 0.0150098, 0.0150036, 0.0150252, 0.0150953, 
        0.0218827, 0.0152387, 0.0150285, 0.0150103, 0.0150798, 0.0153115, 
        0.0152088, 0.0150629, 0.0254806, 0.0150025, 0.0150384, 0.0151946, 
        0.0155797, 0.0553856, 0.0151542, 0.0161887, 0.0152824, 0.0160921, 
    ),
)

## Retrieve data from the cmsdoc web page:
##   https://cmsdoc.cern.ch/cms/Physics/muon/ReferenceEfficiencies/Run2016/25ns/proviSFs_2p6fb/MuonID_Z_2016runB_2p6fb.json
##   https://cmsdoc.cern.ch/cms/Physics/muon/ReferenceEfficiencies/Run2016/25ns/proviSFs_2p6fb/MuonISO_Z_2016runB_2p6fb.json
#muonSFTight = cms.PSet(
#    # Values of "MC_NUM_TightIDandIPCut_DEN_genTracks_PAR_pt_spliteta_bin1 + MC_NUM_TightRelIso_DEN_TightID_PAR_pt_spliteta_bin1"
#    pt_bins = cms.vdouble(20, 25, 30, 40, 50, 60, 100, 200),
#    abseta_bins = cms.vdouble(0, 0.9, 1.2, 2.1, 2.4),
#    values = cms.vdouble(
#        0.941436, 0.959701, 0.968116, 0.970538, 0.968821, 0.972572, 0.987711,
#        0.955623, 0.96175, 0.969717, 0.968784, 0.970868, 0.967741, 1.02273,
#        0.97839, 0.983576, 0.987746, 0.988816, 0.990644, 0.988234, 1.01927,
#        0.968935, 0.963683, 0.967626, 0.966395, 0.979048, 0.975934, 0.916776,
#    ),
#    errors = cms.vdouble(
#        0.0155081, 0.0151449, 0.0150189, 0.0150086, 0.0150436, 0.0151513, 0.0221035,
#        0.0161243, 0.0154153, 0.0150604, 0.0150198, 0.0151218, 0.0154361, 0.0273559,
#        0.0152889, 0.0151052, 0.015018, 0.0150034, 0.015053, 0.0152429, 0.0179484,
#        0.0159104, 0.0153603, 0.0150775, 0.0150447, 0.0154516, 0.0169014, 0.0812482,
#    ),
#)

## Muon SF reference https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonReferenceEffsRun2
## Retrieve data from the cmsdoc web page:
##   https://cmsdoc.cern.ch/cms/Physics/muon/ReferenceEfficiencies/Run2015/25ns/MuonID_Z_RunCD_Reco76X_Feb15.json
##   https://cmsdoc.cern.ch/cms/Physics/muon/ReferenceEfficiencies/Run2015/25ns/MuonIso_Z_RunCD_Reco76X_Feb15.json
muonSFTight76X = cms.PSet(
    # Values of "MC_NUM_TightIDandIPCut_DEN_genTracks_PAR_pt_spliteta_bin1 + MC_NUM_TightRelIso_DEN_TightID_PAR_pt_spliteta_bin1"
    pt_bins = cms.vdouble(20, 25, 30, 40, 50, 60, 120),
    abseta_bins = cms.vdouble(0, 0.9, 1.2, 2.1, 2.4),
    values = cms.vdouble(
        0.975283, 0.980129, 0.986676, 0.985789, 0.980877, 0.985445,
        0.984484, 0.970783, 0.980673, 0.980057, 0.977943, 0.984907,
        0.986784, 0.990845, 0.993367, 0.990324, 0.988209, 0.991915,
        0.971296, 0.971883, 0.976009, 0.977, 0.973655, 0.963135,
    ),
    errors = cms.vdouble(
        0.0157468, 0.0136165, 0.0120878, 0.0118247, 0.0125879, 0.0135921,
        0.0181504, 0.0154891, 0.0127943, 0.0121561, 0.0134922, 0.0152142,
        0.0145121, 0.0132486, 0.0120305, 0.0116593, 0.0124603, 0.0137997,
        0.0176168, 0.0153647, 0.0131657, 0.0126734, 0.0148934, 0.0197265,
    ),

)

## Electron SF from https://twiki.cern.ch/twiki/bin/view/CMS/EgammaIDRecipesRun2?rev=36#Electron_efficiencies_and_scale
## root file is retrieved from 
##  GSF: http://fcouderc.web.cern.ch/fcouderc/EGamma/scaleFactors/ichep2016_80X/resultsGsfID/egammaEffi.txt_SF2D.root
##   ID: http://fcouderc.web.cern.ch/fcouderc/EGamma/scaleFactors/ichep2016_80X//resultsEleID/runBCD/passingMedium/egammaEffi.txt_SF2D.root
## Systematic uncertainty of 1% is added for pt>20, 3% for pt<20
electronSFCutBasedIDMediumWP = cms.PSet(
    pt_bins = cms.vdouble(10.000000,20.000000,30.000000,40.000000,50.000000,200.000000),
    eta_bins = cms.vdouble(-2.500000,-2.400000,-2.300000,-2.200000,-2.000000,-1.800000,-1.630000,-1.566000,-1.444000,-1.200000,-1.000000,-0.800000,-0.600000,-0.400000,-0.200000,0.000000,0.200000,0.400000,0.600000,0.800000,1.000000,1.200000,1.444000,1.566000,1.630000,1.800000,2.000000,2.200000,2.300000,2.400000,2.500000),
    values = cms.vdouble(1.004394, 1.051580, 1.113248, 1.136900, 1.143739, 
        0.865521, 0.906182, 0.959324, 0.979705, 0.985599, 
        0.867195, 0.907936, 0.961180, 0.981601, 0.987506, 
        0.862660, 0.903187, 0.956153, 0.976467, 0.982342, 
        0.747299, 0.852237, 0.921168, 0.951433, 0.964706, 
        0.742633, 0.846916, 0.915417, 0.945493, 0.958683, 
        0.738728, 0.842463, 0.910603, 0.940521, 0.953641, 
        0.845836, 0.915683, 0.920277, 0.914708, 0.930183, 
        0.934946, 0.932272, 0.950788, 0.952276, 0.951018, 
        0.926265, 0.923615, 0.941959, 0.943433, 0.942187, 
        0.918573, 0.915945, 0.934137, 0.935599, 0.934363, 
        0.891241, 0.906104, 0.917720, 0.922408, 0.923756, 
        0.888458, 0.903275, 0.914854, 0.919528, 0.920872, 
        0.885647, 0.900416, 0.911959, 0.916618, 0.917958, 
        0.882610, 0.897329, 0.908832, 0.913475, 0.914811, 
        0.872103, 0.920519, 0.934187, 0.937467, 0.939474, 
        0.884238, 0.933329, 0.947187, 0.950512, 0.952547, 
        0.881481, 0.930418, 0.944233, 0.947548, 0.949576, 
        0.885158, 0.934299, 0.948172, 0.951500, 0.953537, 
        0.913967, 0.915076, 0.933773, 0.938574, 0.945385, 
        0.919637, 0.920752, 0.939565, 0.944396, 0.951249, 
        0.919586, 0.920702, 0.939513, 0.944344, 0.951196, 
        0.981011, 0.893716, 0.918568, 0.906911, 0.912165, 
        0.806139, 0.869133, 0.927573, 0.951968, 0.975987, 
        0.811192, 0.874580, 0.933386, 0.957934, 0.982104, 
        0.806191, 0.869189, 0.927632, 0.952029, 0.976050, 
        0.854016, 0.906395, 0.941262, 0.963355, 0.973669, 
        0.852219, 0.904488, 0.939282, 0.961329, 0.971621, 
        0.829783, 0.880676, 0.914553, 0.936020, 0.946041, 
        0.758867, 0.805410, 0.836393, 0.856025, 0.865189, 
        ),
    errors = cms.vdouble(0.051707, 0.027292, 0.023140, 0.022858, 0.024263, 
        0.049556, 0.027871, 0.023820, 0.023546, 0.024913, 
        0.046713, 0.025251, 0.020693, 0.020378, 0.021943, 
        0.046215, 0.024888, 0.020249, 0.019926, 0.021524, 
        0.064888, 0.027192, 0.020443, 0.018483, 0.018416, 
        0.064821, 0.027197, 0.020450, 0.018490, 0.018424, 
        0.064375, 0.026767, 0.019874, 0.017852, 0.017783, 
        0.105072, 0.067430, 0.034307, 0.029134, 0.030253, 
        0.042703, 0.026322, 0.017786, 0.016833, 0.016811, 
        0.043258, 0.026841, 0.018546, 0.017634, 0.017613, 
        0.042227, 0.026186, 0.017584, 0.016619, 0.016597, 
        0.046313, 0.025447, 0.016927, 0.016205, 0.016597, 
        0.046744, 0.025838, 0.017510, 0.016813, 0.017191, 
        0.046461, 0.025643, 0.017221, 0.016512, 0.016897, 
        0.046552, 0.025759, 0.017393, 0.016691, 0.017072, 
        0.046693, 0.025798, 0.017450, 0.016751, 0.017131, 
        0.046834, 0.025745, 0.017373, 0.016670, 0.017052, 
        0.046978, 0.025902, 0.017605, 0.016912, 0.017288, 
        0.046569, 0.025516, 0.017031, 0.016314, 0.016704, 
        0.042508, 0.026253, 0.017684, 0.016725, 0.016704, 
        0.043490, 0.026899, 0.018629, 0.017721, 0.017701, 
        0.042703, 0.026322, 0.017786, 0.016833, 0.016811, 
        0.105195, 0.067469, 0.034382, 0.029222, 0.030338, 
        0.064430, 0.026787, 0.019901, 0.017882, 0.017813, 
        0.065021, 0.027367, 0.020675, 0.018740, 0.018674, 
        0.064714, 0.027102, 0.020323, 0.018351, 0.018284, 
        0.045996, 0.024845, 0.020197, 0.019873, 0.021475, 
        0.046203, 0.025059, 0.020459, 0.020139, 0.021721, 
        0.048418, 0.027473, 0.023354, 0.023074, 0.024467, 
        0.044372, 0.025018, 0.020409, 0.020089, 0.021675, 
        ),
)

electronSFCutBasedIDMediumWPIdOnly = cms.PSet(
    pt_bins = cms.vdouble(10.000000,20.000000,30.000000,40.000000,50.000000,200.000000),
    eta_bins = cms.vdouble(-2.500000,-2.000000,-1.566000,-1.444000,-0.800000,0.000000,0.800000,1.444000,1.566000,2.000000,2.500000),
    values = cms.vdouble(0.858209, 0.898527, 0.951219, 0.971429, 0.977273, 
        0.748848, 0.854003, 0.923077, 0.953405, 0.966705, 
        0.879630, 0.952267, 0.957045, 0.951253, 0.967347, 
        0.947581, 0.944870, 0.963636, 0.965144, 0.963869, 
        0.919386, 0.934718, 0.946701, 0.951537, 0.952928, 
        0.902622, 0.952733, 0.966879, 0.970273, 0.972350, 
        0.932000, 0.933131, 0.952196, 0.957092, 0.964037, 
        1.010601, 0.920673, 0.946274, 0.934266, 0.939678, 
        0.814554, 0.878205, 0.937255, 0.961905, 0.986175, 
        0.858427, 0.911076, 0.946124, 0.968331, 0.978698, 
        ),
    errors = cms.vdouble(0.025860, 0.016977, 0.008878, 0.008115, 0.011493, 
        0.052968, 0.020792, 0.010527, 0.005876, 0.005664, 
        0.093792, 0.061282, 0.019637, 0.007580, 0.011131, 
        0.023546, 0.020984, 0.007988, 0.005550, 0.005485, 
        0.030269, 0.020054, 0.006414, 0.004149, 0.005486, 
        0.030269, 0.020054, 0.006413, 0.004149, 0.005486, 
        0.023546, 0.020984, 0.007988, 0.005550, 0.005485, 
        0.093791, 0.061282, 0.019637, 0.007580, 0.011132, 
        0.052968, 0.020792, 0.010527, 0.005876, 0.005664, 
        0.025861, 0.016977, 0.008878, 0.008115, 0.011493, 
        ),
)

## Electorn SF from http://fcouderc.web.cern.ch/fcouderc/EGamma/scaleFactors/moriond2016_76X/eleCutBasedID/CutBasedID_MediumWP_76X_18Feb.txt_egammaPlots.pdf
electronSFCutBasedIDMediumWP76X = cms.PSet(
    # Values of "CutBasedID_MediumWP"
    pt_bins = cms.vdouble(10, 20, 30, 40, 50, 200),
    abseta_bins = cms.vdouble(0, 0.8, 1.444, 1.566, 2, 2.5),
    values = cms.vdouble(
        1.00726, 0.971182, 0.984906, 0.985899, 0.988598,
        1.0902, 0.983359, 0.987179, 0.98692, 0.986159,
        1.08642, 0.963054, 0.949123, 0.981612, 0.997257,
        0.984444, 0.936809, 0.975066, 0.992806, 1.00579,
        1.03557, 0.986446, 0.963351, 1.00611, 1.00949,
    ),
    errors = cms.vdouble(
        0.0656124, 0.0279776, 0.0291216, 0.0175478, 0.00603364,
        0.0391175, 0.0256741, 0.0171527, 0.0277844, 0.00540994,
        0.0800687, 0.261884 , 0.0511487, 0.036227 , 0.113466  ,
        0.0447765, 0.0186922, 0.0274652, 0.0404665, 0.0125727 ,
        0.0303603, 0.0263447, 0.0445603, 0.0103732, 0.0137829 ,
    ),
)

## Retrieve data from the cmsdoc web page:
##   https://cmsdoc.cern.ch/cms/Physics/muon/ReferenceEfficiencies/Run2015/25ns/MuonID_Z_RunCD_Reco74X_Dec1.json
muonSFTight74X = cms.PSet(
    # Values of "NUM_TightIDandIPCut_DEN_genTracks_PAR_pt_spliteta_bin1 + NUM_TightRelIso_DEN_TightID_PAR_pt_spliteta_bin1"
    pt_bins = cms.vdouble(20, 25, 30, 40, 50, 60, 120),
    abseta_bins = cms.vdouble(0, 0.9, 1.2, 2.1, 2.4),
    values = cms.vdouble(
        0.979479, 0.984375, 0.987068, 0.986086, 0.983674, 0.985021,
        0.978054, 0.980927, 0.984458, 0.981568, 0.975983, 0.984876,
        0.99541, 0.991193, 0.994704, 0.992697, 0.988925, 0.995536,
        0.983608, 0.974278, 0.976037, 0.980598, 0.969666, 0.969941,
    ),
    errors = cms.vdouble(
        0.0191201, 0.0168928, 0.0151444, 0.0148111, 0.015527, 0.0162596,
        0.021688, 0.0189092, 0.0159175, 0.0150692, 0.0164092, 0.0178394,
        0.0179975, 0.0166027, 0.0151404, 0.0147407, 0.0154785, 0.0167413,
        0.0219747, 0.0194149, 0.0165014, 0.0159522, 0.0180924, 0.0243999,
    ),
)

electronSFWP9074X = cms.PSet(
    ## SF from https://indico.cern.ch/event/369259/contribution/3/attachments/1204731/1755463/update_SFs_triggering_MVA_ID_systematics.pdf
    eta_bins = cms.vdouble(-2.5, -1.5, -1.0, 0, 1.0, 1.5, 2.5),
    pt_bins = cms.vdouble(15, 25, 35, 45, 55, 1e9),
    values = cms.vdouble(
        0.96, 0.95, 0.98, 0.99, 0.99, 0.97,
        0.98, 0.97, 0.97, 0.99, 0.99, 0.98,
        0.98, 0.99, 0.99, 0.99, 0.99, 0.98,
        0.98, 0.99, 0.99, 0.99, 0.99, 0.99,
        0.99, 0.99, 1.00, 1.00, 0.99, 0.99,
    ),
    errors = cms.vdouble(
        0.02, 0.06, 0.01, 0.01, 0.02, 0.01,
        0.01, 0.01, 0.02, 0.01, 0.01, 0.01,
        0.00, 0.00, 0.00, 0.00, 0.00, 0.01,
        0.01, 0.00, 0.01, 0.00, 0.01, 0.01,
        0.01, 0.02, 0.01, 0.00, 0.02, 0.02,
    ),
)

electronSFCutBasedIDMediumWP74X = cms.PSet(
    ## SF from https://indico.cern.ch/event/491528/contribution/2/attachments/1231399/1805319/CutBasedId_EGM_19Feb.pdf
    ## Actual numbers are taken from https://arun-afs.web.cern.ch/arun-afs/Final_Fits_Data_74X/CutBasedID_MediumWP_fromTemplates_withSyst_Final.txt
    # Values of "CutBasedID_MediumWP"
    pt_bins = cms.vdouble(10, 20, 30, 40, 50, 200),
    eta_bins = cms.vdouble(-2.5, -2, -1.566, -1.444, -0.8, 0, 0.8, 1.444, 1.566, 2, 2.5),
    values = cms.vdouble(
        1.25131, 1.0536, 1.01235, 1.00875, 1.006,
        1.09254, 0.969453, 0.971279, 0.983313, 0.985109,
        1.29412, 1.04043, 1.02482, 0.990155, 0.948856,
        1.32673, 1.05939, 0.990897, 0.974057, 0.958097,
        1.23371, 1.02262, 0.978616, 0.969838, 0.967489,
        1.22889, 1.01799, 0.986164, 0.974448, 0.970819,
        1.30827, 1.07742, 1.00654, 0.976359, 0.964773,
        1.35498, 1.18801, 0.990991, 0.956153, 0.974394,
        1.06283, 0.980392, 0.961892, 0.978469, 0.994253,
        1.20769, 1.02649, 1.0096, 1.00125, 1.00481,
    ),
    errors = cms.vdouble(
        0.712863, 0.0517635, 0.0242599, 0.0222102, 0.0337348,
        0.662784, 0.0757762, 0.575897, 0.0392023, 0.0671983,
        3.75487, 1.17119, 0.124767, 0.0150145, 0.0555887,
        1.2277, 0.20447, 0.0280944, 0.00855398, 0.0355446,
        0.813571, 0.108281, 0.00853765, 0.0217419, 0.0302874,
        0.761126, 0.580145, 0.0313306, 0.0196618, 0.0253676,
        0.874693, 0.237932, 0.650881, 0.0103168, 0.0286228,
        4.59432, 1.84669, 0.1764, 0.0506619, 0.161535,
        0.797724, 0.0632952, 0.0377029, 0.0313089, 0.0300417,
        0.617985, 0.0693681, 0.0293348, 0.024152, 0.0894748,
    ),
)

