---
title: "Mpv Keyboard"
description: "mpv-keyboard"
keywords: "mpv,keyboard"

date: 2022-11-04T14:24:27+08:00
lastmod: 2022-11-04T14:24:27+08:00

author: peace0phmind
url: "posts/202211/mpv-keyboard"

draft: false

categories:
  -
tags:
  - mpv

---

## Seek backward/forward 5 seconds 
    LEFT and RIGHT
    Seek backward/forward 5 seconds. Shift+arrow does a 1 second exact seek (see --hr-seek).
## Seek forward/backward 1 minute
    UP and DOWN
    Seek forward/backward 1 minute. Shift+arrow does a 5 second exact seek (see --hr-seek).

## Seek to the previous/next subtitle
    Ctrl+LEFT and Ctrl+RIGHT
    Seek to the previous/next subtitle. Subject to some restrictions and might not always work; see sub-seek command.

## Adjust subtitle delay
    Ctrl+Shift+Left and Ctrl+Shift+Right
    Adjust subtitle delay so that the next or previous subtitle is displayed now. This is especially useful to sync subtitles to audio.

## Decrease/increase speed by 10%
    [ and ]
    Decrease/increase current playback speed by 10%.

## Halve/double speed
    { and }
    Halve/double current playback speed.

## Reset speed
    BACKSPACE
    Reset playback speed to normal.

## Undo the last seek
    Shift+BACKSPACE
    Undo the last seek. This works only if the playlist entry was not changed. Hitting it a second time will go back to the original position. See revert-seek command for details.

## Mark the current position
    Shift+Ctrl+BACKSPACE
    Mark the current position. This will then be used by Shift+BACKSPACE as revert position (once you seek back, the marker will be reset). You can use this to seek around in the file and then return to the exact position where you left off.

## backward/forward playlist
    < and >
    Go backward/forward in the playlist.

## Go forward playlist.
    ENTER
    Go forward in the playlist.

## Pause
    p / SPACE
    Pause (pressing again unpauses).

## Step forward.
    .
    Step forward. Pressing once will pause, every consecutive press will play one frame and then go into pause mode again.

## Step backward
    ,
    Step backward. Pressing once will pause, every consecutive press will play one frame in reverse and then go into pause mode again.

## quit
    q
    Stop playing and quit.

    Q
    Like q, but store the current playback position. Playing the same file later will resume at the old playback position if possible.

## Decrease/increase volume
    / and *
    Decrease/increase volume.
    
    9 and 0
    Decrease/increase volume.

## Mute
    m
    Mute sound.

## Cycle play
    _
    Cycle through the available video tracks.
    
    #
    Cycle through the available audio tracks.

## fullscreen
  f
  Toggle fullscreen (see also --fs).

## Exit fullscreen
    ESC
    Exit fullscreen mode.

## stay-on-top
    T
    Toggle stay-on-top (see also --ontop).

## Decrease/increase pan-and-scan
    w and W
    Decrease/increase pan-and-scan range. The e key does the same as W currently, but use is discouraged.

## Show progression bar
    o (also P)
    Show progression bar, elapsed time and total duration on the OSD.

## Toggle OSD states
    O
    Toggle OSD states between normal and playback time/duration.

## Toggle subtitle
    v
    Toggle subtitle visibility.

## Cycle through the available subtitles
    j and J
    Cycle through the available subtitles.

## Adjust subtitle delay
    z and Z
    Adjust subtitle delay by +/- 0.1 seconds. The x key does the same as Z currently, but use is discouraged.

## Set/clear loop points
    l
    Set/clear A-B loop points. See ab-loop command for details.

## infinite looping
    L
    Toggle infinite looping.

## Adjust audio delay
    Ctrl + and Ctrl -
    Adjust audio delay (A/V sync) by +/- 0.1 seconds.

## Adjust subtitle font size
    Shift+g and Shift+f
    Adjust subtitle font size by +/- 10%.

## subtitles ass overrides
    u
    Switch between applying no style overrides to SSA/ASS subtitles, and overriding them almost completely with the normal subtitle style. See --sub-ass-override for more info.

## subtitle VSFilter aspect compatibility mode
    V
    Toggle subtitle VSFilter aspect compatibility mode. See --sub-ass-vsfilter-aspect-compat for more info.

## Move subtitles up/down
    r and R
    Move subtitles up/down. The t key does the same as R currently, but use is discouraged.

## screenshot
    s
    Take a screenshot.

    S
    Take a screenshot, without subtitles. (Whether this works depends on VO driver support.)

    Ctrl s
    Take a screenshot, as the window shows it (with subtitles, OSD, and scaled video).

## Seek to the beginning of the previous/next chapter
    PGUP and PGDWN
    Seek to the beginning of the previous/next chapter. In most cases, "previous" will actually go to the beginning of the current chapter; see --chapter-seek-threshold.

## Seek backward or forward by 10 minutes
    Shift+PGUP and Shift+PGDWN
    Seek backward or forward by 10 minutes. (This used to be mapped to PGUP/PGDWN without Shift.)

## Activate/deactivate deinterlacer
    d
    Activate/deactivate deinterlacer.

## Cycle aspect ratio
    A
    Cycle aspect ratio override.

## hardware video decoding
    Ctrl h
    Toggle hardware video decoding on/off.

## Move the video rectangle
    Alt+LEFT, Alt+RIGHT, Alt+UP, Alt+DOWN
    Move the video rectangle (panning).

## changes video zoom
    Alt + and Alt -
    Combining Alt with the + or - keys changes video zoom.

## Reset pan/zoom
    Alt+BACKSPACE
    Reset the pan/zoom settings.

## Show the playlist
    F8
    Show the playlist and the current position in it (useful only if a UI window is used, broken on the terminal).

## Show the list of audio and subtitle streams
    F9
    Show the list of audio and subtitle streams (useful only if a UI window is used, broken on the terminal).

## displaying statistics
    i and I
    Show/toggle an overlay displaying statistics about the currently playing file such as codec, framerate, number of dropped frames and so on. See STATS for more information.

## Cycle OSC
    del
    Cycle OSC visibility between never / auto (mouse-move) / always

## Show console
    `
    Show the console. (ESC closes it again. See CONSOLE.)

## ref
[mpv manual](https://mpv.io/manual/stable/)
