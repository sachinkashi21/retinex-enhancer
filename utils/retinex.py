import cv2
import numpy as np
import cv2.ximgproc as xip

def msr(img, sigma_list=[15, 80, 250]):
    img = img.astype(np.float32) + 1.0
    result = np.zeros_like(img)
    for sigma in sigma_list:
        blur = cv2.GaussianBlur(img, (0, 0), sigma)
        result += np.log(img) - np.log(blur + 1.0)
    return result / len(sigma_list)

def color_restoration(img, alpha=125.0, beta=46.0):
    sum_channels = np.sum(img, axis=2, keepdims=True)
    return beta * (np.log(alpha * img + 1.0) - np.log(sum_channels + 1.0))

def msrcr(img):
    img = img.astype(np.float32) + 1.0
    msr_result = msr(img)
    crf = color_restoration(img)
    return msr_result * crf

def apply_guided_filter(I, p, radius=8, eps=0.2**2):
    I = I.astype(np.float32)
    p = p.astype(np.float32)
    return xip.guidedFilter(guide=I, src=p, radius=radius, eps=eps, dDepth=-1)

def enhance_image(input_path, output_path):
    img = cv2.imread(input_path)
    enhanced = msrcr(img)
    guided = apply_guided_filter(img, enhanced)
    guided = cv2.normalize(guided, None, 0, 255, cv2.NORM_MINMAX)
    guided = np.clip(guided, 0, 255).astype(np.uint8)
    cv2.imwrite(output_path, guided)
