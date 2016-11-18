import cv2
import numpy as np

class Saliency:
    def __init__(self, img, use_numpy_fft=True, gauss_kernel=(5,5)):
        self.use_numpy_fft = use_numpy_fft
        self.gauss_kernel = gauss_kernel
        self.frame_orig = img

        self.small_shape = (64, 64)
        self.frame_small = cv2.resize(img, self.small_shape[1::-1])

        # check for math (true/false)
        self.need_saliency_map = True

    def plot_magnitude(self):
        if len(self.frame_orig.shape) > 2:
            frame = cv2.cvtColor(self.frame_orig, cv2.COLOR_BGR2GRAY)
        else:
            frame = self.frame_orig

        rows, cols = self.frame_orig.shape[:2]
        nrows = cv2.getOptimalDFTSize(rows)
        ncols = cv2.getOptimalDFTSize(cols)
        frame = cv2.copyMakeBorder(frame, 0, ncols - cols, 0, nrows - rows, cv2.BORDER_CONSTANT, value=0)
        img_dft = np.fft.fft2(frame)
        magn = np.abs(img_dft)
        log_magn = np.log10(magn)
        spectrum = np.fft.fftshift(log_magn)

        return spectrum/np.max(spectrum)*255

    def plot_power_spectrum(self):
        if len(self.frame_orig.shape) > 2:
            frame = cv2.cvtColor(self.frame_orig, cv2.COLOR_BGR2GRAY)
        else:
            frame = self.frame_orig

        rows, cols = self.frame_orig.shape[:2]
        nrows = cv2.getOptimalDFTSize(rows)
        ncols = cv2.getOptimalDFTSize(cols)
        frame = cv2.copyMakeBorder(frame, 0, ncols - cols, 0, nrows - rows, cv2.BORDER_CONSTANT, value=0)

        if self.use_numpy_fft:
            img_dft = np.fft.fft2(frame)
            spectrum = np.log10(np.real(np.abs(img_dft))**2)
        else:
            img_dft = cv2.dft(np.float32(frame), flags=cv2.DFT_COMPLEX_OUTPUT)
            spectrum = np.log10(img_dft[:,:,0]**2 + img_dft[:,:,1]**2)

        L = max(frame.shape)
        freqs = np.fft.fftfreq(L)[:L/2]
        dists = np.sqrt(np.fft.fftfreq(frame.shape[0])[:,np.newaxis]**2 )

