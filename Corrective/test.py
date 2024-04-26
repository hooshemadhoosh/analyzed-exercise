import pickle


def save_object(obj,filename):
    try:
        with open(filename, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


names = {'سر به جلو': 'Forward Head', 'شانه گرد': 'Rounded Shoulder', 'پشت گرد': 'hyper Kyphosis', 'پشت تابدار': 'Swayback', 'برآمدگی شکم': 'Abdomen Protruding', 'کمر گود': 'hyper Lordosis', 'پشت صاف': 'Flat Back', 'زانوی عقب رفته': 'Hyperextended Knee', 'زانوی خمیده': 'Flexed Knee', 'کج گردنی یا چرخش گردن': 'Torticollis', 'شانه نابرابر': 'Uneven Shoulders', 'کتف بالدار': 'Winging Scapula', 'انحراف جانبی ستون فقرات': 'Scoliosis', 'انحراف جانبی لگن': 'Uneven Hips', 'چرخش خارجی پا': 'toeing out', 'چرخش داخلی پا': 'Toeing in', 'چرخش مچ پا به داخل': 'Pronation', 'چرخش مچ پا به خارج': 'Supination', 'زانو پرانتزی': 'Genu Varum', 'زانو ضربدری': 'Genu Valgum', 'کف پای صاف': 'Flat Foot', 'کف پای گود': 'High Arch Foot', 'اسکات قدامی صاف شدن پاها': 'OverheadSquat_FeetFlatten', 'اسکات قدامی چرخش به خارج پاها': 'OverheadSquat_FeetTurnOut', 'اسکات قدامی حرکت زانوها به داخل': 'OverheadSquat_KneesMoveInward', 'اسکات قدامی حرکت زانوها به خارج': 'OverheadSquat_KneesMoveOutward', 'اسکات جانبی گود شدن کمر': 'OverheadSquat_LowBackArches', 'اسکات جانبی کمر صاف': 'OverheadSquat_LowBackRounds', 'اسکات جانبی خمیدگی به جلو': 'OverheadSquat_ExcessiveForwardLean', 'اسکات جانبی دست ها در جلو': 'OverheadSquat_ArmsFallForward', 'اسکات خلفی صاف شدن پا': 'OverheadSquat_FeetFlatten', 'اسکات خلفی بلند شدن پاشنه': 'OverheadSquat_HeelsRiseOffFloor', 'اسکات خلفی انتقال نامتقارن ': 'OverheadSquat_AsymmetricWeightShift', 'راه رفتن صاف شدن پاها و چرخش زانو به داخل': 'Gait_FeetFlatten', 'راه رفتن گود شدن کمر': 'Gait_LowBackArches', 'راه رفتن شانه ها گرد می شود': 'Gait_ShouldersRound', 'راه رفتن سر به جلو': 'Gait_HeadForward', 'راه رفتن صاف شدن و چرخش به خارج پاها': 'Gait_FeetTurnOut', 'راه رفتن چرخش بیش از حد لگن': 'Gait_ExcessivePelvicRotation', 'راه رفتن بالا آمدن ران': 'Gait_HipHikes', 'اسکات تک پا حرکت زانو به داخل': 'SingleLegSquat_KneeMovesInward', 'اسکات تک پا بالا آمدن ران': 'SingleLegSquat_HipHikes', 'اسکات تک پا سقوط ران': 'SingleLegSquat_HipDrops', 'اسکات تک پا چرخش داخلی تنه': 'SingleLegSquat_TorsoRotatesInward', 'اسکات تک پا چرخش خارجی تنه': 'SingleLegSquat_TorsoRotatesOutward', 'چرخش دست ها بالاآمدن شانه ها': 'ShoulderRotationTest_ShouldersElevate', 'چرخش دست ها پروترکشن شانه ها': 'ShoulderRotationTest_ShouldersProtract', 'چرخش داخلی دست ها فاصله از دیوار': 'ShoulderRotationTest_HandsFarfromWallInternalRotation', 'چرخش خارجی دست ها فاصله از دیوار ': 'ShoulderRotationTest_HandsFarfromWallExternalRotation', 'دور شدن دست ها بالا آمدن شانه': 'ShoulderAbductionTest_ShouldersElevate', 'دور شدن دست ها پروتکشن شانه': 'ShoulderAbductionTest_ShouldersProtract', 'دور شدن دست ها خم شدن آرنج ها': 'ShoulderAbductionTest_ElbowsFlex', 'خم شدن دست ها بالاآمدن شانه': 'ShoulderFlexionTest_ShouldersElevate', 'خم شدن دست ها گود شدن کمر': 'ShoulderFlexionTest_LowBackArches', 'خم شدن دست ها خم شدن آرنج': 'ShoulderFlexionTest_ElbowsFlex', 'شنا گود شدن کمر': 'PushUp_LowBackSags', 'شنا صاف شدن کمر': 'PushUp_LowBackRounds', 'شنا بالا آمدن شانه': 'PushUp_ShouldersElevate', 'شنا بالی شدن کتف': 'PushUp_ScapulaeWings', 'شنا هایپراکستنشن گردن': 'PushUp_CervicalSpineHyperextends','بدشکلی انگشتان پا':'Deformityofthetoes','بدشکلی انگشتان دست':'DeformityofFingers','سینه فرو رفته':'FunnelChest','سینه کبوتری':'PigeonChest'}
for key in names:
    if '_' in key:
        print(key,key.split('_')[1])
        names[key.split('_')[1]]=names[key]

print(names)