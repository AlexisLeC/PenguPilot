g++ -I/usr/include/opencv /usr/lib/libopencv_calib3d.so /usr/lib/libopencv_contrib.so /usr/lib/libopencv_core.so /usr/lib/libopencv_features2d.so /usr/lib/libopencv_flann.so /usr/lib/libopencv_gpu.so /usr/lib/libopencv_highgui.so /usr/lib/libopencv_imgproc.so /usr/lib/libopencv_legacy.so /usr/lib/libopencv_ml.so /usr/lib/libopencv_nonfree.so /usr/lib/libopencv_objdetect.so /usr/lib/libopencv_photo.so /usr/lib/libopencv_stitching.so /usr/lib/libopencv_superres.so /usr/lib/libopencv_ts.a /usr/lib/libopencv_video.so /usr/lib/libopencv_videostab.so main.cpp -ltbb -lrt -lpthread -lm -ldl -I ../../shared/ -I ../../scl/shared ../../scl/shared/libscl.a -l glib-2.0 -l zmq -l yaml -l msgpack ../../shared/libshared.a