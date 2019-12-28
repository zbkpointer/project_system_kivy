import cv2

# 要更改自己的文件绝对路径
face_cascade = cv2.CascadeClassifier(
    '..\\opencv-4.2.0\\opencv-4.2.0\\data\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    '..\\opencv-4.2.0\\opencv-4.2.0\\data\\haarcascades\\haarcascade_eye_tree_eyeglasses.xml')

# 加载CSI摄像头，通过libv4l2
cap = cv2.VideoCapture(0)

# OpenCV版本测试
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

while cap.isOpened():
    _, img = cap.read()

    # 计算摄像头的FPS
    if int(major_ver) < 3:
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = cap.get(cv2.CAP_PROP_FPS)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'FPS: ' + str(fps)

    # 将FPS的值展现到视频帧中
    img = cv2.putText(img, text, (10, 50), font, 1,
                      (0, 255, 255), 2, cv2.LINE_AA)
    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
