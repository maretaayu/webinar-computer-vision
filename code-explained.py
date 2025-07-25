from ultralytics import YOLO
# Artinya: Kita import/mengambil class YOLO dari library ultralytics.
# Gunanya: Library ini adalah tempat YOLOv8 berada. Jadi kita bisa pakai model YOLO dengan mudah.

import cv2
# Artinya: Kita import OpenCV.
# Gunanya: OpenCV adalah tools untuk akses kamera, gambar, dan video. Di sini dipakai buat ambil webcam & tampilin hasil.


# 1. Load pretrained YOLOv8n model
model = YOLO("yolov8n.pt")
# Artinya: Kita ambil model YOLO versi “n” (nano) yang sudah dilatih.
# Gunanya: Supaya bisa deteksi objek langsung. "yolov8n.pt" adalah file model pre-trained.
# Nano itu versi ringan, cocok untuk demo cepat dan real-time.


# 2. Buka webcam
cap = cv2.VideoCapture(0)  # 0 untuk webcam default
# Artinya: Kita hidupkan webcam.
# Gunanya: 0 artinya pakai webcam default laptop/PC kamu. Kalau ada banyak webcam bisa pakai 1, 2, dst.


# Loop untuk Baca dan Deteksi Frame Real-Time
while True:
# Artinya: Kita bikin loop yang jalan terus (infinite loop).
# Gunanya: Supaya terus ambil gambar dari webcam dan proses tiap frame.
    ret, frame = cap.read()
#     Artinya: Kita baca satu frame/gambar dari webcam.
#     Gunanya:  ret: boolean, apakah baca berhasil?
#               frame: isi gambar yang didapat dari webcam
    if not ret:
        break
    # Artinya: Kalau gagal baca frame (misal webcam mati), hentikan loop.


    # 3. Deteksi objek dalam 1 frame
    results = model(frame)
    # Artinya: Kita kirim frame itu ke model YOLO untuk dideteksi objeknya.
    # Gunanya: YOLO akan kasih tahu ada objek apa aja dan posisinya (bounding box)


    # 4. Plot hasil deteksi ke frame (bounding box + label)
    annotated_frame = results[0].plot()
    # Artinya: Kita gambar hasil deteksi ke dalam frame.
    # Gunanya: Supaya muncul kotak dan label nama objek di video (misalnya “person”, “car”).
    # Kenapa results[0]? Karena model() bisa kasih banyak hasil, tapi kita ambil satu frame saja (yang sekarang diproses).

    # 5. Tampilkan di window
    cv2.imshow("YOLO Real-Time Detection", annotated_frame)

    # Tekan 'q' untuk keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 6. Bersihkan setelah selesai
cap.release()
cv2.destroyAllWindows()
