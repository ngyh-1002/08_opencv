import cv2
import numpy as np

categories =  ['P01','P02','P03','P04','P05','P06','P07','P08','P09','P10']
dict_file = './pose_dict.npy'
#dict_file = './plane_bike_dict_4000.npy'
svm_model_file = './pose_svm.xml'
#svm_model_file = './plane_bike_svm_4000.xml'

# 테스트 할 이미지 경로 --- ①
imgs = ['../img/A_P01_0258_cam101_100f.jpg','../img/A_P04_0271_cam101_100f.jpg', 
        '../img/B_P07_0289_cam101_100f.jpg', '../img/C_P09_0313_cam101_100f.jpg']

# 특징 추출기(SIFT) 생성 ---②
detector = cv2.xfeatures2d.SIFT_create()
# BOW 추출기 생성 및 사전 로딩 ---③
bowextractor = cv2.BOWImgDescriptorExtractor(detector, \
                                cv2.BFMatcher(cv2.NORM_L2))
bowextractor.setVocabulary(np.load(dict_file))
# 훈련된 모델 읽어서 SVM 객체 생성 --- ④
svm  = cv2.ml.SVM_load(svm_model_file)

# 4개의 이미지 테스트 
for i, path in enumerate(imgs):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 테스트 이미지에서 BOW 히스토그램 추출 ---⑤
    hist = bowextractor.compute(gray, detector.detect(gray))
    # SVM 예측 ---⑥
    ret, result = svm.predict(hist)
    # 결과 표시 
    name = categories[int(result[0][0])]
    txt, base = cv2.getTextSize(name, cv2.FONT_HERSHEY_PLAIN, 2, 3)
    x,y = 10, 50
    cv2.rectangle(img, (x,y-base-txt[1]), (x+txt[0], y+txt[1]), (30,30,30), -1)
    cv2.putText(img, name, (x,y), cv2.FONT_HERSHEY_PLAIN, \
                                 2, (0,255,0), 2, cv2.LINE_AA)
    cv2.imshow(path, img)
cv2.waitKey(0)
cv2.destroyAllWindows()