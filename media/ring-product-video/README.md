# Ruby halo ring — product turn video

`ring-turn-1080.mp4` — 5s, 1080×1080, 30fps, H.264 (yuv420p), ~1.9 MB, seamless loop.
`ring-turn-poster.jpg` — first frame, for use as a `poster` / thumbnail.
`source-still.jpg` — the still the video was built from.

The ring turns once to the right and once to the left over the five seconds, easing
through centre, and ends where it started so it loops with no visible cut. Light
sweeps across the stone in sync with the turn.

## Regenerating

```sh
pip install pillow numpy scipy imageio-ffmpeg
python3 make_ring_video.py source-still.jpg frames
```

Frames are written to `frames/` (safe to delete afterwards) and the mp4 + poster
land next to the script. `ffmpeg` is taken from `PATH`, falling back to the one
bundled with `imageio-ffmpeg`.

The knobs are the constants at the top of the script:

| Constant | Effect |
| --- | --- |
| `OUT`, `FPS`, `DURATION` | frame size, frame rate, length (square output) |
| `YAW_DEG` | how far it turns either side of centre |
| `ROLL_DEG` | slight roll for a hand-turned feel |
| `VIEW` | source pixels across the frame — lower crops in tighter |
| `FOCAL` | perspective strength; lower makes the near side of the shank read bigger |
| `GLINT` | how hard light sweeps over the stone |

## How it works

The still is cut off its white background (near-white plus low-saturation test, then
the connected region containing the stone), padded by mirroring left and right so the
shank always runs off-frame instead of showing a cut end, and re-projected each frame
as a plane yawing about the vertical axis through the centre of the head. The pavé is
already at paper-white, so there is no headroom to brighten it — the light sweep is
confined to the stone, where it reads as facet fire.

Not wired into the site; these are standalone assets.
