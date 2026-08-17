#!/usr/bin/env python3
"""Turn a single ring product still into a short looping "turn side to side" video.

The ring is isolated from its white background, padded so the shank always runs
off-frame, then re-projected each frame as a plane yawing about the vertical axis
through the centre of the head. A soft specular sweep travels across the metal in
sync with the turn so the pave and the gem catch light as it moves.
"""

import math
import os
import shutil
import subprocess
import sys

import numpy as np
from PIL import Image
from scipy import ndimage

SRC = sys.argv[1] if len(sys.argv) > 1 else "ring.jpg"
OUTDIR = sys.argv[2] if len(sys.argv) > 2 else "out"

OUT = 1080            # square output, px
FPS = 30
DURATION = 5.0        # seconds
YAW_DEG = 20.0        # peak turn either side of centre
ROLL_DEG = 2.0        # slight roll, gives it a hand-turned feel
VIEW = 2000           # source px mapped across the output frame
PAD = 520             # mirrored padding so the shank never shows a cut end
FOCAL = 1.7           # x view width; near side of the shank reads bigger as it turns
GLINT = 26            # strength of the light sweeping over the stone

NFRAMES = int(round(FPS * DURATION))


def subject_mask(rgb):
    """White-background cutout: everything that is not near-white paper."""
    a = rgb.astype(np.int16)
    lum = a.mean(2)
    sat = a.max(2) - a.min(2)
    m = (lum < 247) | (sat > 26)
    m = ndimage.binary_closing(m, np.ones((9, 9)))
    lbl, n = ndimage.label(m)
    if n:
        # keep the component covering the gem (most saturated region)
        ys, xs = np.nonzero(sat > 60)
        gy, gx = int(ys.mean()), int(xs.mean())
        keep = lbl[gy, gx]
        if keep == 0:  # gem centre landed in a gap; fall back to biggest blob
            keep = 1 + np.argmax(ndimage.sum(m, lbl, range(1, n + 1)))
        m = lbl == keep
    return ndimage.binary_dilation(m, np.ones((3, 3)))


def homography(yaw, roll, cx, cy, view, out, breath=1.0):
    """source-layer px -> output px, for a plane yawed about x = cx."""
    f = FOCAL * view
    s, c = math.sin(yaw), math.cos(yaw)

    def mat(*rows):
        return np.array(rows, dtype=float)

    # all of the middle stages work in coordinates centred on the rotation axis
    to_axis = mat((1, 0, -cx), (0, 1, -cy), (0, 0, 1))
    # x' = f*X*cos / (f - X*sin), y' = f*Y / (f - X*sin)
    project = mat((f * c, 0, 0), (0, f, 0), (-s, 0, f))
    rs, rc = math.sin(roll), math.cos(roll)
    rot = mat((rc, -rs, 0), (rs, rc, 0), (0, 0, 1))
    k = out / view * breath
    to_frame = mat((k, 0, out / 2), (0, k, out / 2), (0, 0, 1))
    return to_frame @ rot @ project @ to_axis


def fire(frame, phase):
    """Sweep light across the gem as it turns: facets gain contrast and lift.

    The pave is already near paper-white, so there is no headroom to brighten it;
    the stone is where light actually reads, so the sweep is confined to it.
    """
    sat = frame.max(2) - frame.min(2)
    stone = np.clip((sat - 45.0) / 40.0, 0, 1)
    x = np.arange(OUT, dtype=np.float32)
    centre = OUT / 2 - 0.42 * OUT * phase
    sweep = np.exp(-((x - centre) ** 2) / (2 * (0.22 * OUT) ** 2))[None, :]
    w = (stone * sweep)[:, :, None]

    lum = frame.mean(2, keepdims=True)
    mid = 128.0
    contrast = mid + (frame - mid) * (1.0 + 0.22 * w) + (frame - lum) * 0.10 * w
    lift = np.clip((lum - 150.0) / 105.0, 0, 1) * GLINT * w
    return np.where(w > 0, contrast + lift, frame)


def main():
    src = Image.open(SRC).convert("RGB")
    rgb = np.asarray(src)
    mask = subject_mask(rgb)

    # gem centre = horizontal axis of rotation, vertical centre of the head
    a = rgb.astype(np.int16)
    sat = a.max(2) - a.min(2)
    ys, xs = np.nonzero(sat > 60)
    cx, cy = float(xs.mean()), float((ys.min() + ys.max()) / 2)

    clean = np.where(mask[:, :, None], rgb, 255).astype(np.uint8)
    layer = np.dstack([clean, np.where(mask, 255, 0).astype(np.uint8)])
    layer = np.pad(layer, ((0, 0), (PAD, PAD), (0, 0)), mode="reflect")
    layer_img = Image.fromarray(layer, "RGBA")
    cx += PAD

    if os.path.isdir(OUTDIR):
        shutil.rmtree(OUTDIR)
    os.makedirs(OUTDIR)

    for i in range(NFRAMES):
        t = i / NFRAMES                      # one full side-to-side cycle, loops
        phase = math.sin(2 * math.pi * t)
        yaw = math.radians(YAW_DEG) * phase
        roll = math.radians(ROLL_DEG) * math.sin(2 * math.pi * t + math.pi / 2) * 0.5

        # eases back a touch at the extremes, as if turning away from camera
        breath = 1.0 - 0.015 * phase ** 2
        h = homography(yaw, roll, cx, cy, VIEW, OUT, breath)
        inv = np.linalg.inv(h)
        inv /= inv[2, 2]
        warped = layer_img.transform(
            (OUT, OUT), Image.PERSPECTIVE, inv.flatten()[:8],
            resample=Image.BICUBIC, fillcolor=(255, 255, 255, 0),
        )
        w = np.asarray(warped).astype(np.float32)
        alpha = w[:, :, 3:4]
        frame = w[:, :, :3] * (alpha / 255.0) + 255.0 * (1 - alpha / 255.0)
        frame = fire(frame, phase)
        Image.fromarray(np.clip(frame, 0, 255).astype(np.uint8)).save(
            os.path.join(OUTDIR, f"f{i:04d}.png")
        )

    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        import imageio_ffmpeg
        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

    subprocess.run([
        ffmpeg, "-y", "-framerate", str(FPS), "-i", os.path.join(OUTDIR, "f%04d.png"),
        "-c:v", "libx264", "-preset", "slow", "-crf", "20",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "ring-turn-1080.mp4",
    ], check=True, capture_output=True)
    shutil.copy(os.path.join(OUTDIR, "f0000.png"), "poster.png")
    Image.open("poster.png").convert("RGB").save("ring-turn-poster.jpg", quality=88)
    os.remove("poster.png")
    print("wrote ring-turn-1080.mp4 + ring-turn-poster.jpg")


if __name__ == "__main__":
    main()
